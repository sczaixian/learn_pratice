
import os
import re
import threading
import asyncio
import time
import queue


data_sort = [9, 9, 1, 22, 31, 45, 3, 6, 2, 11]


'''
buble_sort
它重复地走访过要排序的元素列，依次比较两个相邻的元素，如果顺序错误就把他们交换过来
'''
def buble_sort(data):
    flag = True
    while flag:
        print(data)
        flag = False
        for j in range(1, len(data)):
            if data[j-1] > data[j]:
                flag = True
                data[j-1], data[j] = data[j], data[j-1]


# buble_sort(data_sort[:])

'''
selection_sort
第一次从待排序的数据元素中选出最小的一个元素，存放在序列的起始位置
'''
def selection_sort(data):
    for i in range(len(data) - 1):
        min_index = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_index]:
                min_index = j

        if min_index != i:
            data[i], data[min_index] = data[min_index], data[i]

        print(data)

# selection_sort(data_sort[:])

'''
inner_sort
将一个记录插入到已经排好序的有序表中，从而一个新的、记录数增1的有序表
'''
def inner_sort(data):
    for i in range(1, len(data)):
        for j in range(i):
            if data[i] < data[j]:
                data[i], data[j] = data[j], data[i]
        print(data)

# inner_sort(data_sort[:])
'''
quick_sort
通过一趟排序将要排序的数据分割成独立的两部分，
其中一部分的所有数据都比另外一部分的所有数据都要小，
然后再按此方法对这两部分数据分别进行快速排序
'''
def quick_sort(data):
    if data:
        mark = data[0]
        little = [i for i in data if i < mark]
        big = [i for i in data if i > mark]
        middle = [i for i in data if i == mark]
        return quick_sort(little) + middle + quick_sort(big)
    else:
        return []   # !

# print(quick_sort(data_sort[:]))

'''
binary_serach  --normal
'''
data_serach = [1, 2, 3, 6, 9, 9, 11, 22, 31, 45]
def binary_serach_normal(data, item):
    left, right = 0, len(data) - 1
    if item > data[right] or item < data[left]:
        return None
    while left<=right:
        middle = (left + right) // 2
        # print('left: %d,  right: %d,  mid: %d,  data[mid]: %d,  item: %d' % (left, right, middle, data[middle], item))
        if data[middle] == item:
            return middle
        elif data[middle] < item:
            left = middle + 1
        else:
            right = middle - 1
print(data_serach)
print(binary_serach_normal(data_serach, 100))
print(binary_serach_normal(data_serach, 33))
print(binary_serach_normal(data_serach, 11))
'''
binary_serach  --recursion
'''
def binary_serach_recursion(data, item, left, right):
    middle = (left + right) // 2
    if data[-1] < item or data[0] > item or middle == 0:
        return None
    elif data[middle] == item:
        return middle
    elif data[middle] < item:
        left = middle + 1
    else:
        right = middle - 1
    return binary_serach_recursion(data,item, left, right)

print(binary_serach_recursion(data_serach, 100, 0, len(data_serach)-1))
print(binary_serach_recursion(data_serach, 11, 0, len(data_serach)-1))
print(binary_serach_recursion(data_serach, 9, 0, len(data_serach)-1))

'''
triangles  --normal
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
'''
def triangles_normal(n):
    tr_list = [1]
    for _ in range(n):
        tr_list.append(0)
        tr_list = [tr_list[i] + tr_list[i-1] for i in range(len(tr_list))]
        yield tr_list[:]

# for i in triangles_normal(5):
#     print(i)
'''
triangles  --zip
'''
def triangles_zip(n):
    tr_list = [1]
    for _ in range(n):
        tr_list = [sum(i) for i in zip([0]+tr_list, tr_list+[0])]
        print(tr_list)
# triangles_zip(5)
'''
triangles  --map
'''
def triangles_map(n):
    tr_list = [1]
    for _ in range(n):
        tr_list = list(map(lambda x, y: x + y, [0]+tr_list, tr_list+[0]))
        print(tr_list)
