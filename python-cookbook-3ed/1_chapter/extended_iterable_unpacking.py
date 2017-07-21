# It is worth noting that the star syntax can be especially useful when
# iterating over a sequence of tuples of varying length.
# For example, perhaps a sequence of tagged tuples:
print()
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)
print()

# Star unpacking can also be useful when combined with certain kinds of string
# processing operations, such as splitting:
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname,'\n', homedir,'\n', sh,'\n')

# Sometimes you might want to unpack values and throw them away.
# You can't just specify a bare * when unpacking, but you can use a common
# throwaway variable name, such as _ or ign (ignored):
record = ('ACME', 50, 123.45, (12, 18, 2017))
name, *_, (*_, year) = record
print(name,'\n', year,'\n')

# There is a certain similarity between star unpacking and list-processing
# features of various functional languages.
# For example, if you have a list, you can easily split it into head and tail
# components like this:
items = [1, 10, 7, 4, 5, 9]
head, *tail = items
print(head, '\n', tail, '\n')

# One could imagine writing functions that perform such splitting in order to
# carry out some kind of clever recursive algorithm:
def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head

print(sum(items))
print()

# However, be aware that recursion isn't really a strong Python feature due to
# the inherent recursion limit.
