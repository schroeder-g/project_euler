import functools


# Generates the nth number in fib sequence.
@functools.lru_cache(maxsize=128)
def fibonacci(n):
    if n == 0 or n == 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))
