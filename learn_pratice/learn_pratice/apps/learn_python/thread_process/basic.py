
import time
import threading

'''
一、进程与线程：
进程是资源分配的最小单位，一个程序至少有一个进程。

线程是程序执行的最小单位，一个进程至少有一个线程。

进程都有自己独立的地址空间，内存，数据栈等，所以进程占用资源多。由于进程的资源独立，所以通讯不方便，只能使用进程间通讯（IPC）。

线程共享进程中的数据，他们使用相同的地址空间，使用线程创建快捷，创建开销比进程小。同一进程下的线程共享全局变量、静态变量等数据，所以线程通讯非常方便，但会存在数据同步与互斥的问题，如何处理好同步与互斥是编写多线程程序的难点。

一个进程中可以存在多个线程，在单核CPU中每个进程中同时刻只能运行一个线程，只有在多核CPU中才能存在线程并发的情况。

当线程需要运行但没有运行空间时，会对线程的优先级进行判断，高优先级先运行，低优先级进程让行。

二、全局解释器锁（GIL）
Python的多线程，只有用于I/O密集型程序时效率才会有明显的提高。

原因如下：

Python代码的执行是由Python虚拟机进行控制。它在主循环中同时只能有一个控制线程在执行，意思就是Python解释器中可以运行多个线程，但是在执行的只有一个线程，其他的处于等待状态。

这些线程执行是有全局解释器锁（GIL）控制，它来保证同时只有一个线程在运行。在多线程运行环境中，Python虚拟机执行方式如下：

设置GIL
切换进线程
执行下面操作之一
运行指定数量的字节码指令
线程主动让出控制权
切换出线程（线程处于睡眠状态）
解锁GIL
进入1步骤
注意：Python运行计算密集型的多线程程序时，更倾向于让线程在整个时间片内始终占据GIL，而I/O秘籍型的多线程程序在I/O被调用前会释放GIL，以允许其他线程在I/O执行的时候运行。
三、Python 的 threading 模块
Python 常用的多线程模块有threading 和 Queue，在这里我们将 threading 模块。

threading 模块的Thread 类是主要的执行对象。使用Thread 类，可以有很多方法来创建线程。最常用的有下面三种：

创建Thread 的实例，传给它一个可调用对象（函数或者类的实例方法）。
派生Thread 的子类，并创建子类的实例。
3.1 可调用对象（函数，类的实例方法）使用多线程
/imgs/Multithreading.jpg
'''
'''
补充1：threading 模块的类与函数

1. threading 模块的类对象
    Thread              执行线程
    Timer               在运行前等待一段时间的执行线程
    Lock                原语锁（互斥锁，简单锁）
    RLock               重入锁，使单一线程可以（再次）获得已持有的锁
    Condition           条件变量，线程需要等待另一个线程满足特定条件
    Event               事件变量，N个线程等待某个事件发生后激活所有线程
    Semaphore           线程间共享资源的寄存器
    BoundedSemaphore    与Semaphore 相似，它不允许超过初始值
    Barrie              执行线程达到一定数量后才可以继续
2. threading 模块的函数
    activeCount()       获取当前活动中的Thread对象个数
    currentThread()     获取当前的Thread对象
    enumerate()         获取当前活动的Thread对象列表
    settrace(func)      为所有线程设置一个跟踪（trace）函数
    setprofile(func)    为所有线程设置配置文件（profile）函数
    stack_size(size=None) 获取新创建线程的栈大小，也可设置线程栈的大小为size。


补充2 ：Thread 类的属性与方法
threading 中的 Thread 类是主要的执行对象，主要方法和属性如下：

属性
    name    线程名称
    ident   线程标识符号
    daemon  是否为守护线程
方法
___init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None)
    参数：
    group               无用，保留参数
    target              可调用的目标
    name                线程的名称
    args,kwargs         调用目标的参数
    daemon              是否为守护线程
    start()             开始执行
    join(timeout=None)  阻塞timeout秒，否则直到启动的线程终止前一直挂起
    is_alive ()         线程是否存活
    isDaemon()          是否为守护线程
    setDaemon(daemonic) 设置为守护线程
'''


