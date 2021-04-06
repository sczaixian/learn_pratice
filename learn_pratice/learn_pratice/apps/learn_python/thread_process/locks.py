
import threading
import time

'''
死锁
死锁是一个资源被多次调用，而多次调用方都未能释放该资源就会造成死锁，这里结合例子说明下两种常见的死锁情况

1   迭代死锁
'''
class MyThread1(threading.Thread):
    def run(self):
        global num1
        time.sleep(1)
        if mutex1.acquire(1):
            num1 = num1 + 1
            msg = self.name+' set num to '+str(num1)
            print(msg)
            mutex1.acquire()
            mutex1.release()
            mutex1.release()


num1 = 0
mutex1 = threading.Lock()


def test1():
    for i in range(5):
        t = MyThread1()
        t.start()


# test1()


'''互相调用死锁'''
class MyThread2(threading.Thread):
    def do1(self):
        global resA, resB
        if mutexA.acquire():
            msg = self.name+' got resA'
            print(msg)
            if mutexB.acquire(1):
                msg = self.name+' got resB'
                print(msg)
                mutexB.release()
                mutexA.release()

    def do2(self):
        global resA, resB
        if mutexB.acquire():
            msg = self.name+' got resB'
            print(msg)
            if mutexA.acquire(1):
                msg = self.name+' got resA'
                print(msg)
                mutexA.release()
            mutexB.release()

    def run(self):
        self.do1()
        self.do2()


resA = 0
resB = 0
mutexA = threading.Lock()
mutexB = threading.Lock()


def test2():
    for i in range(5):
        t = MyThread2()
        t.start()


# test2()


'''可重入锁 解决了1的问题'''
class MyThread3(threading.Thread):
    def run(self):
        global num3
        time.sleep(1)
        if mutex3.acquire(1):
            num3 = num3 + 1
            msg = self.name+' set num to '+str(num3)
            print(msg)
            mutex3.acquire()
            mutex3.release()
            mutex3.release()


num3 = 0
mutex3 = threading.RLock()


def test3():
    for i in range(5):
        t = MyThread3()
        t.start()


# test3()




'''
三、互斥锁
python threading模块有两类锁：互斥锁（threading.Lock ）和可重用锁（threading.RLock）。两者的用法基本相同
'''
class mythread(threading.Thread):    # 通过继承创建类

  def __init__(self, threadname):   # 初始化方法
    # 调用父类的初始化方法
    threading.Thread.__init__(self, name=threadname)

  def run(self):             # 重载run方法
    global x         # 使用global表明x为全局变量
    lock.acquire()
    for i in range(30):
      x = x + 1
    # time.sleep(5)     # 调用sleep函数，让线程休眠5秒
    lock.release()
    print(x)


lock = threading.Lock()
tl = []               # 定义列表

for i in range(10):
  t = mythread(str(i))        # 类实例化
  tl.append(t)           # 将类对象添加到列表中


x = 0                 # 将x赋值为0

for i in tl:
  i.start()



'''
由于没有线程安全，在两个线程中，在操作+1的操作时，
比如目前g_num=10，此时test1和test2同时拿到g_num=10，
然后都进行+1操作，我们期望结果是12，但是由于都是10+1，所以结果是11.
'''
global_num = 0
def test1():
    global global_num
    for i in range(1000000):
        # mutex_flag = mutex.acquire(True)
        # if mutex_flag:
            global_num += 1
            # mutex.release()

    print("---test1---g_num=%d" % global_num )


def test2():
    global global_num
    for i in range(1000000):
        # mutex_flag = mutex.acquire(True)
        # if mutex_flag:
            global_num += 1
            # mutex.release()

    print("---test2---g_num=%d" % global_num )


mutex = threading.Lock()

p1 = threading.Thread(target=test1)
p2 = threading.Thread(target=test2)
p1.start()
p2.start()

print("---curr_g_num=%d---" % global_num )

