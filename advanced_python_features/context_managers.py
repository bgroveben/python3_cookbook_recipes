# https://docs.python.org/3/library/contextlib.html
# https://docs.python.org/3/library/stdtypes.html#typecontextmanager

# Context managers are mainly used to properly manage resources.
# The most common use of a context manager is the opening of a file:
# => with open('somefile', 'r') as f:
# Python's with statement supports the concept of a runtime context defined by
# a context manager, which is implemented by using the __enter__() and
# __exit__() methods.
from time import time

class Timer():
    def __init__(self, message):
        self.message = message

    def __enter__(self):
        self.start = time()
        return None # could return anything, an example use is:
                    # with Timer("Message") as value:

    def __exit__(self, type, value, traceback):
        elapsed_time = (time() - self.start) * 1000
        print(self.message.format(elapsed_time))

with Timer("Elapsed time to compute prime numbers ranging from 2 to 500: {}ms"):
    primes = []
    for x in range(2, 500):
        if not any(x % p == 0 for p in primes):
            primes.append(x)
        print("Primes: {}".format(primes))

# For simple use cases, it's possible to use a generator function with a single
# yield call, using the @contextmanager decorator:
from contextlib import contextmanager

@contextmanager
def colored_output(color):
    print("\033[%sm" % color, end="")
    yield
    print("\033[0m", end="")

print()
print("Hello World!")
with colored_output(31):
    print("Now in color!")
print("So cool.")
print()
