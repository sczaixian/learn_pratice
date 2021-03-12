

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
