'''------------------------------------------------------------------------------------'''


'''
很多同学都听说过，现代操作系统比如Mac OS X，UNIX，Linux，Windows等，都是支持“多任务”的操作系统。

什么叫“多任务”呢？简单地说，就是操作系统可以同时运行多个任务。
    打个比方，你一边在用浏览器上网，一边在听MP3，一边在用Word赶作业，
    这就是多任务，至少同时有3个任务正在运行。还有很多任务悄悄地在后台同时运行着，只是桌面上没有显示而已。

现在，多核CPU已经非常普及了，但是，即使过去的单核CPU，也可以执行多任务。
    由于CPU执行代码都是顺序执行的，那么，单核CPU是怎么执行多任务的呢？

答案就是操作系统轮流让各个任务交替执行，
    任务1执行0.01秒，切换到任务2，任务2执行0.01秒，再切换到任务3，执行0.01秒……这样反复执行下去。
    表面上看，每个任务都是交替执行的，但是，由于CPU的执行速度实在是太快了，我们感觉就像所有任务都在同时执行一样。

真正的并行执行多任务只能在多核CPU上实现，但是，由于任务数量远远多于CPU的核心数量，所以，操作系统也会自动把很多任务轮流调度到每个核心上执行。

对于操作系统来说，一个任务就是一个进程（Process），比如打开一个浏览器就是启动一个浏览器进程，
打开一个记事本就启动了一个记事本进程，打开两个记事本就启动了两个记事本进程，打开一个Word就启动了一个Word进程。

有些进程还不止同时干一件事，比如Word，它可以同时进行打字、拼写检查、打印等事情。
在一个进程内部，要同时干多件事，就需要同时运行多个“子任务”，我们把进程内的这些“子任务”称为线程（Thread）。

由于每个进程至少要干一件事，所以，一个进程至少有一个线程。
    当然，像Word这种复杂的进程可以有多个线程，多个线程可以同时执行，多线程的执行方式和多进程是一样的，
    也是由操作系统在多个线程之间快速切换，让每个线程都短暂地交替运行，看起来就像同时执行一样。
    当然，真正地同时执行多线程需要多核CPU才可能实现。

我们前面编写的所有的Python程序，都是执行单任务的进程，也就是只有一个线程。
如果我们要同时执行多个任务怎么办？

有两种解决方案：

    一种是启动多个进程，每个进程虽然只有一个线程，但多个进程可以一块执行多个任务。
    
    还有一种方法是启动一个进程，在一个进程内启动多个线程，这样，多个线程也可以一块执行多个任务。
    
    当然还有第三种方法，就是启动多个进程，每个进程再启动多个线程，这样同时执行的任务就更多了，当然这种模型更复杂，实际很少采用。

总结一下就是，多任务的实现有3种方式：

    多进程模式；
    多线程模式；
    多进程+多线程模式。
    
同时执行多个任务通常各个任务之间并不是没有关联的，而是需要相互通信和协调，
有时，任务1必须暂停等待任务2完成后才能继续执行，有时，任务3和任务4又不能同时执行，
所以，多进程和多线程的程序的复杂度要远远高于我们前面写的单进程单线程的程序。

因为复杂度高，调试困难，所以，不是迫不得已，我们也不想编写多任务。
但是，有很多时候，没有多任务还真不行。想想在电脑上看电影，
就必须由一个线程播放视频，另一个线程播放音频，
否则，单线程实现的话就只能先把视频播放完再播放音频，
或者先把音频播放完再播放视频，这显然是不行的。

Python既支持多进程，又支持多线程，我们会讨论如何编写这两种多任务程序。
'''

'''
要让Python程序实现多进程（multiprocessing），我们先了解操作系统的相关知识。

Unix/Linux操作系统提供了一个fork()系统调用，
    它非常特殊。普通的函数调用，调用一次，返回一次，
        但是fork()调用一次，返回两次，
        因为操作系统自动把当前进程（称为父进程）
        复制了一份（称为子进程），然后，分别在父进程和子进程内返回。

子进程永远返回0，而父进程返回子进程的ID。
这样做的理由是，
    一个父进程可以fork出很多子进程，
    所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID。

Python的os模块封装了常见的系统调用，其中就包括fork，可以在Python程序中轻松创建子进程：

由于Windows没有fork调用
有了fork调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务，
常见的Apache服务器就是由父进程监听端口，
每当有新的http请求时，就fork出子进程来处理新的http请求
'''

