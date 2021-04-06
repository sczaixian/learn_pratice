
import os
import time
import asyncio
import threading
from threading import current_thread


def show1():
    for i in range(1, 52, 2):
        l2.acquire()
        print(i, end='')
        print(i+1, end=' ')
        time.sleep(0.1)
        l1.release()


def show2():
    for i in range(26):
        l1.acquire()
        print(chr(i + ord('A')))
        time.sleep(0.1)
        l2.release()


t1 = threading.Thread(target=show1, name='t1')
t2 = threading.Thread(target=show2, name='t2')

l1 = threading.Lock()
l2 = threading.Lock()

l1.acquire()

# t1.start()
# t2.start()


"""
使用协程的概念，达到以下目的， 输入a，b，c，d四个整数，打印(a+b)*(c+d)的值
# 定义负责计算两个数字的和的协程
"""
async def sum(a, b):
    print("【%s-%s】coroutine start to do: %s + %s" % (os.getpid(), current_thread().getName(), a, b))
    await asyncio.sleep(1) # 模拟耗时1秒的IO操作，自动切换协程
    r = int(a) + int(b)
    print("【%s-%s】coroutine end for : %s + %s,  result is %s" % (os.getpid(), current_thread().getName(), a, b, r))
    return r


# 定义主函数
def main(a, b, c, d):
    loop = asyncio.get_event_loop()
    task = asyncio.gather(
        sum(a, b),
        sum(c, d)
    )
    loop.run_until_complete(task)
    r1, r2 = task.result()
    r = r1 * r2
    print("【%s-%s】%s * %s = %s" % (os.getpid(), current_thread().getName(), r1, r2, r))
    loop.close()


# if __name__ == '__main__':
#     main(1, 2, 3, 4)


@asyncio.coroutine
def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1):
    r = yield from asyncio.sleep(1)
    print("Hello again!")

# # 获取EventLoop:
# loop = asyncio.get_event_loop()
# # 执行coroutine
# loop.run_until_complete(hello())
# loop.close()


async def test():
    await asyncio.sleep(1)
    print('----------')

test()
print('-----s-----------')


