
import time
import threading
import redis
# from ..util.redis_utils import StringDAL as RedisCli
from test_redis_lock import RedisLock1


def increase(redis, lock, key):
    # 获得锁
    lock_value = lock.get_lock(key)
    value = redis.get(key)
    # 模拟实际情况下进行的某些耗时操作
    time.sleep(0.1)
    value += 1
    redis.set(key, value)
    thread_name = threading.current_thread().name
    # 打印线程名和最新的值
    print(thread_name, 'new_value')
    # 释放锁
    lock.del_lock(key, lock_value)


def test():
    # 连接服务端
    rds = redis.StrictRedis(decode_responses=True)
    lock = RedisLock1(rds)
    key = 'test_key'
    thread_count = 10
    rds.delete(key)
    for i in range(thread_count):
        thread = threading.Thread(target=increase, args=(redis, lock, key))
        thread.start()


# from lupa import LuaRuntime
# file_handler = open('./test.lua')
# content = ''
# try:
#     content = file_handler.read()
# except Exception as e:
#     print('error : %s' % e)
# lua_runtime = LuaRuntime()
# lua_runtime.execute(content)



