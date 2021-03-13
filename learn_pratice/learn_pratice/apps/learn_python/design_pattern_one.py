# coding=utf-8
import json
import copy
import xml.etree.ElementTree as etree
from threading import Lock
from abc import ABCMeta, abstractmethod
from collections import OrderedDict

'''
创建型模式
    单例模式
    工厂模式
    建造者模式
    原型模式
'''

'''
singleton
某一个类只有一个实例存在
'''

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


# test_singleton = Singleton()
# test_singleton2 = Singleton()
# print(test_singleton, test_singleton2)


'''
Factory
'''
print('----------------------------factory-------------------')


class JSONConnector:

    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode='r', encoding='utf-8') as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data


class XMLConnector:

    def __init__(self, filepath):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree


def connection_factory(filepath):
    if filepath.endswith('json'):
        connector = JSONConnector
    elif filepath.endswith('xml'):
        connector = XMLConnector
    else:
        raise ValueError('Cannot connect to {}'.format(filepath))
    return connector(filepath)


def connect_to(filepath):
    factory = None
    try:
        factory = connection_factory(filepath)
    except ValueError as ve:
        print(ve)
    return factory


def factory_main():
    sqlite_factory = connect_to('data/person.sq3')
    print()

    xml_factory = connect_to('data/person.xml')
    xml_data = xml_factory.parsed_data
    liars = xml_data.findall(".//{}[{}='{}']".format('person',
                                                     'lastName', 'Liar'))
    print('found: {} persons'.format(len(liars)))
    for liar in liars:
        print('first name: {}'.format(liar.find('firstName').text))
        print('last name: {}'.format(liar.find('lastName').text))
        [print('phone number ({})'.format(p.attrib['type']),
               p.text) for p in liar.find('phoneNumbers')]

    print()

    json_factory = connect_to('data/donut.json')
    json_data = json_factory.parsed_data
    print('found: {} donuts'.format(len(json_data)))
    for donut in json_data:
        print('name: {}'.format(donut['name']))
        print('price: ${}'.format(donut['ppu']))
        [print('topping: {} {}'.format(t['id'], t['type'])) for t in donut['topping']]


print('-----------------AbsFactory------------------------')


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


# test_factory()



'''
python扩展类方面，大体包括继承  组合 mixin三种。

继承：子类继承父类，子类具有父类的属性和方法。子类还是和父类是同种东西。比如人和孩子、成年人，孩子也是属于人。is  A

组合：人和手机，人可以有一个实例属性叫phone，phone的值则是一个Phone类的实例，
这样通过操作人这个对象的phone属性来操作手机浏览网页和打电话。

使用Mixin(mix-in)类实现多重继承要非常小心
    首先它必须表示某一种功能，而不是某个物品，如同Java中的Runnable，Callable等
    其次它必须责任单一，如果有多个功能，那就写多个Mixin类
    然后，它不依赖于子类的实现
    最后，子类即便没有继承这个Mixin类，也照样可以工作，就是缺少了某个功能。（比如飞机照样可以载客，就是不能飞了）
'''
class Vehicle(object):
    pass


class PlaneMixin(object):
    def fly(self):
        print('I am flying')


class Airplane(Vehicle, PlaneMixin):
    pass





'''
builder

将一个复杂对象的构建与它的表示分离，使得同样的构建过程可以创建不同的表示。
相关模式：思路和模板方法模式很像，模板方法是封装算法流程，
对某些细节，提供接口由子类修改，建造者模式更为高层一点，将所有细节都交由子类实现

一个例子更能很好的理解以上的内容：
1. 有一个接口类，定义创建对象的方法。一个指挥员类，接受创造者对象为参数。两个创造者类，创建对象方法相同，内部创建可自定义
2.一个指挥员，两个创造者(瘦子 胖子)，指挥员可以指定由哪个创造者来创造
'''

class Builder:
    __metaclass__ = ABCMeta

    @abstractmethod
    def draw_left_arm(self):
        pass


class Thin(Builder):
    def draw_left_arm(self):
        print('Thin....draw...')


class Fat(Builder):
    def draw_left_arm(self):
        print('Fat....draw...')


class Director():
    def __init__(self, person):
        self.person = person

    def draw(self):
        self.person.draw_left_arm()


'''
thin = Thin()
fat = Fat()
drector_draw_thin = Drector(thin)
drector_draw_fat = Drector(fat)
drector_draw_thin.draw()
dreator_draw_fat.draw()
'''





'''
prototype

原型模式本质就是克隆对象，所以在对象初始化操作比较复杂的情况下，很实用，能大大降低耗时，提高性能，
因为“不用重新初始化对象，而是动态地获得对象运行时的状态”。

浅拷贝（Shallow Copy）:指对象的字段被拷贝，而字段引用的对象不会被拷贝，拷贝的对象和源对象只是名称相同，但是他们共用一个实体。
深拷贝（deep copy）:对对象实例中字段引用的对象也进行拷贝。
'''

class Book:
    def __init__(self, name, price, **rest):
        '''rest的例子有：出版商、长度、标签、出版日期'''
        self.name = name
        self.price = price
        self.__dict__.update(rest)

    def __str__(self):
        mylist = []
        ordered = OrderedDict(sorted(self.__dict__.items()))
        for i in ordered:
            mylist.append('{}: {}'.format(i, ordered[i]))
            if i == 'price':
                mylist.append('$')
            mylist.append('\n')
        return ''.join(mylist)


class Prototype:
    def __init__(self):
        self.objects = dict()

    def register(self, identifier, obj):
        self.objects[identifier] = obj

    def unregister(self, identifier):
        del self.objects[identifier]

    def clone(self, identifiter, **attr):
        found = self.objects.get[identifiter]
        if not found:
            raise ValueError('Incorrect....identifier: {}'.format(identifiter))
        obj = copy.deepcopy(found)
        obj.__dict__.update(attr)
        return obj


def prototype_main():
    book = Book('name', price=100, publiction_data='2010-01-01', tags=('xx', 'zz', 'aa'))
    prototype = Prototype()
    cid = 'k&r-first'
    prototype.register(cid, book)
    print(book)
    print('ID book : {}'.format(id(book)))

# prototype_main()


'''

'''



























if __name__ == '__main--':
    pass