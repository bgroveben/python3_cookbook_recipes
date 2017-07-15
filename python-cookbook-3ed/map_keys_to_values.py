# Mapping Keys to Multiple Values in a Dictionary

# You want to make a dictionary that maps keys to more than one value (a
# so-called "multidict").

# A dictionary is a mapping where each key is mapped to a single value.
# If you want to map keys to multiple values, you need to store the multiple
# values in another container such as a list or set.

d = {
   'a' : [1, 2, 3],
   'b' : [4, 5]
}

e = {
   'a' : {1, 2, 3},
   'b' : {4, 5}
}

# Use a list if you want to preserve the insertion order of the items.
# Use a set if you want to eliminate duplicates and don't care about the order.

# To easily construct such dictionaries, you can use defaultdict in the
# collections module.
# A feature of defaultdict is that it automatically initializes the first value
# so you can simply focus on adding items.
print()
from collections import defaultdict

dl = defaultdict(list)
dl['a'].append(1)
dl['a'].append(2)
dl['a'].append(4)
# ...
print(dl)
print()
ds = defaultdict(set)
ds['a'].add(1)
ds['a'].add(2)
ds['a'].add(4)
# ...
print(ds)
print()
# One issue with defaultdict is that it will automatically create dictionary
# entries for keys accessed later on (even if they aren't currently found in
# the dictionary).
# If you don't want this behavior, you might use setdefault() on an ordinary
# dictionary instead.
dr = {}    # A regular dictionary
dr.setdefault('a', []).append(1)
dr.setdefault('a', []).append(2)
dr.setdefault('a', []).append(4)
# ...
print(dr)
print()

# In principle, constructing a multivalued dictionary is simple.
# However, initialization of the first value can be messy if you try to do it
# yourself.

d_messy = {}
for key, value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)

# Using defaultdict simply leads to much cleaner code.

d_clean = defaultdict(list)
for key, value in pairs:
    d[key].append(value)

# This recipe is strongly related to the problem of grouping records together
# in data processing problems.
