from argparse import _MutuallyExclusiveGroup

cache = {}
def fibonacci(n):
    print(n)
    if n in cache:
        return cache[n]
    else:
        print("orere")
        if n < 2:
            return n   
        cache[n] = fibonacci(n-1) + fibonacci(n-2)
        return cache[n]


print(fibonacci(9))