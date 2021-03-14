'''
优美胜于丑陋；
明了胜于晦涩；
简单胜于复杂；
复杂胜于晦涩；
扁平胜于嵌套；
间隔胜于紧凑；
可读性很重要；
特例不足以特殊到违背这些原则；
实用性胜过纯粹；
永远不要默默地忽视错误；
除非明确需要这样做；
面对模棱两可，拒绝猜测；
解决问题最直接的方法应该有一种，最好只有一种；
当然这是没法一蹴而就的，除非你是荷兰人；
做也许好过不做；
但不想就做还不如不做；
如果方案难以描述明白，那么一定是个糟糕的方案；
如果实现容易描述，那可能是个好方案；
命名空间是一种绝妙的理念，多加利用！



模块命名尽量短小，使用全部小写的方式，可以使用下划线。
包命名尽量短小，使用全部小写的方式，不可以使用下划线。
类的命名使用CapWords的方式，模块内部使用的类采用_CapWords的方式。
异常命名使用CapWords+Error后缀的方式。
全局变量尽量只在模块内有效，类似C语言中的static。实现方法有两种，一是all机制;二是前缀一个下划线。
函数命名使用全部小写的方式，可以使用下划线。
常量命名使用全部大写的方式，可以使用下划线。
类的属性（方法和变量）命名使用全部小写的方式，可以使用下划线。
类的属性有3种作用域public、non-public和subclass API，
可以理解成C++中的public、private、protected，non-public属性前，前缀一条下划线。

类的属性若与关键字名字冲突，后缀一下划线，尽量不要使用缩略等其他方式。
为避免与子类属性命名冲突，在类的一些属性前，前缀两条下划线。
比如：类Foo中声明__a,访问时，只能通过Foo._Foo__a，避免歧义。如果子类也叫Foo，那就无能为力了。

类的方法第一个参数必须是self，而静态方法第一个参数必须是cls。


编码中考虑到其他python实现的效率等问题，比如运算符‘+’在CPython（Python）中效率很高，
都是Jython中却非常低，所以应该采用.join()的方式。

尽可能使用‘is’‘is not’取代‘==’，比如if x is not None 要优于if x
使用基于类的异常，每个模块或包都有自己的异常类，此异常类继承自Exception。
常中不要使用裸露的except，except后跟具体的exceptions。例如

'''

'''
a, b = b, a
推导式一行代码就可以实现 集合 字典
ls = [x*x for x in range(5) if x % 2 == 0]
num = [1, 2, 3, 4, 4, 4, 4, 2, 3, 4, 5, 6, 7, 8, 9]
print(max(set(num), key=num.count))
'''

'''
一般来说，避免使用以下名称：
太宽泛，如my_list；
太冗长，如list_of_machine_learning_data_set；
太模糊，如“1”、“I”、“o”、“O”。
包 / 模块名应该全部小写：
首选使用一个单词命名；
当需要使用多个单词时，使用下划线分割它们。
类名应遵循 UpperCaseCamelCase 规范
变量\方法\函数应该采用小写（如果需要，用下划线分割）
常量名必须全大写（如果需要，用下划线分割）
'''

# 化繁为简的能力就是消除不必要的东西，保留必要的东西。
words = ['Hannibal', 'Hanny', 'Steeve']
# 不成熟的方法
# index = 0
# for word in words:
# print(index, word)
# index += 1
# 推荐方法
# for index, word in enumerate(words):
# print(index, word)


subjects = ['math', 'chemistry', 'biology', 'pyhsics']
grades = ['100', '83', '90', '92']
grades_dict = dict(zip(subjects, grades))
print(grades_dict)

# 可读性很重要
money = 10000000
print("I earn", money, "dollars by writing on medium.")
money = 10_000_000
print(f"I earn {money} dollars by writing on medium.")


#永远不要默默地忽视错误
try:
    x = int(input("Please enter an Integer: "))
except ValueError:
    print("Oops! This is not an Integer.")
except Exception as err:
    print(err)
else:
    print('You did it! Great job!')
finally:
    print('ヽ(✿ﾟ▽ﾟ)ノ')
    # 1. 这段代码可能中断。
    # 2. 如果出现值错误就会触发。
    # 3. 处理值错误之外的错误。
    # 4. 如果没有触发错误就执行。
    # 5. 不管是否触发错误都执行。


# 面对模棱两可，拒绝猜测
import numpy as np

a = np.arange(5)
print(a < 3)
if a < 3:
    print('smaller than 3')

a = np.array([True, True, True])
b = np.array([False, True, True])
c = np.array([False, False, False])
print(a.all())
print(a.any())
print(b.all())
print(b.any())
print(c.all())
print(c.any())


