# import os
#
# print('Process (%s) start...' % os.getpid())
# # Only works on Unix/Linux/Mac:
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
'''
Process (876) start...
I (876) just created a child process (877).
I am child process (877) and my parent is 876.
'''


'''
多进程
    multiprocessing模块就是跨平台版本的多进程模块。
    multiprocessing模块提供了一个Process类来代表一个进程对象，
        下面的例子演示了启动一个子进程并等待其结束
            创建子进程时，只需要传入一个执行函数和函数的参数，
            创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单。
            join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
'''

# from multiprocessing import Process
# import os
#
# # 子进程要执行的代码
# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))
#
# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end.')

'''
Parent process 928.
Child process will start.
Run child process test (929)...
Process end.
'''

'''
Pool
如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
'''
# from multiprocessing import Pool
# import os, time, random
#
# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))
#
# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')
'''
Parent process 669.
Waiting for all subprocesses done...
Run task 0 (671)...
Run task 1 (672)...
Run task 2 (673)...
Run task 3 (674)...
Task 2 runs 0.14 seconds.
Run task 4 (673)...
Task 1 runs 0.27 seconds.
Task 3 runs 0.86 seconds.
Task 0 runs 1.41 seconds.
Task 4 runs 1.91 seconds.
All subprocesses done.
'''

# TODO: 后面的没加上
#       地址是: https://www.liaoxuefeng.com/wiki/1016959663602400/1017628290184064


'''------------------------------------------------------------------------------------'''


'''
进程是资源（CPU、内存等）分配的基本单位，它是程序执行时的一个实例。
程序运行时系统就会创建一个进程，并为它分配资源，然后把该进程放入进程就绪队列
进程调度器选中它的时候就会为它分配CPU时间，程序开始真正运行。


线程是程序执行时的最小单位，它是进程的一个执行流，是CPU调度和分派的基本单位。
一个进程可以由很多个线程组成，线程间共享进程的所有资源，每个线程有自己的堆栈和局部变量。
线程由CPU独立调度执行，在多CPU环境下就允许多个线程同时运行。
同样多线程也可以实现并发操作，每个请求分配一个线程来处理。


与进程相关的资源包括:
内存页（同一个进程中的所有线程共享同一个内存空间）
文件描述符(e.g. open sockets)
安全凭证（e.g.启动该进程的用户ID）

1.3 进程与线程区别
1.同一个进程中的线程共享同一内存空间，但是进程之间是独立的。
2.同一个进程中的所有线程的数据是共享的（进程通讯），进程之间的数据是独立的。
3.对主线程的修改可能会影响其他线程的行为，但是父进程的修改（除了删除以外）不会影响其他子进程。
4.线程是一个上下文的执行指令，而进程则是与运算相关的一簇资源。
5.同一个进程的线程之间可以直接通信，但是进程之间的交流需要借助中间代理来实现。
6.创建新的线程很容易，但是创建新的进程需要对父进程做一次复制。
7.一个线程可以操作同一进程的其他线程，但是进程只能操作其子进程。
8.线程启动速度快，进程启动速度慢（但是两者运行速度没有可比性）。

'''


'''

2.1 线程常用方法

方法	            注释
start()	        线程准备就绪，等待CPU调度
setName()	    为线程设置名称
getName()	    获取线程名称
setDaemon(True)	设置为守护线程
join()	        逐个执行每个线程，执行完毕后继续往下执行
run()	        线程被cpu调度后自动执行线程对象的run方法，如果想自定义线程类，直接重写run方法就行了

'''


