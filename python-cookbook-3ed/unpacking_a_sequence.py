# You have an N-element tuple or sequence that you would like to unpack into a
# collection of N variables.
print()

# Unpack a tuple:
tup = (4,5)
x, y = tup
print(x, '\n', y, '\n')

# Unpack a list:
data = ['ACME', 50, 91.1, (2012, 12, 21) ]
name, shares, price, date = data
print(name, '\n', shares, '\n', price, '\n' ,date, '\n')
name, shares, price, (year, month, day) = data
print(name, '\n', year, '\n', month, '\n' ,day, '\n')

# Unpacking works with any iterable:
s = 'Hello'
a, b, c, d, e = s
print(a, '\n', b, '\n', c, '\n', d, '\n', e, '\n')

# When unpacking, you may want to discard certain values.
# Python has no special syntax for this, but you can pick a throwaway variable
# name for the value:
data = ['ACME', 50, 91.1, (2012, 12, 21) ]
_, shares, price, _ = data
print(shares, '\n', price, '\n')
