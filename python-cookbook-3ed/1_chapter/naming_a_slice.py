# Naming a Slice

# Your program has become an unreadable mess of hardcoded slice indices and you want to clean it up.

# Suppose you have some code that is pulling specific data fields out of a record string with fixed fields (like from a flat file or similar format):
print()
######     0123456789012345678901234567890123456789012345678901234567890'
record = '....................100          .......513.25     ..........'
cost = int(record[20:32]) * float(record[40:48])
print(cost)
print()

# Instead of doing that, why not name slices like this?
SHARES = slice(20,32)
PRICE = slice(40,48)
cost2 = int(record[SHARES]) * float(record[PRICE])
print(cost2)
print()

# In the latter version, you avoid having a lot of mysterious hardcoded indices, and what you're doing becomes much clearer.

# In general, the built-in slice() creates a slice object that can be used anywhere a slice is allowed.
items = [0, 1, 2, 3, 4, 5, 6]
print(items)
s = slice(2,4)
print(items[2:4])
print(items[s])
items[s] = [10,11]
print(items)
del items[s]
print(items)
print()

# If you have a slice instance s, you can get more information about it by looking at its s.start, s.stop, and s.step attributes, respectively.
a = slice(10, 50, 2)
print(a.start)
print(a.stop)
print(a.step)
print()

# In addition, you can map a slice onto a sequence of a specific size by using its indices(size) method.
# This returns a tuple (start, stop, step) where all values have been suitably limited to fit within bounds (to avoid IndexError exceptions when indexing).
s = "HelloWorld"
print(a.indices(len(s)))
for i in range(*a.indices(len(s))):
    print(s[i])
print()
