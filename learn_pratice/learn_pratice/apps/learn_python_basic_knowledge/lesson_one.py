'''

    #endswith()  /   startswith()   /isspace()   /len()   /find()   /rfind()
    #index()   /count()   /replace()   /upper()   /lower()   /capitalize()
    #split()   /title()   /swapcase()   /strip()   /istrip()   /rstrip()
    #eval()   /ord()   /enter()   /ljust()   /rjust()
    #/format()

'''

print('Hello, %s'%'word')
print('1 + 2 = %d'%(3))

print('{}:{}'.format('a', 'b'))
print('{what}+{}={}'.format('2', '3', what='1'))
print('{0[2]}.{0[0]}.{0[1]}'.format(('baidu', 'com', 'www')))
print('{0:-^7}___{1:->7}_{2:*<7}'.format('123', 'abc', 2*4))
print('123456789'[5:1:-1])



import os, sys, random, keyword

print(keyword.kwlist)

total = 3 + 4 \
        + 5
print(total)

print("ni  hao  \n  lao  shi ")
print(r"ni hao  \n  lao  shi ")
print('______________________________________')

str = '0123456789101112'
print(str[0: -1])
print(str[0])
print(str[2:])
print(str[1:10])
print(str[1:10:2])
print(str * 2)
print(str + '  hello')
print('______________________________')




for i in sys.argv:
    print(i)

print('\n  python root ', sys.path)
# print(os.path())


testNumber = 1111
print(isinstance(testNumber, int))

