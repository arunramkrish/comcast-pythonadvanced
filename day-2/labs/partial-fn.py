from functools import partial

def multiply(x, y, z):
    return x * y * z

double = partial(multiply, 2)
print(double(5, 10))  # Output: 10

from functools import lru_cache

@lru_cache(maxsize=9)
def fibonacci(n):
    if n < 2:
        return n
    print("inside fn")
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))  # Output: 55


