# https://docs.python.org/3/library/itertools.html
# https://docs.python.org/3/library/itertools.html#itertools-recipes

# itertools is a module in the Python standard library that allows you to
# create iterators for efficient looping.
# For example, permutations allows you to generate all of the possible ways of
# ordering a set of objects:
print()
from itertools import permutations

for p in permutations([1, 2, 3]):
    print(p)

print()

# Similarly, combinations generates all of the possible ways of selecting items
# from a collection.
# Unlike permutations, the order does not matter.
from itertools import combinations
for c in combinations([1, 2, 3, 4], 2):
    print(c)

print()

# itertools also contains utitlity functions such as chain, which takes
# iterables and creates a new iterator that returns elements from the given
# iterables sequentially, as a single sequence.
from itertools import chain

for c in chain(range(3), range(12, 15)):
    print(c)

print()