print(8 // 3)

print(17 % 3)

print(2 ** 5)

print(0x1009)


def test_reversewords():
    str = "i love the world and i have mach money !"
    split_str = str.split(" ")
    revers_str = str[::-1]
    print(revers_str)
    print(split_str)
    output = ' '.join(revers_str)
    print(output)
    print(output[1:3])
test_reversewords()


testTuple = (1, 2, 3, 4, 5)
likeList = [1, 2, 3, 4, 5]
print(testTuple[1:3])
print(likeList[1:3])

# set可以进行集合运算
b = set('abracadabra')
a = set('alacazam')
print(a)
print(b)
print("----------------------------------------------------------")

print(a - b)  # a 和 b 的差集

print(a | b)  # a 和 b 的并集

print(a & b)  # a 和 b 的交集

print(a ^ b)  # a 和 b 中不同时存在的元素

print("----------------------------------------------------------")
outPutEval = eval("{'name':'linux','age':age}", {"age": 1822}, locals())
print(outPutEval)
age = 18
outPutEval = eval("{'name':'linux','age':age}", {"age": 1822}, locals())
print(outPutEval)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

reMatrix = [
    [row[i] for row in matrix] for i in range(4)
]

print(reMatrix)
print(list(zip(*matrix)))


print('-------------------------*args----------------------------------')


def test_args_fun(*args):
    print(args, type(args))
test_args_fun(1)
def test_args_fun2(x, y, *args):
    print(x, y, args)
test_args_fun2(1, 2, 3, 5)
def test_kwargs_fun(**kwargs):
    print(kwargs)
test_kwargs_fun()


print('-------------------------join----------------------------------')


def test_join_fun():
    seq_list = ['seq_list', 'abc', 'qwe', 'jfk']
    print(' '.join(seq_list))
    print(':'.join(seq_list))
    seq_str = 'seq_str hello good boy'
    print(':'.join(seq_str))
    seq_tuple = ('seq_tuple', 'hello', 'good', 'boy')
    print(':'.join(seq_tuple))
    seq_dict = {'seq_dict': 0, 'hello': 1, 'good': 2, 'boy': 3}
    print(':'.join(seq_dict))


test_join_fun()


def test_os_jion_fun():
    print(os.path.join('os_join', 'hello', 'good', 'boy'))


test_os_jion_fun()
print('-------------------------split----------------------------------')


def test_split_os_split_fun():
    str = 'www.good_boy.com'
    str_split_simple_out = str.split('.')
    print(str_split_simple_out, type(str_split_simple_out))
    str_split_out = str.split('.', random.randint(0, 2))
    #     str_split_out = str.split(':', -1)
    print(str_split_out)
    str_os_path = '/home/python/share/abc.txt'
    str_os_split_out = os.path.split(str_os_path)  # return path  and  fileName
    print(str_os_split_out, type(str_os_split_out))


test_split_os_split_fun()

print('-------------------------trip----------------------------------')


def test_trip_fun():
    test_str_space = ' sDFas  '
    print(test_str_space.lstrip())
    print(test_str_space.rstrip())
    print('%s, %s' % (test_str_space.lower(), test_str_space.upper()))


test_trip_fun()

print('-------------------------str_int_----------------------------------')


def test_str_fun():
    a = 3.1415926
    print('{:+2f}'.format(a))
    #     print('{:x<4d}'.format(a))
    print(''' sfad
        fsdfds
    ''')
    c = '杰尼龟' '暴打'"可达鸭"
    print(c)  # 结果为杰尼龟暴打可达鸭
    print('12345345 32'.isdigit())
    print('fdasfdsfds2fdsafds'.isalpha())
    print('fdssa'.isupper())  # islower
    # endswith()  /   startswith()   /isspace()   /len()   /find()   /rfind()
    # index()   /count()   /replace()   /upper()   /lower()   /capitalize()
    # split()   /title()   /swapcase()   /strip()   /istrip()   /rstrip()
    # eval()   /ord()   /enter()   /ljust()   /rjust()
    # /format()
    print('{}:{}'.format('a', 'b'))  # 位置索引
    print('{server}{0}:{1}'.format('a', 'b', server='c:'))  # 关键字映射
    print('{0[0]}.{0[1]}.{0[2]}'.format(('www', 'baidu', 'com')))  # 元素访问
    print('{0[0]}.{1[0]}.{1[1]}'.format(('www', 'sa'), ('baidu', 'com')))  # 元素访问
    print('{0:-^7}____{1:->7}_{2:*<7}'.format('123', 'abc', 2 * 4))  # 填充对齐
    print('123456789'[6:1:-1])
    # is -->id()  == --> value()

    # list
    # append()  <--> / extend()   /insert()   /以上操作均为原地修改，不产生新对象
    # list + list   /list *list   /
    ss_1 = [1, 2, 3, 6]  # 利用切片添加添加成段元素
    ss_1[2:2] = [4, 5]
    ss_1.sort(reverse=True)
    print(ss_1)
    # del   /clear()   /pop()   /remove()   /len()   /sum()   /max
    # min   /index()   /count()   /sort()   /sorted()   /random.shuffle()   /reersed()
    # copy()   /

    # tuple
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [7, 8, 9]
    d = zip(a, b, c)
    print(d)  # 结果为<zip object at 0x0000028C7CA43900>
    print(tuple(d))  # 结果为((1, 4, 7), (2, 5, 8), (3, 6, 9))
    print(list(d))  # 结果为[]


test_str_fun()
print('-------------------------pass----------------------------------')


def test_pass_fun():
    pass
    print('sdd22222')
    while True:
        pass
        print('ssssss')
        break


test_pass_fun()

print('-------------------------inner_outer/ closure----------------------------------')


def out_fun():
    out_str = 'outer'

    def inner_fun():
        print('inner_fun_out_put:  %s' % (out_str))
        print('wwww')

    return inner_fun()


out_fun()


def my_func(*args):
    fs = []
    for i in range(3):
        def func():
            return i * i

        fs.append(func)
    return fs


def test_my_func():
    fs1, fs2, fs3 = my_func()
    print(fs1())
    print(fs2())
    print(fs3())


test_my_func()


def people(peoplename):
    def print_age(peopleage):
        print(peoplename, peopleage)

    return print_age


def test_people_fun():
    peo = people('李白')
    peo('5岁')


test_people_fun()
print('-------------------------fromkeys----------------------------------')


def test_fromkeys_fun():
    print(dict.fromkeys(range(5)))
    print(dict.fromkeys(range(5), 'hello'))
    print(dict.fromkeys('name', ('1', 'b', 'c')))


test_fromkeys_fun()
print('-------------------------set----------------------------------')


def test_set_fun():
    print({'s', 'b', 'c'} == {'c', 'b', 's'})  # set
    print(('s', 'b', 'c') == ('s', 'b', 'c'))  # tuple
    a = 'fdssdfdsaasfsd'
    b = ''.join(x for x in a)
    print(set(a) == set(b))


test_set_fun()
print('-------------------------lambda----------------------------------')


def test_lambda_fun():
    out_list = (1, 2, 3)
    simp_fun = lambda x: (x < 5, 5)
    print(simp_fun(2))
    a = [('b', 3), ('a', 2), ('d', 4), ('c', 1)]
    print(sorted(a, key=lambda x: x[0]))


test_lambda_fun()

print('-------------------------fun_default_args----------------------------------')


def test_default_args_fun(value, list=[]):
    list.append(value)
    return list


print(test_default_args_fun('first'))
print(test_default_args_fun('second', []))
print(test_default_args_fun('third'))
print(test_default_args_fun('fourth'))
print(test_default_args_fun('fifth', []))

print('-------------------------yield_next_send----------------------------------')


def add(a, b):
    return a + b


def my_yidle_fun():
    for r_i in range(1, 4):
        yield r_i


def test_yield():
    g = my_yidle_fun()
    for n in [2, 10]:
        g = (add(n, i) for i in g)
        print(list(g), type(g))


test_yield()


def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b  # 使用 yield
        a, b = b, a + b
        n = n + 1


def test_fab_fun():
    fab_yield = fab(5)
    while True:
        try:
            x = next(fab_yield)
            print(x)
        except StopIteration as e:
            print('back : ', e.value)
            break


test_fab_fun()


def consumer(name):
    print('%s ready start!' % name)
    while True:
        lesson = yield
        print('come on num:%s! teacher: %s start to give lectures!' % (name, lesson))


def producer(lesson_count=1):
    c1 = consumer('Ruby')
    c2 = consumer('Python')
    #     c1.__next__()
    #     c2.__next__()
    next(c1)
    next(c2)
    print('---ready----!!')
    for i in range(lesson_count):
        c1.send(i)
        c2.send(i)


producer()
print('-----next------')
producer(3)

print('-------------------------list_lamdba_range_enumerate----------------------------------')
info = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a = [i + 1 for i in range(len(info))]
b = map(lambda x: x + 1, info)
for index, i in enumerate(info):
    info[index] += 1
print(a)
print(b)
print(info)

print('--------------------_ - __ - __xx__ -----私有化----------------------------------')


class Const_Test_A:
    def __method(self):
        print('This is a method from calss A')

    def _method(self):
        print('This is a private method from class A')

    def method(self):
        return self.__method()

    @classmethod
    def print_info_class_method(cls):
        print('')

    @staticmethod
    def print_info_static_method():
        print('')


class Const_Test_B(Const_Test_A):
    def __method(self):
        print('This is a method from calss B')


#     def method(self):
#         return self.__method()

Const_Test_B().method()














import time
def timer(fun):
    def warpper(*args, **kwargs):
        star = time.time()
        fun(*args, **kwargs)
        end = time.time()
        return end - star
    return warpper

@timer
def fun(a):
    return [x for x in range(a)]
print(fun(10000))
from functools import reduce
print(reduce(lambda x, y: x+y, [1,2,3,4,5]))


def ms():
    return [lambda x:i * x for i in range(4)]
print([m(2) for m in ms()])

def mss():
    return [lambda x, i=i:i * x for i in range(4)]
print([m(2) for m in mss()])

def msss():
    for i in range(4): yield lambda x: i * x
print([m(2) for m in mss()])

print((lambda x, y: x + y)(2, 4))

# 1-None.
print([[x for x in range(1, 51)][i:i+3] for i in range(0, 51, 3)])

print('-----------------xx---------------')

import math
print(math.ceil(5.3))



print((17 - 1) % 2 == 0)