'''# 1.普通创建方式'''
# import threading
# import time
#
# def run(n):
#     print("task", n)
#     time.sleep(1)
#     print('2s')
#     time.sleep(1)
#     print('1s')
#     time.sleep(1)
#     print('0s')
#     time.sleep(1)
#
# t1 = threading.Thread(target=run, args=("t1",))
# t2 = threading.Thread(target=run, args=("t2",))
# t1.start()
# t2.start()

'''
# 2.继承threading.Thread来自定义线程类
# 其本质是重构Thread类中的run方法
'''
# import threading
# import time

# class MyThread(threading.Thread):
#     def __init__(self, n):
#         super(MyThread, self).__init__()  # 重构run函数必须要写
#         self.n = n
#
#     def run(self):
#         print("task", self.n)
#         time.sleep(1)
#         print('2s')
#         time.sleep(1)
#         print('1s')
#         time.sleep(1)
#         print('0s')
#         time.sleep(1)
#
#
# if __name__ == "__main__":
#     t1 = MyThread("t1")
#     t2 = MyThread("t2")
#
#     t1.start()
#     t2.start()


'''
# 计算子线程执行的时间
# sleep的时候是不会占用cpu的,在sleep的时候操作系统会把线程暂时挂起
# join()    #等此线程执行完后，再执行其他线程或主线程
# threading.current_thread()    #输出当前线程
'''
# import threading
# import time
#
# def run(n):
#     print("task", n,threading.current_thread())    #输出当前的线程
#     time.sleep(1)
#     print('3s')
#     time.sleep(1)
#     print('2s')
#     time.sleep(1)
#     print('1s')
#
# strat_time = time.time()
#
# t_obj = []   #定义列表用于存放子线程实例
#
# for i in range(3):
#     t = threading.Thread(target=run, args=("t-%s" % i,))
#     t.start()
#     t_obj.append(t)
#
# """
# 由主线程生成的三个子线程
# task t-0 <Thread(Thread-1, started 44828)>
# task t-1 <Thread(Thread-2, started 42804)>
# task t-2 <Thread(Thread-3, started 41384)>
# """
#
# for tmp in t_obj:
#     t.join()            #为每个子线程添加join之后，主线程就会等这些子线程执行完之后再执行。
#
# print("cost:", time.time() - strat_time) #主线程
#
# print(threading.current_thread())       #输出当前线程

'''
统计当前活跃的线程数
由于主线程比子线程快很多，当主线程执行active_count()时，
其他子线程都还没执行完毕，
因此利用主线程统计的活跃的线程数num = sub_num(子线程数量)+1(主线程本身)
'''
# import threading
# import time
#
# def run(n):
#     print("task", n)
#     time.sleep(1)       #此时子线程停1s
#
# for i in range(3):
#     t = threading.Thread(target=run, args=("t-%s" % i,))
#     t.start()
#
# time.sleep(0.5)     #主线程停0.5秒
# print(threading.active_count()) #输出当前活跃的线程数
#
"""
task t-0
task t-1
task t-2
4
"""

# 由于主线程比子线程慢很多，当主线程执行active_count()时，其他子线程都已经执行完毕，
# 因此利用主线程统计的活跃的线程数num = 1(主线程本身)
# import threading
# import time
#
#
# def run(n):
#     print("task", n)
#     time.sleep(0.5)       #此时子线程停0.5s
#
#
# for i in range(3):
#     t = threading.Thread(target=run, args=("t-%s" % i,))
#     t.start()
#
# time.sleep(1)     #主线程停1秒
# print(threading.active_count()) #输出活跃的线程数
"""
task t-0
task t-1
task t-2
1
"""
'''
此外我们还能发现在python内部默认会等待最后一个进程执行完后再执行exit()，
或者说python内部在此时有一个隐藏的join()。
'''


