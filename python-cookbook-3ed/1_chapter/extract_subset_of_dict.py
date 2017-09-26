# Problem:
# You want to make a dictionary that is a subset of another dictionary.

# Solution:
# This is easily accomplished using a dictionary comprehension.
#######################################################################

prices = {
   'ACME': 45.23,
   'AAPL': 612.78,
   'IBM': 205.55,
   'HPQ': 37.20,
   'FB': 10.75
}

# Make a dictionary of all prices over 200:
p1 = { key:value for key, value in prices.items() if value > 200 }
print("p1: {}".format(p1))
print()

# Make a dictionary of tech stocks:
tech_names = { 'AAPL', 'IBM', 'HPQ', 'MSFT' }
p2 = { key:value for key, value in prices.items() if key in tech_names }
print("p2: {}".format(p2))
print()

# Much of what can be accomplished with a dictionary comprehension might also
# be done by creating a sequence of tuples and passing them to the dict()
# function. For example:

p1 = dict((key, value) for key, value in prices.items() if value > 200)
print("p1: {}".format(p1))
print()

# However, the dictionary comprehension solution is a bit clearer and actually
# runs quite a bit faster.
# Sometimes there are multiple ways of accomplishing the same thing.
# For instance, the second example could be rewritten as:

tech_names = { 'AAPL', 'IBM', 'HPQ', 'MSFT' }
p2 = { key:prices[key] for key in prices.keys() & tech_names }
print("p2: {}".format(p2))

# However, this solution runs much slower than the first alternative.
