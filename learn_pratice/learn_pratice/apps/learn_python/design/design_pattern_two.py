# coding=utf-8
import time
from functools import wraps

'''
结构型模式
    适配器模式
    修饰器模式
    外观模式
    享元模式
    模型-视图-控制器模式
    代理模式
'''


'''
adaptee
适配器模式是指是一种接口适配技术，它可通过某个类来使用另一个接口与之不兼容的类，运用此模式，两个类的接口都无需改动。
适配器模式主要应用于希望复用一些现存的类，但是接口又与复用环境要求不一致的情况
'''

class Target(object):
    def request(self):
        pass


class Adaptee(object):
    def specific_request(self):
        pass


class Adapter(Adaptee):
    def __init__(self):
        self.adaptee = Adaptee()

    def request(self):
        self.adaptee.specific_request()


'''
Decorator
修饰器模式通常用于扩展一个对象的功能

装饰器函数 必须接受一个callable对象作为参数，
然后返回一个callable对象。
在Python中一般callable对象都是函数，但也有例外。
只要某个对象重载了__call__()方法，那么这个对象就是callable的。

@property、@staticmethod、@classmethod和@abstractmethod。
@staticmethod不需要表示自身对象的self和自身类的cls参数，就跟使用函数一样。
@classmethod也不需要self参数，但第一个参数需要是表示自身类的cls参数。
类方法有类变量cls传入，从而可以用cls做一些相关的处理。并且有子类继承时，调用该类方法时，传入的类变量cls是子类，而非父类。

Python的abc提供了@abstractmethod装饰器实现抽象方法，使用@abstractmethod装饰器类将不能被实例化。
'''
print('----------------------------decorator-------------------')
print('-----------第一种--原封不动返回被装饰函数-------------------')


def register(fun):
    print('---reg-')
    return fun


@register
def test():
    print('----tst-')

# test()

print('-----------第二种---把被装饰函数替换成新函数 闭包结构的函数------------------')


def running_time(fun):
    print('--running_time---')

    def print_run_tim(*args):
        start_time = time.time()
        fun(*args)
        end_time = time.time()
        print('-- {} --print_run_time--- {} -'.format(fun.__name__, end_time - start_time))
        return fun(*args)
    return print_run_tim


@running_time
def do_something(name):
    print('hello    {} !'.format(name))


print('--result {}-- -name   {}--'.format(do_something('Jack'), do_something.__name__))




# 带参数的类装饰器
class logging(object):
    def __init__(self, level='INFO'):
        self.level = level

    def __call__(self, func):  # 接受函数
        def wrapper(*args, **kwargs):
            print("[{level}]: enter function {func}()".format(level=self.level,func=func.__name__))
            func(*args, **kwargs)

        return wrapper  # 返回函数


@logging(level='INFO')
def say(something):
    print("say {}!".format(something))


'''
使用类装饰器能使代码更加简洁。
比方说有时你只想打印日志到一个文件。而有时你想把引起你注意的问题发送到一个email，
同时也保留日志，留个记录。这是一个使用继承的场景，我们可以用类来构建装饰器。
'''

class logit(object):
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile并写入
            try:
                with open(self.logfile, 'a') as opened_file:
                    # 现在将日志打到指定的文件
                    # opened_file.write(log_string + '\n')
                    pass
            except IOError as e:
                print(e)
            # 现在，发送一个通知
            self.notify()
            return func(*args, **kwargs)
        return wrapped_function

    def notify(self):
        # logit只打日志，不做别的
        pass

class email_logit(logit):
    '''
    一个logit的实现版本，可以在函数调用时发送email给管理员
    '''
    def __init__(self, email='admin@myproject.com', *args, **kwargs):
        self.email = email
        super(email_logit, self).__init__(*args, **kwargs)

    def notify(self):
        # 发送一封email到self.email
        # 这里就不做实现了
        print('send')

@email_logit()
def myfunc1():
    print("func1")

@logit()
def myfunc2():
    print("func2")

def test_func():
    myfunc1()
    print("-----------------------")
    myfunc2()


print('-----------使用functools.wraps装饰器把相关属性从func复制到新函数中------------------')


def new_running_time(fun):
    @wraps(fun)
    def print_run_time(*args):
        start_time = time.time()
        fun(*args)
        end_time = time.time()
        return end_time - start_time
    return print_run_time


@new_running_time
def do_something2(name):
    print('hello    {} !'.format(name))


print('--result- {}-----name  {}--'.format(do_something2('Mack'), do_something2.__name__))




'''
facade

在面向对象程序设计中，解耦是一种推崇的理念。但事实上由于某些系统中过于复杂，从而增加了客户端与子系统之间的耦合度
'''


print('Facade ....')



'''
享元模式
'''








































