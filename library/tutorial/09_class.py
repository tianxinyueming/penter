# 钻石继承（菱形继承）super
class A1:
    def print(self):
        print("A1")


class B1(A1):
    def print(self):
        print("B1 From A1")
        A1.print(self)


class C1(A1):
    def print(self):
        print("C1 From A1")
        A1.print(self)


class D1(B1, C1):
    def print(self):
        print("D1 From B1, C1")
        B1.print(self)
        C1.print(self)


d = D1()
d.print()
"""
输出：
D1 From B1, C1
B1 From A1
A1
C1 From A1
A1
"""


# 如果只要调用一次A1.print怎么办？使用super()
class A2:
    def print(self):
        print("A2")


class B2(A2):
    def print(self):
        print("B2 From A2")
        super(B2, self).print()
        # super().print()


class C2(A2):
    def print(self):
        print("C2 From A2")
        super(C2, self).print()


class D2(B2, C2):
    def print(self):
        print("D2 From B2, C2")
        super(D2, self).print()


d2 = D2()
d2.print()
"""
输出：
D2 From B2, C2
B2 From A2
C2 From A2
A2
注意：如果B2或者C2任意一个没有调用super是不会打印A2的
D2(B2, C2)：如果B2没有调用super，连“C2 From A2”都不会打印

"""


class ex_5:
    "My first example"

    class O: pass

    class F(O): pass

    class E(O): pass

    class D(O): pass

    class C(D, F): pass

    class B(D, E): pass

    class A(B, C): pass


# 抽象类
import abc


class Abs(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def abs_func1(self): pass

    @abc.abstractmethod
    def abs_func2(self): pass

    def func2(self): print("默认实现")


# 必须实现所有抽象方法
class Obj(Abs):
    def abs_func1(self):
        print("实现1")

    def abs_func2(self):
        print("实现2")


obj = Obj()
obj.abs_func1()
obj.func2()
print(issubclass(Obj, Abs))  # True
print(isinstance(obj, Abs))  # True


# 如果不想实现所有的抽象方法就要继承object
@Abs.register
class Obj2(object):
    def abs_func1(self):
        print("实现..")


obj2 = Obj2()
obj2.abs_func1()
# obj.abs_func2() 没得调用
# obj2.func2() 也没得调用

print(issubclass(Abs, Obj2))  # False
print(isinstance(obj2, Abs))  # True

print("------------------------")


# 作用域和命名空间示例
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)


# 请注意 局部 赋值（这是默认状态）不会改变 scope_test 对 spam 的绑定。 nonlocal 赋值会改变 scope_test 对 spam 的绑定，而 global 赋值会改变模块层级的绑定。
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'


x = MyClass()
print(x.f())
print(x.i)

setattr(x, "a", 1)
print(x.a)
x.b = 2
print(x.b)
del x.b


# 不能删除x.i


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = Complex(3.0, -4.5)
print(x.r, x.i)

"""
9.5.1. 多重继承
Python也支持一种多重继承。 带有多个基类的类定义语句如下所示:

class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
对于多数应用来说，在最简单的情况下，你可以认为搜索从父类所继承属性的操作是深度优先、从左至右的，当层次结构中存在重叠时不会在同一个类中搜索两次。 
因此，如果某一属性在 DerivedClassName 中未找到，则会到 Base1 中搜索它，然后（递归地）到 Base1 的基类中搜索，如果在那里未找到，再到 Base2 中搜索，依此类推。

真实情况比这个更复杂一些；方法解析顺序会动态改变以支持对 super() 的协同调用。 这种方式在某些其他多重继承型语言中被称为后续方法调用，它比单继承型语言中的 super 调用更强大。

动态改变顺序是有必要的，因为所有多重继承的情况都会显示出一个或更多的菱形关联（即至少有一个父类可通过多条路径被最底层类所访问）。 例如，所有类都是继承自 object，因此任何多重继承的情况都提供了一条以上的路径可以通向 object。 
为了确保基类不会被访问一次以上，动态算法会用一种特殊方式将搜索顺序线性化， 保留每个类所指定的从左至右的顺序，只调用每个父类一次，并且保持单调（即一个类可以被子类化而不影响其父类的优先顺序）。 
总而言之，这些特性使得设计具有多重继承的可靠且可扩展的类成为可能。 要了解更多细节，请参阅 https://www.python.org/download/releases/2.3/mro/。
"""


# 迭代器
class Reverse:
    """Iterator for looping over a sequence backwards."""

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


rev = Reverse('spam')
for char in rev:
    print(char)

"""
在幕后，for 语句会在容器对象上调用 iter()。 该函数返回一个定义了 __next__() 方法的迭代器对象，此方法将逐一访问容器中的元素。 
当元素用尽时，__next__() 将引发 StopIteration 异常来通知终止 for 循环。 你可以使用 next() 内置函数来调用 __next__() 方法；这个例子显示了它的运作方式:

如果类已定义了 __next__()，则 __iter__() 可以简单地返回 self:
"""


# 生成器
def reverse(data):
    for index in range(len(data) - 1, -1, -1):
        yield data[index]


# 自动创建 __iter__() 和 __next__() 方法。
for char in reverse('golf'):
    print(char)
