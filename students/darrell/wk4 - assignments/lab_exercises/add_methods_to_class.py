def my_method(self):
    print("called my_method, x = %s" % self.x)

def __init__(self):
    self.y = 10

MyClass = type('MyClass',(), {'x': 1, 'my_method': my_method, '__init__':__init__})
o = MyClass()
o.my_method()