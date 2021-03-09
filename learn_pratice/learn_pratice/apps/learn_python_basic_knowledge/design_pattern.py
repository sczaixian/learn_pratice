'''
singleton
'''
from threading import Lock
from functools import wraps
import time

print('----------------------------singleton-------------------')
class Singleton:
    _instance_lock = Lock()
    _init_lock = Lock()

    def __new__(cls, *args, **kwargs):
        with Singleton._instance_lock:
            if not hasattr(Singleton, '_instance'):
                Singleton._instance = object.__new__(cls)
                print('----new---')
        return Singleton._instance

    def __init__(self):
        with Singleton._init_lock:
            if not hasattr(Singleton, '_first_init'):
                Singleton._first_init = True
                print('-----init-----')


test_singleton = Singleton()
test_singleton2 = Singleton()


'''

Decorator

'''
print('----------------------------decorator-------------------')
print('-----------第一种--原封不动返回被装饰函数-------------------')
def register(fun):
    print('---reg-')
    return fun
@register
def test():
    print('----tst-')
test()

print('-----------第二种---把被装饰函数替换成新函数 闭包结构的函数------------------')
def running_time(fun):
    print('--running_time---')
    def print_run_tim(*args):
        print('----print_run_time---{}-'.format(fun.__name__))
        start_time = time.time()
        fun(*args)
        end_time = time.time()
        return end_time - start_time
    return print_run_tim

@running_time
def do_something(name):
    print('hello    {} !'.format(name))

print('--result {}-- -name   {}--'.format(do_something('Jack'), do_something.__name__))


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
Factory
'''
print('----------------------------factory-------------------')
class Benz:
    def __repr__(self):
        return 'Benz...'

class AbsFactory:
    def produce_car(self):
        pass

class BenzFactory(AbsFactory):
    def produce_car(self):
        return Benz()

def test_factory():
    car = BenzFactory().produce_car()
    print(f'car ---  {car}')

test_factory()