'''
守护进程
我们看下面这个例子，这里使用setDaemon(True)
把所有的子线程都变成了主线程的守护线程，
因此当主进程结束后，子线程也会随之结束。
所以当主线程结束后，整个程序就退出了
'''
# import threading
# import time
#
# def run(n):
#     print("task", n)
#     time.sleep(1)       #此时子线程停1s
#     print('3')
#     time.sleep(1)
#     print('2')
#     time.sleep(1)
#     print('1')
#
# for i in range(3):
#     t = threading.Thread(target=run, args=("t-%s" % i,))
#     t.setDaemon(True)   #把子进程设置为守护线程，必须在start()之前设置
#     t.start()
#
# time.sleep(0.5)     #主线程停0.5秒
# print(threading.active_count()) #输出活跃的线程数
"""
task t-0
task t-1
task t-2
4

Process finished with exit code 0
"""


'''
GIL
在非python环境中，单核情况下，同时只能有一个任务执行。多核时可以支持多个线程同时执行。
但是在python中，无论有多少核，同时只能执行一个线程。究其原因，这就是由于GIL的存在导致的。

GIL的全称是Global Interpreter Lock(全局解释器锁)，来源是python设计之初的考虑，
为了数据安全所做的决定。某个线程想要执行，必须先拿到GIL，我们可以把GIL看作是“通行证”，
并且在一个python进程中，GIL只有一个。拿不到通行证的线程，就不允许进入CPU执行。GIL只在cpython中才有，
因为cpython调用的是c语言的原生线程，所以他不能直接操作cpu，只能利用GIL保证同一时间只能有一个线程拿到数据。
而在pypy和jpython中是没有GIL的。

Python多线程的工作过程：
python在使用多线程的时候，调用的是c语言的原生线程。

1. 拿到公共数据
2. 申请gil
3. python解释器调用os原生线程
4. os操作cpu执行运算
5. 当该线程执行时间到后，无论运算是否已经执行完，gil都被要求释放
6. 进而由其他进程重复上面的过程
7. 等其他进程执行完后，又会切换到之前的线程（从他记录的上下文继续执行）
   整个过程是每个线程执行自己的运算，当执行时间到就进行切换（context switch）。
   
python针对不同类型的代码执行效率也是不同的：
1、CPU密集型代码(各种循环处理、计算等等)，在这种情况下，由于计算工作多，ticks计数很快就会达到阈值，
然后触发GIL的释放与再竞争（多个线程来回切换当然是需要消耗资源的），所以python下的多线程对CPU密集型代码并不友好。

2、IO密集型代码(文件处理、网络爬虫等涉及文件读写的操作)，多线程能够有效提升效率(单线程下有IO操作会进行IO等待，
造成不必要的时间浪费，而开启多线程能在线程A等待时，自动切换到线程B，可以不浪费CPU的资源，从而能提升程序执行效率)。
所以python的多线程对IO密集型代码比较友好。

使用建议？
python下想要充分利用多核CPU，就用多进程。因为每个进程有各自独立的GIL，互不干扰，这样就可以真正意义上的并行执行，
在python中，多进程的执行效率优于多线程(仅仅针对多核CPU而言)。

GIL在python中的版本差异：
1、  在python2.x里，GIL的释放逻辑是当前线程遇见IO操作或者ticks计数达到100时进行释放。（
    ticks可以看作是python自身的一个计数器，专门做用于GIL，
    每次释放后归零，这个计数可以通过sys.setcheckinterval 来调整）。
    而每次释放GIL锁，线程进行锁竞争、切换线程，会消耗资源。并且由于GIL锁存在，
    python里一个进程永远只能同时执行一个线程(拿到GIL的线程才能执行)，
    这就是为什么在多核CPU上，python的多线程效率并不高。

2、  在python3.x中，GIL不使用ticks计数，改为使用计时器（执行时间达到阈值后，当前线程释放GIL），
    这样对CPU密集型程序更加友好，但依然没有解决GIL导致的同一时间只能执行一个线程的问题，所以效率依然不尽如人意。
'''


'''
线程锁

由于线程之间是进行随机调度，并且每个线程可能只执行n条执行之后，当多个线程同时修改同一条数据时可能会出现脏数据，
所以，出现了线程锁，即同一时刻允许一个线程执行操作。线程锁用于锁定资源，你可以定义多个锁, 
像下面的代码, 当你需要独占某一资源时，任何一个锁都可以锁这个资源，就好比你用不同的锁都可以把相同的一个门锁住是一个道理。

由于线程之间是进行随机调度，如果有多个线程同时操作一个对象，如果没有很好地保护该对象，会造成程序结果的不可预期，我们也称此为“线程不安全”。

实测：在python2.7、mac os下，运行以下代码可能会产生脏数据。但是在python3中就不一定会出现下面的问题
'''

