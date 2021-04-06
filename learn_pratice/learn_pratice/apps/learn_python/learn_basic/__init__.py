


'''

The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

'''


'''
PEP8

缩进
    每一级缩进使用4个空格。
    
    续行应该与其包裹元素对齐，要么使用圆括号、方括号和花括号内的隐式行连接来垂直对齐，
    要么使用挂行缩进对齐3。当使用挂行缩进时，应该考虑到第一行不应该有参数，
    以及使用缩进以区分自己是续行
        
        # 与左括号对齐
        
        foo = long_function_name(var_one, var_two,
        
                                var_three, var_four)
        
        # 用更多的缩进来与其他行区分
        
        def long_function_name(
        
                var_one, var_two, var_three,
        
                var_four):
        
            print(var_one)
        
        # 挂行缩进应该再换一行
        
        foo = long_function_name(
        
            var_one, var_two,
        
            var_three, var_four)
    
    不要在行尾加分号, 也不要用分号将两条命令放在同一行

行的最大长度   
    每行不超过80个字符（长的导入模块语句和注释里的URL除外）
    不要使用反斜杠连接行。Python会将圆括号, 中括号和花括号中的行隐式的连接起来 ：
    
    如果一个文本字符串在一行放不下, 可以使用圆括号来实现隐式行连接:
        x = ('这是一个非常长非常长非常长非常长 '
         '非常长非常长非常长非常长非常长非常长的字符串')

空行
    顶层函数和类的定义，前后用两个空行隔开。
    
    类里的方法定义用一个空行隔开。

Imports 导入
    导入通常在分开的行，例如：
        
        推荐:    import os
        
                import sys
        
        不推荐:  import sys, os
        
        也可以：
        
        from subprocess import Popen, PIPE

    导入总是位于文件的顶部，在模块注释和文档字符串之后，在模块的全局变量与常量之前
    
    导入应该按照以下顺序分组：
    
        标准库导入
        
        相关第三方库导入
        
        本地应用/库特定导入
    
        你应该在每一组导入之间加入空行。
    
    推荐使用绝对路径导入，如果导入系统没有正确的配置（比如包里的一个目录在sys.path里的路径后），
    使用绝对路径会更加可读并且性能更好（至少能提供更好的错误信息）

Comments 注释
    
    与代码相矛盾的注释比没有注释还糟，当代码更改时，优先更新对应的注释！
    
    注释应该是完整的句子。如果一个注释是一个短语或句子，它的第一个单词应该大写，除非它是以小写字母开头的标识符(永远不要改变标识符的大小写！)。

    如果注释很短，结尾的句号可以省略。块注释一般由完整句子的一个或多个段落组成，并且每句话结束有个句号。
    
    在句尾结束的时候应该使用两个空格。
    
    当用英文书写时，遵循Strunk and White （译注：《Strunk and White, The Elements of Style》）的书写风格。
    
    在非英语国家的Python程序员，请使用英文写注释，除非你120%的确信你的代码不会被使用其他语言的人阅读。
    

Documentation Strings 文档字符串
    要为所有的公共模块，函数，类以及方法编写文档说明。

    非公共的方法没有必要，但是应该有一个描述方法具体作用的注释。这个注释应该在def那一行之后
    
    多行文档说明使用的结尾三引号应该自成一行
        """Return a foobang
        
        Optional plotz says to frobnicate the bizbaz first.
        
        """
        
    对于单行的文档说明，尾部的三引号应该和文档在同一行

约定俗成的命名约定
    
    Names to Avoid 应避免的名字
        
        永远不要使用字母‘l’（小写的L），‘O’（大写的O），或者‘I’（大写的I）作为单字符变量名。

        在有些字体里，这些字符无法和数字0和1区分，如果想用‘l’，用‘L’代替。   
    
    Class Names 类名
    
        类名一般使用首字母大写的约定。

        在接口被文档化并且主要被用于调用的情况下，可以使用函数的命名风格代替。
        
        注意，对于内置的变量命名有一个单独的约定：大部分内置变量是单个单词（或者两个单词连接在一起），首字母大写的命名法只用于异常名或者内部的常量。

    Function Names 函数名
    
        函数名应该小写，如果想提高可读性可以用下划线分隔。
        
        大小写混合仅在为了兼容原来主要以大小写混合风格的情况下使用（比如 threading.py），保持向后兼容性。

    Function and method arguments 函数和方法参数
    
        始终要将 self 作为实例方法的的第一个参数。
        
        始终要将 cls 作为类静态方法的第一个参数。
        
        如果函数的参数名和已有的关键词冲突，在最后加单一下划线比缩写或随意拼写更好。
        因此 class_ 比 clss 更好。（也许最好用同义词来避免这种冲突）

    Programming Recommendations 编程建议
    
        代码应该用不损害其他Python实现的方式去编写（PyPy，Jython，IronPython，Cython，Psyco 等）。 
        比如，不要依赖于在CPython中高效的内置字符连接语句 a += b 或者 a = a + b。
        这种优化甚至在CPython中都是脆弱的（它只适用于某些类型）并且没有出现在不使用引用计数的实现中。
        在性能要求比较高的库中，可以种 ”.join() 代替。这可以确保字符关联在不同的实现中都可以以线性时间发生。
        
        和像None这样的单例对象进行比较的时候应该始终用 is 或者 is not，永远不要用等号运算符。
        
        另外，如果你在写 if x 的时候，请注意你是否表达的意思是 if x is not None。
        举个例子，当测试一个默认值为None的变量或者参数是否被设置为其他值的时候。
        这个其他值应该是在上下文中能成为bool类型false的值。
        
        使用 is not 运算符，而不是 not … is 。虽然这两种表达式在功能上完全相同，
        但前者更易于阅读，所以优先考虑。


'''


import this