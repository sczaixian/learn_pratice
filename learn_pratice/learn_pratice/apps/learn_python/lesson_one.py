import os
import sys
import math
import time
import random
import keyword
from functools import reduce, wraps
from collections.abc import Iterable, Iterator

print(keyword.kwlist)

total = 3 + 4 \
        + 5
print(total)

print("ni  hao  \n  lao  shi ")
print(r"ni hao  \n  lao  shi ")
'''
字符串相关

    #endswith()  /   startswith()   /isspace()   /len()   /find()   /rfind()
    #index()   /count()   /replace()   /upper()   /lower()   /capitalize()
    #split()   /title()   /swapcase()   /strip()   /istrip()   /rstrip()
    #eval()   /ord()   /enter()   /ljust()   /rjust()
    #/format()

'''

print('Hello, %s'%'word')
print('1 + 2 = %d'%(3))

print('\'{}:{}\'.format(\'a\', \'b\')  -> ', '{}:{}'.format('a', 'b'))
print('\'{what}+{}={}\'.format(\'2\', \'3\', what=\'1\') = ', '{what}+{}={}'.format('2', '3', what='1'))
print('\'{0[2]}.{0[0]}.{0[1]}\'.format((\'baidu\', \'com\', \'www\')) = ', '{0[2]}.{0[0]}.{0[1]}'.format(('baidu', 'com', 'www')))
print('\'{0:-^7}___{1:->7}_{2:*<7}\'.format(\'123\', \'abc\', 2*4) = ', '{0:-^7}___{1:->7}_{2:*<7}'.format('123', 'abc', 2*4))
'''
'{}:{}'.format('a', 'b')  ->  a:b
'{what}+{}={}'.format('2', '3', what='1') =  1+2=3
'{0[2]}.{0[0]}.{0[1]}'.format(('baidu', 'com', 'www')) =  www.baidu.com
'{0:-^7}___{1:->7}_{2:*<7}'.format('123', 'abc', 2*4) =  --123--___----abc_8******
'''
print('____________字符串切片__________________________')
test_str = '0123456789101112'
print('0123456789101112 - test_str[0:-1] --> ', test_str[0: -1])
print('0123456789101112 - test_str[0] --> ', test_str[0])
print('0123456789101112 - test_str[2:] --> ', test_str[2:])
print('0123456789101112 - test_str[1:10] --> ', test_str[1:10])
print('0123456789101112 - test_str[1:10:2] --> ', test_str[1:10:2])
print('0123456789101112 - test_str * 2 --> ', test_str * 2)
print('0123456789101112 - test_str + \'  hello\' --> ', test_str + '  hello')
print('123456789[5:1:-1] = ', '123456789'[5:1:-1])
'''
0123456789101112 - test_str[0:-1] -->  012345678910111
0123456789101112 - test_str[0] -->  0
0123456789101112 - test_str[2:] -->  23456789101112
0123456789101112 - test_str[1:10] -->  123456789
0123456789101112 - test_str[1:10:2] -->  13579
0123456789101112 - test_str * 2 -->  01234567891011120123456789101112
0123456789101112 - test_str + '  hello' -->  0123456789101112  hello
123456789[5:1:-1] =  6543
'''

for i in sys.argv:
    print('sys.argv = ', i)
print('python root ', sys.path)

