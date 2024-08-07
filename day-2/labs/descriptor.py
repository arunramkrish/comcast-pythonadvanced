class Descriptor:
    def __init__(self, name=None):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

class ReadOnlyDescriptor:
    def __init__(self, name=None):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

class MyClass:
    attr = Descriptor('attr')
    name = ReadOnlyDescriptor('name')

    def __init__(self, attr, name):
        self.attr = attr
        self.name = name

obj = MyClass('descriptor attr', "arun")
print(obj.attr + " " + obj.name)
obj.name = "Ram"
print(obj.attr + " " + obj.name)

