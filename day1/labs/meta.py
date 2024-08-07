# class MyMeta(type):
#     def __new__(cls, name, bases, dct):
#         print(f"Creating class {name}")
#         return super().__new__(cls, name, bases, dct)
#
# class MyClass(metaclass=MyMeta):
#     def doSomething(self):
#         print('I am an instance method')

# inst = MyClass()
# print(inst.doSomething())
#
# inst2 = MyClass()
# print(inst2.doSomething())

class MethodNameEnforcer(type):
    def __new__(cls, name, bases, dct):
        for attr_name in dct:
            if callable(dct[attr_name]) and not attr_name.startswith('method_'):
                raise ValueError(f"Method {attr_name} does not start with 'method_'")
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=MethodNameEnforcer):
    def method_valid(self):
        pass

    # Uncommenting the following method will raise an error
    def invalid_method(self):
        pass