# import threading
# import time
#
# def run(n):
#     global num
#     num += 1
#
# num = 0
# t_obj = []
#
# for i in range(20000):
#     t = threading.Thread(target=run, args=("t-%s" % i,))
#     t.start()
#     t_obj.append(t)
#
# for t in t_obj:
#     t.join()
#
# print "num:", num
"""
产生脏数据后的运行结果：
num: 19999
"""


'''
互斥锁（mutex）
为了方式上面情况的发生，就出现了互斥锁(Lock)
'''
# import threading
# import time
#
#
# def run(n):
#     lock.acquire()  #获取锁
#     global num
#     num += 1
#     lock.release()  #释放锁
#
# lock = threading.Lock()     #实例化一个锁对象
#
# num = 0
# t_obj = []
#
# for i in range(20000):
#     t = threading.Thread(target=run, args=("t-%s" % i,))
#     t.start()
#     t_obj.append(t)
#
# for t in t_obj:
#     t.join()
#
# print "num:", num

'''
信号量（BoundedSemaphore类）
互斥锁同时只允许一个线程更改数据，而Semaphore是同时允许一定数量的线程更改数据 ，
比如厕所有3个坑，那最多只允许3个人上厕所，后面的人只能等里面有人出来了才能再进去。
'''
# import threading
# import time
#
#
# def run(n):
#     semaphore.acquire()   #加锁
#     time.sleep(1)
#     print("run the thread:%s\n" % n)
#     semaphore.release()     #释放
#
#
# num = 0
# semaphore = threading.BoundedSemaphore(5)  # 最多允许5个线程同时运行
#
# for i in range(22):
#     t = threading.Thread(target=run, args=("t-%s" % i,))
#     t.start()
#
# while threading.active_count() != 1:
#     pass  # print threading.active_count()
# else:
#     print('-----all threads done-----')


'''
事件（Event类）
python线程的事件用于主线程控制其他线程的执行，事件是一个简单的线程同步对象，其主要提供以下几个方法：
方法	        注释
clear	    将flag设置为“False”
set	        将flag设置为“True”
is_set	    判断是否设置了flag
wait	    会一直监听flag，如果没有检测到flag就一直处于阻塞状态

事件处理的机制：全局定义了一个“Flag”，当flag值为“False”，那么event.wait()就会阻塞，
当flag值为“True”，那么event.wait()便不再阻塞。
'''
# #利用Event类模拟红绿灯
# import threading
# import time
#
# event = threading.Event()
#
#
# def lighter():
#     count = 0
#     event.set()     #初始值为绿灯
#     while True:
#         if 5 < count <=10 :
#             event.clear()  # 红灯，清除标志位
#             print("\33[41;1mred light is on...\033[0m")
#         elif count > 10:
#             event.set()  # 绿灯，设置标志位
#             count = 0
#         else:
#             print("\33[42;1mgreen light is on...\033[0m")
#
#         time.sleep(1)
#         count += 1
#
# def car(name):
#     while True:
#         if event.is_set():      #判断是否设置了标志位
#             print("[%s] running..."%name)
#             time.sleep(1)
#         else:
#             print("[%s] sees red light,waiting..."%name)
#             event.wait()
#             print("[%s] green light is on,start going..."%name)
#
# light = threading.Thread(target=lighter,)
# light.start()
#
# car = threading.Thread(target=car,args=("MINI",))
# car.start()


'''
条件（Condition类）
    使得线程等待，只有满足某条件时，才释放n个线程

定时器（Timer类）
    定时器，指定n秒后执行某操作

from threading import Timer
def hello():
    print("hello, world")
 
t = Timer(1, hello)
t.start()  # after 1 seconds, "hello, world" will be printed
'''



