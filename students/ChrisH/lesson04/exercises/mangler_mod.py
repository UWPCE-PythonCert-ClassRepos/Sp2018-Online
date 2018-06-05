#!/usr/bin/env python3

"""
Simple metaclass example that creates name doubled versions of
all non-dunder class attributes
"""


class NameMangler(type):  # deriving from type makes it a metaclass.

    def __new__(cls, clsname, bases, _dict):
        new_class_attr = {}
        for name, val in _dict.items():
            if not name.startswith('__'):
                new_class_attr[name] = val
                new_class_attr[name * 2] = val
            else:
                new_class_attr[name] = val

        return super().__new__(cls, clsname, bases, new_class_attr)


class Foo(metaclass=NameMangler):
    x = 1
    Y = 2


# note that it works for methods, too!
class Bar(metaclass=NameMangler):
    x = 1

    def a_method(self):
        print("in a_method")


class MangledSingleton(NameMangler):
    instance = None

    def __call__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__call__(*args, **kwargs)
        return cls.instance


class MyClass(metaclass=MangledSingleton):
    x = 177777


if __name__ == "__main__":

    o1 = MyClass()
    o2 = MyClass()
    print(o1.x)
    print(o1.xx)
    assert id(o1) == id(o2)

    f = Foo()
    print(f.x)
    print(f.xx)
    print(f.Y)
    print(f.YY)

    b = Bar()
    b.a_methoda_method()
    # print(dir(b))
