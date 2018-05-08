import json_save.json_save.json_save_dec as js


@js.json_save
class MyClass:

    x = js.Int()
    y = js.Float()
    lst = js.List()

    def __init__(self, x, lst):
        self.x = x
        self.lst = lst

# create one:
print("about to create a instance")
mc = MyClass(5, [3, 5, 7, 9])

print(mc)
print(mc.x)
print(mc.lst)

