# Filtering Sequence Elements

# You have data inside of a sequence, and need to extract values or reduce the sequence using some criteria.

# List comprehensions are a straightforward way to filter sequence data.
print()
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
print([n for n in mylist if n > 0])
print([n for n in mylist if n < 0])
print()

# If the original input is large and you don't want to produce a large result, use a generator expression to produce the filtered values iteratively.
positive = (n for n in mylist if n > 0)
print(positive)
# Here's another list comprehension, just because list comprehensions.
print([x for x in positive])
# Here's the generator expression again, because they go poof after one iteration.
positive = (n for n in mylist if n > 0)
for x in positive:
    print(x)
print()

# Sometimes, the filtering criteria cannot be easily expressed in a list comprehension or a generator expression.
# For example, suppose that the filtering process involves exception handling or some other detail.
# In these cases, put the filtering code into its own function and use the built-in filter() function.
values = ['1', '2', '-3', '-', '4', 'N/A', '5']

def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

# The filter() function creates an iterator, so if you want to create a list of results, make sure you also use the list() function.
ivals = list(filter(is_int, values))
print(ivals)
print()

# This generator expression does the same thing as the code with the filter function.
the_ints = (i for i in values if is_int(i))
print(the_ints)
print([value for value in the_ints])
print()

# List comprehensions and generator expressions are often the easiest and most straightforward ways to filter simple data.
# They also have the added power to transform the data at the same time.
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
import math
print([math.sqrt(n) for n in mylist if n > 0])
print()

# One variation on filtering involves replacing the values that don't meet the criteria with a new value instead of discarding them.
# For example, perhaps instead of just finding positive values, you also want to clip undesired values to fit within a specified range.
# This is often easily accomplished by moving the filter criterion into a conditional expression like this.
trim_negatives = [n if n > 0 else 0 for n in mylist]
print(trim_negatives)
trim_positives = [n if n < 0 else None for n in mylist]
print(trim_positives)
print()

# Another nifty filtering tool is itertools.compress(), which takes an iterable and an accompanying Boolean selector sequence as input.
# https://docs.python.org/3/library/itertools.html#itertools.compress
# As output, it gives you all of the items in the iterable where the corresponding element in the selector is True.
# This can be useful if you're trying to apply the results of filtering one sequence to another related sequence.
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK'
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]

counts = [ 0, 3, 10, 4, 1, 7, 6, 1]

# Suppose you want to make a list of all addresses where the corresponding count value is greater than 5.
# Here is one way to do that:
from itertools import compress
greater_than5 = [n > 5 for n in counts]
print(greater_than5)
print(tuple(compress(addresses, greater_than5)))
print()

# The key here is to first create a sequence of Booleans that indicates which elements satisfy the desired condition.
# The compress() function then picks out the items corresponding to True values.
# Like filter(), compress() normally returns an iterator, so you need to use a sequence type like list() or tuple() to view the results.