'''
多进程
在linux中，每个进程都是由父进程提供的。每启动一个子进程就从父进程克隆一份数据，但是进程之间的数据本身是不能共享的
'''

# from multiprocessing import Process
# import time
# def f(name):
#     time.sleep(2)
#     print('hello', name)
#
# if __name__ == '__main__':
#     p = Process(target=f, args=('bob',))
#     p.start()
#     p.join()


# from multiprocessing import Process
# import os
#
# def info(title):
#     print(title)
#     print('module name:', __name__)
#     print('parent process:', os.getppid())  #获取父进程id
#     print('process id:', os.getpid())   #获取自己的进程id
#     print("\n\n")
#
# def f(name):
#     info('\033[31;1mfunction f\033[0m')
#     print('hello', name)
#
# if __name__ == '__main__':
#     info('\033[32;1mmain process line\033[0m')
#     p = Process(target=f, args=('bob',))
#     p.start()
#     p.join()


'''
进程间通信
    由于进程之间数据是不共享的，所以不会出现多线程GIL带来的问题。多进程之间的通信通过Queue()或Pipe()来实现

Queue()
    使用方法跟threading里的queue差不多
'''

# from multiprocessing import Process, Queue
#
# def f(q):
#     q.put([42, None, 'hello'])
#
# if __name__ == '__main__':
#     q = Queue()
#     p = Process(target=f, args=(q,))
#     p.start()
#     print(q.get())    # prints "[42, None, 'hello']"
#     p.join()

'''
Pipe()
    Pipe的本质是进程之间的数据传递，而不是数据共享，这和socket有点像。
    pipe()返回两个连接对象分别表示管道的两端，每端都有send()和recv()方法。
    如果两个进程试图在同一时间的同一端进行读取和写入那么，这可能会损坏管道中的数据
'''

# from multiprocessing import Process, Pipe
#
# def f(conn):
#     conn.send([42, None, 'hello'])
#     conn.close()
#
# if __name__ == '__main__':
#     parent_conn, child_conn = Pipe()
#     p = Process(target=f, args=(child_conn,))
#     p.start()
#     print(parent_conn.recv())   # prints "[42, None, 'hello']"
#     p.join()

'''
Manager
    通过Manager可实现进程间数据的共享。Manager()返回的manager对象会通过一个服务进程，
    来使其他进程通过代理的方式操作python对象。
    manager对象支持 
        list, dict, 
        Namespace, 
        Lock, RLock, 
        Semaphore, 
        BoundedSemaphore, 
        Condition, 
        Event, 
        Barrier, 
        Queue, 
        Value ,Array.
'''

# from multiprocessing import Process, Manager
#
# def f(d, l):
#     d[1] = '1'
#     d['2'] = 2
#     d[0.25] = None
#     l.append(1)
#     print(l)
#
# if __name__ == '__main__':
#     with Manager() as manager:
#         d = manager.dict()
#
#         l = manager.list(range(5))
#         p_list = []
#         for i in range(10):
#             p = Process(target=f, args=(d, l))
#             p.start()
#             p_list.append(p)
#         for res in p_list:
#             res.join()
#
#         print(d)
#         print(l)


'''
进程锁（进程同步）
    数据输出的时候保证不同进程的输出内容在同一块屏幕正常显示，防止数据乱序的情况
    如果不使用锁，来自不同进程的输出很容易混淆。
'''

# from multiprocessing import Process, Lock
#
# def f(l, i):
#     l.acquire()
#     try:
#         print('hello world', i)
#     finally:
#         l.release()
#
# if __name__ == '__main__':
#     lock = Lock()
#
#     for num in range(10):
#         Process(target=f, args=(lock, num)).start()


