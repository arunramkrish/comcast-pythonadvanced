class ReadOnlyDescriptor:
    def __init__(self, value):
        self._value = value

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        raise AttributeError("This attribute is read-only")

    def __delete__(self, instance):
        raise AttributeError("This attribute cannot be deleted")

class MyClass:
    read_only_attribute = ReadOnlyDescriptor(42)

# Example usage
obj = MyClass()
print(obj.read_only_attribute)  # Output: 42

# Attempting to set or delete the attribute raises an AttributeError
try:
    obj.read_only_attribute = 100
except AttributeError as e:
    print(e)  # Output: This attribute is read-only

try:
    del obj.read_only_attribute
except AttributeError as e:
    print(e)  # Output: This attribute cannot be deleted


# class ConfigurableReadOnlyDescriptor:
#     def __init__(self, initial_value=None):
#         self._value = initial_value
#
#     def __get__(self, instance, owner):
#         return self._value
#
#     def __set__(self, instance, value):
#         raise AttributeError("This attribute is read-only")
#
#     def __delete__(self, instance):
#         raise AttributeError("This attribute cannot be deleted")
#
# class MyClass:
#     read_only_attr1 = ConfigurableReadOnlyDescriptor(42)
#     read_only_attr2 = ConfigurableReadOnlyDescriptor("Hello, world!")
#
# # Example usage
# obj = MyClass()
# print(obj.read_only_attr1)  # Output: 42
# print(obj.read_only_attr2)  # Output: Hello, world!
