# A generator is an object that can be used to iterate over a large number of
# values without storing all of those values in memory.
# A generator object can be used as an iterator, however, you can iterate over
# the values only once.
# A generator object can be created using a function that uses the yield
# keyword to generate a value.
# The generator object is created when the generator function is called.
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, (a + b)

print()
# Print all of the numbers in the Fibonacci sequence that are less than 1000:
for i in fibonacci_generator():
    if i > 1000:
        break
    print(i)

print()

# A generator expression is similar to a list comprehension, except that the
# values are computed on the fly instead of being computed once and stored in
# memory:
a = (x * x for x in range(100))
# a is a generator object
print(a)
print(type(a))
print(sum(a))
# Now no elements remain in the generator:
print(sum(a))
print()
