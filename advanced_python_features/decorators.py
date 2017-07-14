# https://wiki.python.org/moin/PythonDecoratorLibrary
# Decorators dynamically alter the functionality of a function, method, or
# class without having to directly use subclasses or change the source code of
# the function being decorated.
# A Python decorator is a specific change to the Python syntax that allows us
# to more conveniently alter functions and methods.
print()
# In the following code, the cache() function is used as a decorator to
# remember the Fibonacci numbers that have already been computed.
def cache(function):
    cached_values = {} # contains already computed values
    def wrapping_function(*args):
        if args not in cached_values:
            # Call the function only if we haven't already done so with those
            # parameters
            cached_values[args] = function(*args)
        return cached_values[args]
    return wrapping_function

@cache
def fibonacci(n):
    print("Calling fibonacci(%d)" % n)
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print([fibonacci(n) for n in range(1, 9)])
print()

# The functools module provides a few decorators, such as lru_cache, which can
# do what we just did: memoization.
# It saves recent calls to save time when a given function is called with the
# same arguments.
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    print('calling fibonacci(%d)' % n)
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print([fibonacci(n) for n in range(1, 9)])
