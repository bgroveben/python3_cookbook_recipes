# Finding Commonalities in Two Dictionaries

# You have two dictionaries and want to find out what they might have in common (same keys, same values, etc).

a = {
   'x' : 1,
   'y' : 2,
   'z' : 3
}

b = {
   'w' : 10,
   'x' : 11,
   'y' : 2
}

# To find out what the two dictionaries have in common, simply perform common set operations using the keys() or items() methods.
print()
# Find keys in common:
print(a.keys() & b.keys())
# Find keys in a that are not in b:
print(a.keys() - b.keys())
# Find (key, value) pairs in common:
print(a.items() & b.items())
print()

# These kinds of operations can also be used to alter or filter dictionary contents.
# For example, suppose you want to make a new dictionary with selected keys removed.
# That can be done using a dictionary comprehension:
new_dict = {key:a[key] for key in a.keys() - {'z', 'w'}}
print(new_dict)