'''
进程池
    由于进程启动的开销比较大，使用多进程的时候会导致大量内存空间被消耗。
    为了防止这种情况发生可以使用进程池，
    （由于启动线程的开销比较小，所以不需要线程池这种概念，多线程只会频繁得切换cpu导致系统变慢，并不会占用过多的内存空间）

进程池中常用方法：
    apply()         同步执行（串行）
    apply_async()   异步执行（并行）
    terminate()     立刻关闭进程池
    join()          主进程等待所有子进程执行完毕。必须在close或terminate()之后。
    close()         等待所有进程结束后，才关闭进程池。

进程池内部维护一个进程序列，当使用时，去进程池中获取一个进程，
如果进程池序列中没有可供使用的进程，那么程序就会等待，直到进程池中有可用进程为止。
在下面的程序中产生了10个进程，但是只能有5同时被放入进程池，
剩下的都被暂时挂起，并不占用内存空间，等前面的五个进程执行完后，再执行剩下5个进程。
'''

# from  multiprocessing import Process,Pool
# import time
#
# def Foo(i):
#     time.sleep(2)
#     return i+100
#
# def Bar(arg):
#     print('-->exec done:',arg)
#
# pool = Pool(5)  #允许进程池同时放入5个进程
#
# for i in range(10):
#     # func子进程执行完后，才会执行callback，否则callback不执行（而且callback是由父进程来执行了）
#     pool.apply_async(func=Foo, args=(i,),callback=Bar)
#     #pool.apply(func=Foo, args=(i,))
#
# print('end')
# pool.close()
# pool.join() # 主进程等待所有子进程执行完毕。必须在close()或terminate()之后。


'''
协程
线程和进程的操作是由程序触发系统接口，最后的执行者是系统，它本质上是操作系统提供的功能。
而协程的操作则是程序员指定的，在python中通过yield，人为的实现并发处理。

协程存在的意义：对于多线程应用，CPU通过切片的方式来切换线程间的执行，线程切换时需要耗时。
协程，则只使用一个线程，分解一个线程成为多个“微线程”，在一个线程中规定某个代码块的执行顺序。

协程的适用场景：当程序中存在大量不需要CPU的操作时（IO）。
常用第三方模块gevent和greenlet。
本质上，gevent是对greenlet的高级封装，因此一般用它就行，这是一个相当高效的模块。
实际上，greenlet就是通过switch方法在不同的任务之间进行切换
'''

# def test1():
#     print(12)
#     gr2.switch()
#     print(34)
#     gr2.switch()
#
# def test2():
#     print(56)
#     gr1.switch()
#     print(78)
#
# gr1 = greenlet(test1)
# gr2 = greenlet(test2)
# gr1.switch()

'''
gevent
    通过joinall将任务f和它的参数进行统一调度，实现单线程中的协程。
    代码封装层次很高，实际使用只需要了解它的几个主要方法即可
'''

# from gevent import monkey; monkey.patch_all()
# import gevent
# import requests
#
# def f(url):
#     print('GET: %s' % url)
#     resp = requests.get(url)
#     data = resp.text
#     print('%d bytes received from %s.' % (len(data), url))
#
# gevent.joinall([
#         gevent.spawn(f, 'https://www.python.org/'),
#         gevent.spawn(f, 'https://www.yahoo.com/'),
#         gevent.spawn(f, 'https://github.com/'),
# ])


'''
百度快照
http://cache.baiducontent.com/c?m=wElSz55zB6uXmGwlFd-D7_n_klKSF0xX1qrSuXwPAvyaJvJc2qpBCgGy3rq-TvFUCO9WHbkeAKBqcbjpDYt-pigHNhYIPgKLglVK-lNSWSlB62VrdP7KpmoZeRhHAdgl70_3SHM_ix4r5Ls0dR4aCnW8o4ViOWJePQMreR6ns27rxVAFh6gcfAIvuzdUAcRDOa2Lw3QdKU8ChF21fFJsHcL75RiBmYctDegEGljq14z9rH2Z7PSn9AumhM1fXYFm&p=aa6cde1885cc43ff57ee94785454cd&newp=8b2a971186cc42af5eb3f868544897231610db2151d0d601298ffe0cc4241a1a1a3aecbf2c241701d6c67c6d0aa9435de9f63d723d0034f1f689df08d2ecce7e7b&s=8f14e45fceea167a&user=baidu&fm=sc&query=https%3A//www%2Ecnblogs%2Ecom/whatisfantasy/p/6440585%2Ehtml&qid=d944ce74000be4c1&p1=3
'''