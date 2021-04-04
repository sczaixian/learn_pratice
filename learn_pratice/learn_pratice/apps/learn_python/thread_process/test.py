
import queue
# import threading
# import time
#
# def test():
#
#     for i in range(5):
#         print(threading.current_thread().name+' test ',i)
#         time.sleep(0.5)
#
#
# thread = threading.Thread(target=test,name='fdsTh')
# thread.start()
# print('----------w-------')
# thread.join()
# print('---------s--------')
#
# for i in range(5):
#     print(threading.current_thread().name+' main ', i)
#     print(thread.name+' is alive ', thread.isAlive())
#     time.sleep(1)
# # 主线程创建了 TestThread 对象后，让其 start，然后通过调用 join() 方法，实现等待。程序运行结果如下



#
# import threading
# import time
#
# def test():
#
#     for i in range(5):
#         print(threading.current_thread().name+' test ',i)
#         time.sleep(2)
#
#
# thread = threading.Thread(target=test,name='TestThread', daemon=True)
# # thread = threading.Thread(target=test,name='TestThread',daemon=True)
# thread.start()
#
#
# for i in range(5):
#     print(threading.current_thread().name+' main ', i)
#     print(thread.name+' is alive ', thread.isAlive())
#     time.sleep(1)


# import time, threading
#
# # 假定这是你的银行存款:
# balance = 0
# lock = threading.Lock()
#
# def change_it(n):
#     # 先存后取，结果应该为0:
#     global balance
#     balance = balance + n
#     balance = balance - n
#
# def run_thread(n):
#     start = time.time()
#     # 百万级别以上的计算成本相当高
#     for i in range(1000000):
#         change_it(n)
#         # -------------------------------
#         # lock.acquire()
#         # try:
#         #     change_it(n)
#         # finally:
#         #     lock.release()
#         # ---------------------------------
#         # with lock:
#         #     change_it(n)
#     print('-----:  ', time.time() - start)
#
#
# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)

#

# import time, threading
#
# local_data = threading.local()
# balance = 0
#
# def change_it(n):
#     # 先存后取，结果应该为0:
#     local_data.balance += n
#     local_data.balance -= n
#
#
# def run_thread(n):
#     local_data.balance = 0
#     start = time.time()
#     # 百万级别以上的计算成本相当高
#     for i in range(1000000):
#         change_it(n)
#     print('-----:  ', time.time() - start)
#     global balance
#     balance = local_data.balance
#
# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)

# import threading
#
# # 创建全局ThreadLocal对象:
# local_school = threading.local()
#
#
# def process_student():
#     # 获取当前线程关联的student:
#     std = local_school.student
#     print('Hello, %s (in %s)' % (std, threading.current_thread().name))
#
#
# def process_thread(name):
#     # 绑定ThreadLocal的student:
#     local_school.student = name
#     process_student()
#
#
# t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
# t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
# t1.start()
# t2.start()
# t1.join()
# t2.join()


# xyz = 100
# def change(arg):
#     if arg is 1:
#         t1()
#     else:
#         t2()
# def t1():
#     xyz = 1
# def t2():
#     global xyz
#     xyz = 1
# change(1)
# print(xyz)
# change(2)
# print(xyz)
import threading
class ss(threading.Thread):
    def __init__(self):
        super(ss, self).__init__()