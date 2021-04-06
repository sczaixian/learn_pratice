
import os
import time
import socket
# import logging
import threading
# pip install lupa
from lupa import LuaRuntime


class RedisLock1(object):
    '''加锁操作非原子性
    在这个版本中，当线程 A get(key) 的值为空时，set key 的值为 1，
    并返回，这表示线程 A 获得了锁，可以继续执行后面的操作，
    否则需要一直循环去获取锁，直到 key 的值再次为空，
    重新获得锁，执行任务完毕后释放锁
    '''
    def __init__(self, rediscli):
        self.rediscli = rediscli

    def get_lock_key(self, key):
        lock_key = "lock_%s" % key
        return lock_key

    # def get_lock(self, key):
    #     lock_key = self.get_lock_key(key)
    #     while True:
    #         value = self.rediscli.get(lock_key)
    #         if not value:
    #             self.rediscli.set(lock_key, '1')
    #             return True
    #         time.sleep(0.01)

    '''使用 setnx 来实现
    鉴于上面版本是由于命令不是原子性操作造成两个或多个线程同时获得锁的问题，
    这个版本改成使用 redis 的 setnx 命令来进行锁的查询和设置操作，
    setnx 即 set if not exists，
    顾名思义就是当key不存在的时候才设置 value，
    并返回 1，如果 key 已经存在，则不进行任何操作，返回 0
    
    '''
    # def get_lock(self, key):
    #     lock_key = self.get_lock_key(key)
    #     while True:
    #         value = self.rediscli.setnx(lock_key, 1)  # TODO:
    #         if value:
    #             return True
    #         time.sleep(0.01)

    '''
    还是会出问题的，比如假设 A 线程获得了锁后，由于某种异常原因导致线程 crash了，
    一直不释放锁呢？我们稍微改一下测试用例的 increase 函数，
    模拟某个线程在释放锁之前因为异常退出
    线程 2 crash 之后，后续的线程一直获取不了锁，便一直处于等待锁的状态，于是乎产生了死锁。
    如果数据是多线程处理的，比如每来一个数据就开一个线程去处理，那么堆积的线程会逐渐增多，最终可能会导致系统崩溃。

    产生锁的线程由于异常退出，没法释放锁，我们可能就得曲线救国，找其他方式来释放锁了。
    既然我们使用了 redis 来实现分布式锁，何不利用 redis 的 ttl 机制呢，
    给锁加上过期时间，不就可以解决了上面的问题了吗？
    但如果是这样的方式处理，使用 redis expire 来设置锁的过期时间
    value = self.rediscli.setnx(lock_key, '1')
    if value:
        self.rediscli.expire(lock_key, 5)
    貌似又回到了第一版的操作命令不是原子性的问题，查看redis手册，
    好在从 redis 2.6.12 版本开始，set 命令就已经支持了 nx 和 expire 功能
    '''
    def get_lock(self, key, timeout=3):
        lock_key = self.get_lock_key(key)
        while True:
            value = self.rediscli.set(lock_key, '1', nx=True, ex=timeout)
            if value:
                return True
            time.sleep(0.01)

    '''
    比如假设 A 进程的逻辑还没处理完，但是锁由于过期时间到了，
    导致锁自动释放掉，这时 B 线程获得了锁，
    开始处理 B 的逻辑，然后 A 进程的逻辑处理完了，
    就把 B 进程的锁给删除了呢？这也是下面要讲的问题
    
        方式三：锁的生成和删除必须是同一个线程
    
    由于锁过期导致误删别人家的锁引发的，那我们就顺着这个思路，强制线程只能删除自己设置的锁。
    如果是这样，就得被每个线程的锁添加一个唯一标识了。
    看看上面的锁机制，我们每次添加锁的时候，
    都是给 lock_key 设为 1，无论是 key 还是 value，都不具备唯一性，
    如果把 key 设为每个线程唯一的，
    那在分布式系统中，得产生 N （等于总线程数）个 key 了 ，
    从直观性和维护性上来说，这都是不可取的，于是乎只能从 value 入手了。
    我们看到每个线程都可以取到一个唯一标识，即线程 ID，如果加上进程的 PID，
    以及机器的 IP，就可以构成一个线程锁的唯一标识了，
    如果还担心不够唯一，再打上一个时间戳了，
    于是乎，我们的分布式锁最终版就变成了以下这样
    '''

    def del_lock(self, key, new_expire_time):
        lock_key = self.get_lock_key(key)
        return self.rediscli.delete(lock_key)


class RedisLock2(object):

    def __init__(self, rediscli):
        self.rediscli = rediscli.master
        # ip 在实例化的时候就获取，避免过多访问DNS
        self.ip = socket.gethostbyname(socket.gethostname())
        self.pid = os.getpid()

    def gen_lock_key(self, key):
        lock_key = "lock_%s" % key
        return lock_key

    def gen_unique_value(self):
        thread_name = threading.current_thread().name
        time_now = time.time()
        unique_value = "{0}-{1}-{2}-{3}".format(self.ip, self.pid, thread_name, time_now)
        return unique_value

    def get(self, key, timeout=3):
        lock_key = self.gen_lock_key(key)
        unique_value = self.gen_unique_value()
        # logger.info("unique value %s" % unique_value)
        print("unique value %s" % unique_value)
        while True:
            value = self.rediscli.set(lock_key, unique_value, nx=True, ex=timeout)
            if value:
                return unique_value
            # 进入阻塞状态，避免一直消耗CPU
            time.sleep(0.1)

    def delete(self, key, value):
        lock_key = self.gen_lock_key(key)
        old_value = self.rediscli.get(lock_key)
        '''
        以上我们设置值的唯一性只能确保线程不会误删其他线程产生的锁，进而出现连串的误删锁的情况，
        比如 A 删了 B 的锁，B 执行完删了 C 的锁 。
        使用 redis 的过期机制，只要业务的处理时间大于锁的过期时间，
        就没有一个很好的方式来避免由于锁过期导致其他线程同时占有锁的问题，
        所以需要熟悉业务的执行时间，来合理地设置锁的过期时间。

        还需注意的一点是，以上的实现方式中，删除锁（del_lock）的操作不是原子性的，
        先是拿到锁，再判断锁的值是否相等，相等的话最后再删除锁，
        既然不是原子性的，就有可能存在这样一种极端情况：在判断的那一时刻，锁正好过期了，
        被其他线程占有了锁，那最后一步的删除，就可能会造成误删锁了。
        可以使用官方推荐的 Lua 脚本来确保原子性
        '''
        # file_handler = open('./test.lua')
        # content = ''
        # try:
        #     content = file_handler.read()
        # except Exception as e:
        #     print('error : %s' % e)
        # lua_runtime = LuaRuntime()
        # lua_runtime.execute(content)
        if old_value == value:
            return self.rediscli.delete(lock_key)