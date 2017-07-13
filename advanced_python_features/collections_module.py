# collections is a module in the standard library that implements alternative
# container datatypes.
# A Counter is a collection where elements are stored as dictionary keys and
# their counts are stored as dictionary values:
print()
from collections import Counter

a = Counter('blue')
b = Counter('yellow')

print(a)
print(b)
print((a + b).most_common(3))
print()

# A defaultdict is a subclass of dict, which allows you to pass a factory used
# to automatically create a new value when a key is missing:
from collections import defaultdict

my_dict = defaultdict(lambda: 'Default Value')
my_dict['a'] = 42

print(my_dict['a'])
print(my_dict['b'])
print()

# The defaultdict can be used to create a tree data structure:
from collections import defaultdict
import json

def tree():
    """
    Factory that creates a defaultdict that also uses this factory.
    """
    return defaultdict(tree)

root = tree()
root['Page']['Python']['defaultdict']['Title'] = 'Using defaultdict'
root['Page']['Python']['defaultdict']['Subtitle'] = 'Create a tree'
root['Page']['Java'] = None

print(json.dumps(root, indent=4))
print()
