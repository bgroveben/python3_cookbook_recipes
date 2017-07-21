# Removing Duplicates from a Sequence while Maintaining Order

# You want to eliminate duplicate values in a sequence, but preserve the order of the remaining items.

# If the values in the sequence are hashable, the problem can be easily solved using a set and a generator.
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

# Let's use this function:
print()
a = [1, 5, 2, 1, 9, 1, 5, 10, 9, 10]
print(list(dedupe(a)))
print()

# This only works if the items in the sequence are hashable.
# If you are trying to eliminate duplicates in a sequence of unhashable types (such as dicts), you can make a slight change to this recipe, as follows:
def unhashable_dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

# Here, the purpose of the key argument is to specify a function that converts sequence items into a hashable type for the purposes of duplicate detection.
# Umm, yeah; here's how that works:
b = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x': 2, 'y':3}, {'x':2, 'y':4}, {'x':2, 'y':4}]
print(list(unhashable_dedupe(b, key=lambda d: (d['x'], d['y']))))
print()
print(list(unhashable_dedupe(b, key=lambda d: d['x'])))
print()

# This latter solution also works nicely if you want to eliminate duplicates based on the value of a single field or attribute or a larger data structure.

# If all you want to do is eliminate duplicates, it is often easy enough to make a set.
print(a)
print(set(a))
print()

# However, this approach doesn't preserve the original ordering of the list a, and the resulting data will be scrambled afterward.

# The use of a generator function in this recipe reflects the fact that you might want the function to be extremely general purpose -- not necessarily tied directly to list processing.
# For example, if you want to read a file, eliminating duplicate lines, you could simply do this:
with open('example.txt', 'r') as f:
    for line in dedupe(f):
        # do somethig
        pass
f.close()

# The specification of a key function mimics similar functionality in built-in functions such as sorted(), min(), and max().
