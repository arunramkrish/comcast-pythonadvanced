def greet_decorator(func):
    def wrapper():
        return f"Greetings! {func()}"
    return wrapper

def greet_decorator2(func):
    def wrapper():
        return f"Hi! {func()}"
    return wrapper

@greet_decorator2
@greet_decorator
def say_hello():
    return "Hello!"

print(say_hello())  # Output: Greetings! Hello!
