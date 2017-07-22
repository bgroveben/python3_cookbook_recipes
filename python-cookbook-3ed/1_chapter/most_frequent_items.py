# Determining the Most Frequently Occurring Items in a Sequence

# You have a sequence of items, and you would like to determine which items occur most frequently in that sequence.

# The collections.Counter class is designed for just such a problem.
# It even comes with a handy most_common() method that will give you the answer.

# To illustrate, here is a list of words from which you can find those words that occur most often.
print()
words = [
   'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
   'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
   'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
   'my', 'eyes', "you're", 'under'
]

from collections import Counter
word_counts = Counter(words)
print(word_counts)
print()
top_three = word_counts.most_common(3)
print(top_three)
print()

# As input, Counter objects can be fed any sequence of hashable input types.
# Under the hood, a Counter is a dictionary that maps the items to the number of occurrences.
print(word_counts['not'])
print(word_counts['eyes'])
print()

# If you want to increment the count manually, simply use addition.
morewords = ['why','are','you','not','looking','in','my','eyes']
for word in morewords:
    word_counts[word] += 1

print(word_counts['eyes'])
print()

# Or, alternatively, you could use the update() method:
word_counts.update(morewords)
print(word_counts['eyes'])
print(word_counts)
print()

# A little-known feature of Counter instances is that they can be easily combined using various mathematical operations.
a = Counter(words)
b = Counter(morewords)
print(a)
print(b)
print()
# Combine counts:
c = a + b
print(c)
print()
# Subtract counts:
d = a - b
print(d)
print()

# Counter objects are a tremendously useful tool for almost any kind of problem that involves tabulating and counting data.
