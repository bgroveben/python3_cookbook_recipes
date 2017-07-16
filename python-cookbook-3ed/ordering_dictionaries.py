# Keeping Dictionaries in Order

# You want to create a dictionary, and you also want to control the order of
# items when iterating or serializing.

# To control the order of items in a dictionary, you can use an OrderedDict from the collections module.
# It exacly preserves the original insertion order of data when iterating.
print()
from collections import OrderedDict

d_ordered = OrderedDict()
d_ordered['foo'] = 1
d_ordered['bar'] = 2
d_ordered['spam'] = 3
d_ordered['grok'] = 4

for key in d_ordered:
    print(key, d_ordered[key])

print()

# An OrderedDict can be particularly useful when you want to build a mapping that you may want to later serialize or encode into a different format.
# For example, if you want to precisely control the order of fields appearing in a JSON encoding, first building the data in an OrderedDict will do the trick.

import json
print(json.dumps(d_ordered))
print()

# An OrderedDict internally maintains a doubly linked lsit that orders the keys according to insertion order.
# When a new item is first inserted, it is placed at the end of this list.
# This means that the size of an OrderedDict is more than twice as large as a normal dictionary due to the extra linked list that's created.
