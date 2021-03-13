import os
import time
import random
import subprocess
from multiprocessing import Process, Pool, Queue
'''
Unix/Linux操作系统提供了一个fork()系统调用，
它非常特殊。普通的函数调用，调用一次，返回一次，
但是fork()调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），
然后，分别在父进程和子进程内返回。

子进程永远返回0，而父进程返回子进程的ID。
这样做的理由是，一个父进程可以fork出很多子进程，
所以，父进程要记下每个子进程的ID，
而子进程只需要调用getppid()就可以拿到父进程的ID。
'''
print('Process   (%s)   start' % os.getpid())
pid = os.fork()
if pid == 0:
    print('I am child process (%s)  and my parent is %s' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

'''
multiprocessing模块就是跨平台版本的多进程模块。
multiprocessing模块提供了一个Process类来代表一个进程对象
join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
'''

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


# if __name__ == '__main__':
print()
p = Process(target=run_proc, args=('test', ))
print('Child process will start.')
p.start()
p.join()
print('Child process end.')



def long_time_task(name):
    print('Run task %s  (%s) ...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

# 对Pool对象调用join()方法会等待所有子进程执行完毕，
# 调用join()之前必须先调用close()，
# 调用close()之后就不能继续添加新的Process了。
# task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行，
# 这是因为Pool的默认大小在我的电脑上是4，因此，最多同时执行4个进程
# if __name__ == '__main__':
print('Parent process %s.' % os.getpid())
p = Pool(4)
for i in range(5):
    p.apply_async(long_time_task, args=(i, ))
print('Waiting for all subprocesses done...')
p.close()
p.join()
print('All subprocesses done.')


# subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出
website = ['www.baidu.com', 'www.python.org']
print('$ nslookup %s'% website[0])
back_msg = subprocess.call(['nslookup', website[0]])
print('Exit code: ', back_msg)
# 如果子进程还需要输入，则可以通过communicate()方法输入
print('% nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out_put, error = p.communicate(b' set q = mx\npython.org\nexit\n')
print(out_put.decode('utf-8'))
print('Exit code: ', p.returncode)


'''
操作系统提供了很多机制来实现进程间的通信。
Python的multiprocessing模块包装了底层的机制，
提供了Queue、Pipes等多种方式来交换数据
'''

def write(q):
    print('Process to write: %s ' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue... ' % value)
        q.put(value)
        time.sleep(random.random())


def read(q):
    print('Process to read: %s ' % os.getpid())
    while True:
        value = q.get(True)
        print('Get  %s from queue. ' % value)


queue_one = Queue()
process_write = Process(target=write, args=(queue_one, ))
process_read = Process(target=read, args=(queue_one, ))
process_write.start()
process_read.start()
process_write.join()
process_read.terminate()















