from enum import Enum, unique
import sys
import os

'''
面向对象最重要的概念就是类（Class）和实例（Instance），
必须牢记类是抽象的模板，比如Student类，而实例是根据类创建出来的一个个具体的“对象”，
每个对象都拥有相同的方法，但各自的数据可能不同。

和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，
并且，调用时，不用传递该参数。
除此之外，类的方法和普通函数没有什么区别，
所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数

如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），
只有内部可以访问，外部不能访问
双下划线开头的实例变量不能直接访问__name
是因为Python解释器对外把__name变量改成了_Student__name，
所以，仍然可以通过_Student__name来访问__name变量
'''


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


# This is a method from calss A
Const_Test_B().method()



'''
多态的好处就是，当我们需要传入Dog、Cat、Tortoise……时，我们只需要接收Animal类型就可以了，
因为Dog、Cat、Tortoise……都是Animal类型，
然后，按照Animal类型进行操作即可。由于Animal类型有run()方法，
因此，传入的任意类型，只要是Animal类或者子类，就会自动调用实际类型的run()方法，
这就是多态的意思

对于一个变量，我们只需要知道它是Animal类型，
无需确切地知道它的子类型，就可以放心地调用run()方法，
而具体调用的run()方法是作用在Animal、Dog、Cat还是Tortoise对象上，
由运行时该对象的确切类型决定，这就是多态真正的威力：

调用方只管调用，不管细节，而当我们新增一种Animal的子类时，
只要确保run()方法编写正确，不用管原来的代码是如何调用的。这就是著名的“开闭”原则：
对扩展开放：允许新增Animal子类；
对修改封闭：不需要修改依赖Animal类型的run_twice()等函数


对于静态语言（例如Java）来说，
如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
对于Python这样的动态语言来说，则不一定需要传入Animal类型。
我们只需要保证传入的对象有一个run()方法就可以了：

这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，
一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。

Python的“file-like object“就是一种鸭子类型。对真正的文件对象，
它有一个read()方法，返回其内容。
但是，许多对象，只要有read()方法，都被视为“file-like object“。
许多函数接收的参数就是“file-like object“，
你不一定要传入真正的文件对象，完全可以传入任何实现了read()方法的对象。

为了达到限制的目的，Python允许在定义class的时候，
定义一个特殊的__slots__变量，来限制该class实例能添加的属性
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
'''

class Student(object):

    @property
    def name(self):
        return self._name


    @name.setter
    def name(self, name):
        self._name = name


student1 = Student()
student1.name = 'Jack'
print(student1.name)
student1.name = 'Mack'
print(student1.name)


'''
如果一个类想被用于for ... in循环，类似list或tuple那样，
就必须实现一个__iter__()方法，
该方法返回一个迭代对象，
然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，
直到遇到StopIteration错误时退出循环。
'''
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

    def __getitem__(self, item):
        a, b = 1, 1
        for x in range(item):
            a, b = b, a + b
        return a


for i in Fib():
    sys.stdout.write(str(i) + ' ')
print()
# print(Fib()[5])
get_item_fb = Fib()
print(get_item_fb[5])

t_list = list(range(20)[3:15])
print(t_list)



class Chain(object):
    def __init__(self, path=''):
       self.__path = path

    def __getattr__(self, path):
        return Chain('%s/%s' %(self.__path, path))

    def __call__(self, path):
        return Chain('%s/%s' %(self.__path, path))

    def __str__(self):
        return self.__path

    __repr__ = __str__

print(Chain().users('michael').repos) # /users/michael/repos




@unique
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, Gender):
        self.name = name
        self.gender = Gender


'''
要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可
with open('path', encoding='gbk', 'r/w/rb') as f:
t	文本模式 (默认)。
x	写模式，新建一个文件，如果该文件已存在则会报错。
b	二进制模式。
+	打开一个文件进行更新(可读可写)。
U	通用换行模式（Python 3 不支持）。
r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。
r+	打开一个文件用于读写。文件指针将会放在文件的开头。
rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。一般用于非文本文件如图片等。
w	打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
w+	打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
'''






'''
要获取某个环境变量的值，可以调用os.environ.get('key')
# 查看当前目录的绝对路径:
>>> os.path.abspath('.')
'/Users/michael'
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
>>> os.path.join('/Users/michael', 'testdir')
'/Users/michael/testdir'
# 然后创建一个目录:
>>> os.mkdir('/Users/michael/testdir')
# 删掉一个目录:
>>> os.rmdir('/Users/michael/testdir')
 对文件重命名:
>>> os.rename('test.txt', 'test.py')
# 删掉文件:
>>> os.remove('test.py')
'''

# 列出当前目录下的所有目录
print([x for x in os.listdir('..') if os.path.isdir(x)])
# 列出所有的.json文件
print([x for x in os.listdir('/home/python') if os.path.splitext(x)[1] == '.json'])



'''
import pickle, json
pickle.dumps()方法把任意对象序列化成一个bytes，
然后，就可以把这个bytes写入文件。
或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object
然后用pickle.loads()方法反序列化出对象，
也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象
>>> import pickle
>>> d = dict(name='Bob', age=20, score=88)
>>> pickle.dumps(d)
>>> f = open('dump.txt', 'wb')
>>> pickle.dump(d, f)
>>> f.close()
>>> f = open('dump.txt', 'rb')
>>> d = pickle.load(f)
>>> f.close()
>>> d
{'age': 20, 'score': 88, 'name': 'Bob'}

>>> import json
>>> d = dict(name='Bob', age=20, score=88)
>>> json.dumps(d)
'{"age": 20, "score": 88, "name": "Bob"}'

>>> json_str = '{"age": 20, "score": 88, "name": "Bob"}'
>>> json.loads(json_str)
{'age': 20, 'score': 88, 'name': 'Bob'}

Python的dict对象可以直接序列化为JSON的{}
def strdent2dict(std):
    return {
        'name':std.name,
        ....
    }
json.dumps(s, default=student2dict)
通常class的实例都有一个__dict__属性，它就是一个dict，
用来存储实例变量。也有少数例外，比如定义了__slots__的class
json.dumps(s, default=lambda obj: obj.__dict__)

def dict2student(d):
    return Student(d['name']....)
json.loads(json_str, object_hook=dict2student)
'''




























