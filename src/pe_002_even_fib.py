from functools import lru_cache
import sys


sys.setrecursionlimit(10000)
cache = {0: 0, 1: 1, 2: 1}


@lru_cache()
def gen_fib(n):
    if n in cache.keys():
        return cache[n]
    else:
        num = gen_fib(n - 1) + gen_fib(n - 2)
        if num > 4000000:
            pass
        cache[n] = num
        return cache[n]


print(sum(filter(lambda i: i % 2 == 0 and i < 4000000, cache.values())))
