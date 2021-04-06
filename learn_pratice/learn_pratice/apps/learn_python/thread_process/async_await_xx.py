
import os
import asyncio
from threading import current_thread
from aiohttp import web

'''

async/await关键字是出现在python3.4以后。网上已经有很多文章对async/await这两个关键字都有讲解，
包括如何由python2的yield from发展到async/await这两个关键字，以及一些代码实现都有。
但是对于像我这样初次接触的人来说，光看代码分析也不一定能理解，我也是在度娘上搜索很多相关的网站，
当中也有官网，都没有发现能让我一眼看懂在什么地方可以用await，什么情况用await的文章。
经过自己的重新思考，总算对async、await有一些初步的了解，所以想把自己的理解记录下来，
希望对一些学习协程或者异步的初学者也有一定的帮助。

对于网上能搜到的一些代码实现、例子，这里就不重复了。

一、首先要知道什么是协程、异步。

举个例子：假设有1个洗衣房，里面有10台洗衣机，有一个洗衣工在负责这10台洗衣机。
那么洗衣房就相当于1个进程，洗衣工就相当1个线程。如果有10个洗衣工，
就相当于10个线程，1个进程是可以开多线程的。这就是多线程！

那么协程呢？先不急。大家都知道，洗衣机洗衣服是需要等待时间的，
如果10个洗衣工，1人负责1台洗衣机，这样效率肯定会提高，但是不觉得浪费资源吗？
明明1 个人能做的事，却要10个人来做。只是把衣服放进去，打开开关，就没事做了，
等衣服洗好再拿出来就可以了。就算很多人来洗衣服，1个人也足以应付了，开好第一台洗衣机，
在等待的时候去开第二台洗衣机，再开第三台，……直到有衣服洗好了，就回来把衣服取出来，
接着再取另一台的（哪台洗好先就取哪台，所以协程是无序的）。这就是计算机的协程！
洗衣机就是执行的方法。

当你程序中方法需要等待时间的话，就可以用协程，效率高，消耗资源少。

好了！现在来总结一下：

洗衣房 ==> 进程

洗衣工 ==> 线程

洗衣机 ==> 方法（函数）

二、async\await 的使用

正常的函数在执行时是不会中断的，所以你要写一个能够中断的函数，就需要添加async关键。

async 用来声明一个函数为异步函数，异步函数的特点是能在函数执行过程中挂起，
去执行其他异步函数，等到挂起条件（假设挂起条件是sleep(5)）消失后，也就是5秒到了再回来执行。

await 用来用来声明程序挂起，比如异步程序执行到某一步时需要等待的时间很长，
就将此挂起，去执行其他的异步程序。await 后面只能跟异步程序或有__await__属性的对象，
因为异步程序与一般程序不同。假设有两个异步函数async a，async b，a中的某一步有await，
当程序碰到关键字await b()后，异步程序挂起后去执行另一个异步b程序，就是从函数内部跳出去执行其他函数，
当挂起条件消失后，不管b是否执行完，要马上从b程序中跳出来，回到原程序执行原来的操作。
如果await后面跟的b函数不是异步函数，那么操作就只能等b执行完再返回，无法在b执行的过程中返回。
如果要在b执行完才返回，也就不需要用await关键字了，直接调用b函数就行。
所以这就需要await后面跟的是异步函数了。在一个异步函数中，可以不止一次挂起，也就是可以用多个await。

'''


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

# main(1, 2, 3 ,5)


async def test():
    print('start')
    await asyncio.sleep(1)
    print('end')

# loop = asyncio.get_event_loop()
# loop.run_until_complete(test())
# loop.close()


async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>')

async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'))

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
    print('Server started at http://127.0.0.1:8000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()