print('_____//___%___**____0x_______________')
testNumber = 1111
print(isinstance(testNumber, int))
print('8 // 3 = ', 8 // 3)
print('17 % 3 = ', 17 % 3)
print('2 ** 5 = ', 2 ** 5)
print('0x1009 = ', 0x1009)
'''
True
8 // 3 =  2
17 % 3 =  2
2 ** 5 =  32
0x1009 =  4105
'''

def test_reversewords():
    str = "i love the world and i have mach money !"
    split_str = str.split(" ")
    revers_str = str[::-1]
    print(revers_str)
    print(split_str)
    output = ' '.join(revers_str)
    print(output)
    print(output[1:3])
'''
! yenom hcam evah i dna dlrow eht evol i
['i', 'love', 'the', 'world', 'and', 'i', 'have', 'mach', 'money', '!']
!   y e n o m   h c a m   e v a h   i   d n a   d l r o w   e h t   e v o l   i
'''
test_reversewords()


testTuple = (1, 2, 3, 4, 5)
likeList = [1, 2, 3, 4, 5]
print(testTuple[1:3])
print(likeList[1:3])

print("-----------------set可以进行集合运算---------------------")
b = set('abracadabra')
a = set('alacazam')
print('a = ', a)
print('b = ', b)

print('a - b = ', a - b)  # a 和 b 的差集
print('a | b = ', a | b)  # a 和 b 的并集
print('a & b = ', a & b)  # a 和 b 的交集
print('a ^ b = ', a ^ b)  # a 和 b 中不同时存在的元素
'''
a =  {'m', 'l', 'a', 'z', 'c'}
b =  {'d', 'a', 'r', 'b', 'c'}
a - b =  {'m', 'z', 'l'}
a | b =  {'m', 'd', 'l', 'a', 'r', 'b', 'z', 'c'}
a & b =  {'a', 'c'}
a ^ b =  {'m', 'd', 'l', 'b', 'z', 'r'}
'''
print("-----------------eval----------------------------------")
outPutEval = eval("{'name':'linux','age':age}", {"age": 1822}, locals())
print(outPutEval)
age = 18
outPutEval = eval("{'name':'linux','age':age}", {"age": 1822}, locals())
print(outPutEval)
'''
{'name': 'linux', 'age': 1822}
{'name': 'linux', 'age': 18}
'''
print('----------------矩阵转换-----------------------')
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print([[row[i] for row in matrix] for i in range(4)])
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
'''
(1,) <class 'tuple'>
1 2 (3, 5)
{}
'''

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

'''
seq_list abc qwe jfk
seq_list:abc:qwe:jfk
s:e:q:_:s:t:r: :h:e:l:l:o: :g:o:o:d: :b:o:y
seq_tuple:hello:good:boy
seq_dict:hello:good:boy
os_join/hello/good/boy
'''
test_join_fun()


def test_os_jion_fun():
    print(os.path.join('os_join', 'hello', 'good', 'boy'))

# os_join/hello/good/boy
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

'''
['www', 'good_boy', 'com'] <class 'list'>
['www', 'good_boy', 'com']
('/home/python/share', 'abc.txt') <class 'tuple'>
'''
test_split_os_split_fun()

print('-------------------------trip----------------------------------')


def test_trip_fun():
    test_str_space = ' sDFas  '
    print(test_str_space.lstrip())
    print(test_str_space.rstrip())
    print('%s, %s' % (test_str_space.lower(), test_str_space.upper()))

'''
sDFas  
 sDFas
 sdfas  ,  SDFAS  
'''
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

    # is -->id()  == --> value()

    # list
    # append()  <--> / extend()   /insert()   /以上操作均为原地修改，不产生新对象
    # list + list   /list *list   /
    ss_1 = [1, 2, 3, 6]  # 利用切片添加添加成段元素
    ss_1[2:2] = [4, 5]
    ss_1.sort(reverse=True)
    print(ss_1)   #[6, 5, 4, 3, 2, 1]
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

print('-------------------------inner_outer/ closure----------------------------------')


def my_func(*args):
    fs = []
    for i in range(3):
        def func():
            return i * i
        fs.append(func)
    return fs


def test_my_func():
    fs1, fs2, fs3 = my_func()
    print(fs1())    #  4
    print(fs2())    #  4
    print(fs3())    #  4

'''
返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量
'''
test_my_func()


def people(people_name):

    def print_age(people_age):
        print(people_name, people_age)
    return print_age


def test_people_fun():
    peo = people('李白')
    peo('5岁')


test_people_fun()   #李白 5岁
print('-------------------------fromkeys----------------------------------')


def test_fromkeys_fun():
    print(dict.fromkeys(range(5)))
    print(dict.fromkeys(range(5), 'hello'))
    print(dict.fromkeys('name', ('1', 'b', 'c')))

'''
{0: None, 1: None, 2: None, 3: None, 4: None}
{0: 'hello', 1: 'hello', 2: 'hello', 3: 'hello', 4: 'hello'}
{'n': ('1', 'b', 'c'), 'a': ('1', 'b', 'c'), 'm': ('1', 'b', 'c'), 'e': ('1', 'b', 'c')}
'''
test_fromkeys_fun()
print('-------------------------set----------------------------------')


def test_set_fun():
    print({'s', 'b', 'c'} == {'c', 'b', 's'})  # set
    print(('s', 'b', 'c') == ('s', 'b', 'c'))  # tuple
    a = 'fdssdfdsaasfsd'
    b = ''.join(x for x in a)
    print(set(a) == set(b))

# True
# True
# True
test_set_fun()
print('-------------------------lambda----------------------------------')


def test_lambda_fun():
    print((lambda x: (x < 5, 5))(2))
    a = [('b', 3), ('a', 2), ('d', 4), ('c', 1)]
    print(sorted(a, key=lambda x: x[0]))

# (True, 5)
# [('a', 2), ('b', 3), ('c', 1), ('d', 4)]
test_lambda_fun()

print('-------------------------fun_default_args----------------------------------')


def test_default_args_fun(value, list=[]):
    list.append(value)
    return list


print(test_default_args_fun('first'))           # ['first']
print(test_default_args_fun('second', []))      # ['second']
print(test_default_args_fun('third'))           # ['first', 'third']
print(test_default_args_fun('fourth'))          # ['first', 'third', 'fourth']
print(test_default_args_fun('fifth', []))       # ['fifth']


print('-------------------------yield_next_send----------------------------------')


def add(a, b):
    return a + b


def my_yidle_fun():
    for i in range(1, 4):
        yield i


def test_yield():
    g = my_yidle_fun()
    for n in [2, 10]:
        g = (add(n, i) for i in g)
        print(list(g), type(g))


#   [3, 4, 5] <class 'generator'>
#   [] <class 'generator'>
test_yield()
print('----------------ss--------------')

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

# 1  1  2  3  5
# back :  None
test_fab_fun()


def consumer(name):
    print('%s ready start!' % name)
    while True:
        lesson = yield
        print('come on num:%s! teacher: %s start to give lectures!' % (name, lesson))


def producer(lesson_count=1):
    c1 = consumer('Ruby')
    c2 = consumer('Python')
    next(c1)
    next(c2)
    print('---ready----!!')
    for i in range(lesson_count):
        c1.send(i)
        c2.send(i)

# Ruby ready start!
# Python ready start!
# ---ready----!!
# come on num:Ruby! teacher: 0 start to give lectures!
# come on num:Python! teacher: 0 start to give lectures!
# -----next------
# Ruby ready start!
# Python ready start!
# ---ready----!!
# come on num:Ruby! teacher: 0 start to give lectures!
# come on num:Python! teacher: 0 start to give lectures!
# come on num:Ruby! teacher: 1 start to give lectures!
# come on num:Python! teacher: 1 start to give lectures!
# come on num:Ruby! teacher: 2 start to give lectures!
# come on num:Python! teacher: 2 start to give lectures!
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
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# <map object at 0x7f2d4d94f898>
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


'''
*args   ---》  将参数打包成tuple  
例如     def xxx(a, b, *args):  print(a, b, args)    ，  
测试  xxx(1,2,3,4,5,6,7,8)  ------> 1   2    (3,4,5,6,7,8)
**kwargs   将传入打包成dict  '字典'  传入  
例如： def xxx(**kwargs): print(kwargs)      
测试  xxx(a=1)    xxx(a=1,b=2,c=3)
输出    {'a':1}     {'a':1, 'b':2, 'c':3}
args *args **kwargs   顺序必须一定的  不能颠倒顺序
'''


def timer(fun):
    @wraps(fun)
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


def ms():
    return [lambda x:i * x for i in range(4)]

# [6, 6, 6, 6]
print([m(2) for m in ms()])


def mss():
    return [lambda x, i=i:i * x for i in range(4)]

# [0, 2, 4, 6]
print([m(2) for m in mss()])


def msss():
    for i in range(4): yield lambda x: i * x

# [0, 2, 4, 6]
print([m(2) for m in mss()])

print((lambda x, y: x + y)(2, 4))       # 6

# 列表 1-50 三个一组
print([[x for x in range(1, 51)][i:i+3] for i in range(0, 51, 3)])
# [
# [1, 2, 3], [4, 5, 6], [7, 8, 9],
# [10, 11, 12], [13, 14, 15], [16, 17, 18],
# [19, 20, 21], [22, 23, 24], [25, 26, 27],
# [28, 29, 30], [31, 32, 33], [34, 35, 36],
# [37, 38, 39], [40, 41, 42], [43, 44, 45],
# [46, 47, 48], [49, 50]
# ]
print('-----------------xx---------------')


print(math.ceil(5.3))   # 6

print([d for d in os.listdir('.')])     # 当前目录下的文件


'''
generator
杨辉三角
'''
def test_generator():
    list = [x for x in range(10)]
    generator = (x for x in range(10))
    print(list)
    print(generator)
    print(next(generator))
    for x in generator:
        yield x
        print(x)

gen = test_generator()
next(gen)
next(gen)
next(test_generator())
print(gen)
for i in test_generator():
    print('-----', i)

def triangles():
    L=[1]
    while True:
        yield L[:]
        L.append(0)
        L = [ L[i]+ L[i-1] for i in range(len(L))]

def tr2(num=1):
    n, l1 = 0, [1]
    for _ in range(num):
        l1 = [sum(t) for t in zip([0]+l1, l1+[0])]
        print(l1)

def tr3(num=1):
    l1, n = [[1]], 1
    for _ in range(num):
        l1.append(list(map(lambda x, y: x+y, [0]+l1[-1], l1[-1]+[0])))
    for i in l1:
        print(i)

t = triangles()
for x in range(5):
    print(next(t))
print('---------------------------')
tr2(5)
print('---------------------------')
tr3(5)

'''
可以直接作用于for循环的数据类型有以下几种：
一类是集合数据类型，如list、tuple、dict、set、str等；
一类是generator，包括生成器和带yield的generator function。
这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
可以使用isinstance()判断一个对象是否是Iterable对象：
'''

print(isinstance([], Iterable))         # True

'''
生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，
直到最后抛出StopIteration错误表示无法继续返回下一个值了。
可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
可以使用isinstance()判断一个对象是否是Iterator对象：
'''
print(isinstance({}, Iterator))         # False
print(isinstance((a for a in range(3)), Iterator))      #True

'''
生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
把list、dict、str等Iterable变成Iterator可以使用iter()函数：
'''

isinstance(iter([]), Iterator)      #True

'''
Python的for循环本质上就是通过不断调用next()函数实现的，例如：
'''

for i in [1, 2, 3, 4]:
    pass
it = iter([1, 2, 3, 4])
while True:
    try:
        next(it)
    except StopIteration as e:
        break

'''
map()函数接收两个参数，一个是函数，一个是Iterable，
map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回

    l2 = map(lambda x, y: x ** y, [1, 2, 3], [1, 2, 3])   print(list(l2))   ----》 【1， 4， 27】
    l4 = map(lambda x, y: (x ** y, x + y), [1, 2, 3], [1, 2])           ------->((1, 2), (2, 4))
    l5 = map(lambda x, y: (x ** y, x + y), [1, 2, 3], [1, 2, 'a'])   ----->出错 有不一样的类型

特殊用法，做类型转换：
l=map(int,'1234')
for i in l:
    print(type(i))
    print(i)                -------> 返回数字  类型int
 
如果函数是 None，自动假定一个‘identity’函数,这时候就是模仿 zip()函数，
l=[1,2,3]
x=map(None,l)
print(x)
这时候 None 类型不是一个可以调用的对象。所以他没法返回值。
目的是将多个列表相同位置的元素归并到一个元组。如：

>>> print map(None, [2,4,6],[3,2,1])
[(2, 3), (4, 2), (6, 1)]
但是在 python3中，返回是一个迭代器，所以它其实是不可调用的

'''
title = ['adam', 'LISA', 'barT']
print(list(map(lambda x: x.title(), title)))

'''
reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
这个函数必须接收两个参数，
reduce把结果继续和序列的下一个元素做累积计算
'''

print(reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))    #15

'''
filter()函数用于过滤序列
filter()把传入的函数依次作用于每个元素，
然后根据返回值是True还是False决定保留还是丢弃该元素
'''

print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
filter_test_list = [11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]
print(list(filter(lambda x: str(x) == str(x)[::-1], filter_test_list)))


'''
Python内置的sorted()函数就可以对list进行排序
可以接收一个key函数来实现自定义的排序
'''
print(sorted([36, 5, -12, 9, -21], key=abs, reverse=True))

# print(list(map(lambda x: sorted(x[1]), [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)])))
print(sorted([('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)], key=(lambda x: x[1]), reverse=True))





































