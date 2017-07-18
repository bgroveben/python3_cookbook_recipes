# You want to perform various calculations on a dictionary of data.
# Consider a dictionary that maps stock names to prices.

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# In order to perform calculations on the dictionary contents, it is often useful to invert the keys and values of the dictionary using the zip() function.
# https://docs.python.org/3/library/functions.html#zip
# Here is how to find the minimum and maximum price and stock name.
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
print()
print('min price: ', min_price)
print('max price: ', max_price)
print()

# Similarly, to rank the data, use zip() with sorted() as follows:
print('sorted_prices: ')
prices_sorted = sorted(zip(prices.values(), prices.keys()))
for price, name in prices_sorted:
    print('    ', name, price)
print()

# If you try to perform common data reductions on a dictionary, you'll find that only the keys are processes, not the values.
print(min(prices))
print(max(prices))
print()

# This is probably not aht you want because you're actually trying to perform a calculation involving the dictionary values.
# You might try to fix this using the values() method of a dictionary.
print(min(prices.values()))
print(max(prices.values()))
print()

# Unfortunately, this is often not exactly what you want either.
# For example, you may want to know information about the corresponding keys (e.g., which stock has the lowest price?).

# You can get the key corresponding to the min or max value if you supply a key function to min() and max():
print(min(prices, key=lambda k: prices[k]))
print(max(prices, key=lambda k: prices[k]))
print()

# However, to get the minimum value, you need to perform an extra lookup step.
min_value = prices[min(prices, key=lambda k: prices[k])]
print(min_value)
# Same goes for maximum value:
max_value = prices[max(prices, key=lambda k: prices[k])]
print(max_value)
print()

# The solution involving zip() solves the problem by "inverting" the dictionary into a sequence of (value, key) pairs.
# When performing comparisons on such tuples, the value element is compared first, followed by te key.
# This gives you exactly the behavior that you want and allows reductions and sorting to be easily performed on the dictionary contents using a single statment.

# It should be noted that in calculations involving (value, key) pairs, the key will be used to determine the result in instances where multiple entries happen to have the same value.
# For instance, in calculations such as min() and max(), the entry with the largest or smallest key will be returned if there are duplicate values.
more_prices = { 'AAA': 45.23, 'ZZZ': 45.23 }
print(min(zip(more_prices.values(), more_prices.keys())))
print(max(zip(more_prices.values(), more_prices.keys())))
print()
