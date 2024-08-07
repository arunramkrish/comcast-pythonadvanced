# def logging_decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling function: {func.__name__}")
#         result = func(*args, **kwargs)
#         print(f"Function {func.__name__} returned {result}")
#         return result
#
#     return wrapper
#
#
# @logging_decorator
# def mul(a, b):
#     return a * b
#
# @logging_decorator
# def div(a, b):
#     return a / b
#
# print(mul(5, 3))
# print(div(5, 3))

# def logging_decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling function: {func.__name__}")
#         result = func(*args, **kwargs)
#         print(f"Function {func.__name__} returned {result}")
#         return result
#
#     return wrapper
#
#
# @logging_decorator
# def add(a, b):
#     return a + b
#
#
# @logging_decorator
# def subtract(a, b):
#     return a - b
#
#
# @logging_decorator
# def multiply(a, b):
#     return a * b
#
#
# @logging_decorator
# def divide(a, b):
#     if b == 0:
#         raise Exception("Error: Division by zero")
#     return a / b
#
#
# # Example usage
# print(add(5, 3))
# print(subtract(10, 4))
# print(multiply(2, 3))
# print(divide(8, 2))
# print(divide(8, 0))

def requires_authentication(func):
    def wrapper(user, *args, **kwargs):
        if not user.is_authenticated:
            raise PermissionError(f" User is not authenticated. {user.name}")
        return func(user, *args, **kwargs)
    return wrapper

class User:
    def __init__(self, name, authenticated):
        self.name = name
        self.is_authenticated = authenticated

@requires_authentication
def view_dashboard(user):
    return f"Welcome to the dashboard, {user.name}!"

user = User("Alice", True)
print(view_dashboard(user))  # Output: Welcome to the dashboard, Alice!

unauthenticated_user = User("Bob", False)
print(view_dashboard(unauthenticated_user))  # Raises PermissionError
