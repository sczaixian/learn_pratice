




def godme(fun):
    def __godme(*args, **kwargs):
        print('there are no function')

    return __godme


@godme
def test():
    print('test')


# test()  # there are no function



'''

'''


def godme(fun):
    def __godme(self, message):
        print('before')
        fun(self, message)
        print('after')

    return __godme


class Person:
    def show(self, message):
        print(message)

    @godme
    def say(self, message):
        print(message)


# person = Person()
# person.say('happy')
'''
before
happy
after
'''


def godme(fun):
    def __godme(cls, *args, **kwargs):
        print('before')
        fun(cls, *args, **kwargs)
        print('after')

    return __godme


@godme
class Person:
    def __new__(cls, *args, **kwargs):
        print('__new__')


# Person(Person)





import time
import functools

class DelayFunc:
    def __init__(self,  duration, func):
        self.duration = duration
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f'Wait for {self.duration} seconds...')
        time.sleep(self.duration)
        return self.func(*args, **kwargs)

    def eager_call(self, *args, **kwargs):
        print('Call without delay')
        return self.func(*args, **kwargs)

def delay(duration):
    """
    装饰器：推迟某个函数的执行。
    同时提供 .eager_call 方法立即执行
    """
    # 此处为了避免定义额外函数，
    # 直接使用 functools.partial 帮助构造 DelayFunc 实例
    return functools.partial(DelayFunc, duration)

@delay(duration=2)
def add(a, b):
    return a+b

print(add(3, 5))



def xx(fun):
    print('------xx-----')
    def wp(*args, **kwargs):
        print('-----wp-----')
        # 如果这里不返回fun则aa()中的内容不会执行
        fun(*args, **kwargs)
        # return fun(*args, **kwargs)
    return wp
@xx
def aa():
    print('-----aa------')
aa()