# triangles_map(5)
'''
fib  --recursion
0, 1, 2, 3, 5, 8....
'''
def fib_recursion(n):
    if n <= 1:
        return n
    else:
        return fib_recursion(n - 1) + fib_recursion(n - 2)

# for i in range(10):
#     print(fib_recursion(i), end=', ')

'''
fib --magic
'''
class Fib(object):
    def __init__(self, n):
        self.n = n
        self.a = 0
        self.b = 1
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            self.a, self.b = self.b, self.a+self.b
            return self.a
        else:
            return 'StopIteration'
fb_1 = Fib(10)
for i in range(10):
    print(next(fb_1), end=' ')

''' 
fib --generator
'''
def fib_generator(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
        yield a
# for i in fib_generator(10):
#     print(i, end=', ')
'''
singleton  --modules
'''
# class Singleton:
#     def foo(self):
#         pass
# single = Singleton()
'''
singleton  --class  --threading
'''
class SingletonThreading():
    _instance_lock = threading.Lock()

    def __init__(self, *args, **kwargs):
        time.sleep(1)

    @classmethod
    def get_single(cls, *args, **kwargs):
        if not hasattr(SingletonThreading, '_instance'):
            with SingletonThreading._instance_lock:
                SingletonThreading._instance = SingletonThreading(*args, **kwargs)

        return SingletonThreading._instance
# for i in range(10):
#     s = SingletonThreading.get_single()
#     print(id(s))
print('----------------------------------')
# def task():
#     s = SingletonThreading.get_single()
#     print(id(s))

# t1 = threading.Thread(target=task(), name=1)
# t2 = threading.Thread(target=task(), name=2)
# t3= threading.Thread(target=task(), name=3)
# t1.start()
# t2.start()
# t3.start()


'''
singleton  --decorator
'''


def singleton_decorate(cls):
    _instance = {}

    def _single(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
            return _instance[cls]
    return _single


@singleton_decorate
class A:
    pass


# for i in range(10):
#     a = A()
#     print(id(a))

'''
singleton  --__new__
'''
class SingletonNew(object):
    _instance_lock = threading.Lock()

    def __init__(self, *args, **kwargs):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            with cls._instance_lock:
                cls._instance = super().__new__(cls)
        return cls._instance

'''
singleton  --attr
'''
def singleton_attr(fun):
    def __single():
        return hasattr(fun, '_instance') and getattr(fun, '_instance') or \
                setattr(fun, '_instance', fun()) or getattr(fun, '_instance')
    return __single

@singleton_attr
class B:
    pass

def test_attr():
    b = B()
    print(id(b))

# t1 = threading.Thread(target=test_attr(), name=1)
# t2 = threading.Thread(target=test_attr(), name=2)
# t3= threading.Thread(target=test_attr(), name=3)
# t1.start()
# t2.start()
# t3.start()

'''
link
'''
class Node:
    def __init__(self, item):
        self.next = None
        self.item = item

class LinkList:
    def __init__(self):
        self._head = None

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, node):
        self._head = node

    def length(self):
        current = self._head
        count = 0
        while current is not None:
            current = current.next
            count += 1
        return count

    def items(self):
        current = self._head
        while current is not None:
            yield current.item
            current = current.next

    def add(self, item):
        node = Node(item)
        node.next = self._head
        self._head = node

    def append(self, item):
        pass

    def insert_into(self, item, index):
        pass

    def remove(self, item):
        current = self._head
        pre = None
        pass
'''
about thread  asyncio queue
'''
async def sub(a, b):
    print('-----sub-------')
    print('---start: %d + %d = %d' % (a, b, a+b))
    await asyncio.sleep(5)
    return a + b


loop = asyncio.get_event_loop()
task = asyncio.gather(
    sub(3, 4),
    sub(1, 7)
)
loop.run_until_complete(task)
c, d = task.result()
result = c * d
print('result: (a + b) * (c + d) = %d' % result)
loop.close()
'''
zip, filter, map, reduce, sort,
list, tuple, dict, set, string
'''

'''
sql
'''

'''
gc
'''

'''
coroutine
'''