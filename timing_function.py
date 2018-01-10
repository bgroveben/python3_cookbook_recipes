# This timing function is cribbed from:
# https://realpython.com/blog/python/primer-on-python-decorators/.

import time

def timing_function(nested_function):
    """
    Outputs the time a function takes to execute.
    """

    def wrapper():
        t1 = time.time()
        nested_function()
        t2 = time.time()
        return "Time taken to run the function: " + str((t2-t1)) + "\n"

    return wrapper

@timing_function
def sum_numbers():
    num_list = []
    for num in (range(0, 10000)):
        num_list.append(num)
    print("\nSum of all numbers: " + str((sum(num_list))))

# sum_numbers() makes a good demonstration of what this file can do.
# Feel free to write a function that does just about anything that you
# want to set a timing benchmark for.

print(sum_numbers())
