# Itertools is a module in the Python standard library that allows you to
# create iterators for efficient looping.
# For example, permutations allows you to generate all of the possible ways of
# ordering a set of objects:
print()
from itertools import permutations

for p in permutations([1, 2, 3]):
    print(p)

print()
