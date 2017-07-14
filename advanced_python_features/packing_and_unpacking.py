# The * operator, known as the unpack or splat operator, allows very convenient
# transformations, going from lists or tuples to separate variables or
# arguments (and vice-versa):
a, *b, c = [2, 7, 5, 6, 3, 4, 1]
print()
print(a)
print(b)
print(c)
print()

# When the arguments for your function are already in a list or in a tuple, you
# can unpack them using *args.
# You can unpack arguments in a dict using **kwargs.
def repeat(count, name):
    for i in range(count):
        print(name)

print("Call repeat() function using a list of arguments:")
args = [4, "cats"]
repeat(*args)
print()

print("Call repeat function using a dictionary of keyword arguments:")
args2 = {'count': 4, 'name': 'cats'}
repeat(**args2)
print()

# You can also define a function that will pack all of the arguments into a
# single tuple and all of the keyword arguments into a single dict.
def pack_em_up(*args, **kwargs):
    print("Arguments: ", args)
    print("Keyword arguments: ", kwargs)

pack_em_up(3, 4, 9, foo=42, bar=7)
print()
