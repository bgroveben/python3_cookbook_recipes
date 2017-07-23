# Sorting a List of Dictionaries by a Common Key

# You have a list of dictionaries and you would like to sort the entries according to one or more of the dictionary values.

# Sorting this type of structure is easy using the operator module's itemgetter() function.
# Let's say you've queried a database table to get a listing of the members on your website, and you receive the following data structure in return:

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

# It's fairly easy to output these rows ordered by any of the fields common to all of the dictionaries.

from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))

print()
print(rows_by_fname)
print()
print(rows_by_uid)
print()

# The itemgetter() function can also accept multiple keys.
rows_by_lfname = sorted(rows, key=itemgetter('lname','fname'))
print(rows_by_lfname)
print()

# In this example, rows is passed to the built-in sorted() function, whaich accepts a keyword argument key.
# This argument is expected to be a callable that accepts a single item from rows as input and returns a value that will be used as the basis for sorting.
# The itemgetter function creates just such a callable.

# The operator.itemgetter() function takes as arguments the lookup indices used to extract the desired values from the records in rows.
# It can be a dictionary key name, a numeric list element, or any value that can be fed to an object's __getitem__() method.
# If you give multiple indices to itemgetter(), the callable it produces will return a tuple with all of the elements in it, and sorted() will order the output according to the sorted order of the tuples.
# This can be useful if you want to simultaneously sort on multiple fields (such as first and last name, as shown in the example).

# The functionality of itemgetter() is sometimes replaced by lambda expressions.
rows_by_fname = sorted(rows, key=lambda r: r['fname'])
rows_by_lfname = sorted(rows, key=lambda r: (r['lname'],r['fname']))
print(rows_by_fname)
print()
print(rows_by_lfname)
print()

# This solution often works just fine.
# However, the solution involving itemgetter() typically runs a bit faster, you you may prefer it if performance is a concern.

# Last, but not least, don't forget that the technique shown in this recipe can be applied to functions such as min() and max().
print(min(rows, key=itemgetter('uid')))
print()
print(max(rows, key=itemgetter('uid')))
print()
