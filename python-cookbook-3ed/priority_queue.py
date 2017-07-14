# Implementing a Priority Queue

# You want to implement a queue that sorts items by a given priority and always
# returns the item with the highest priority on each pop operation.

# The following class uses the heapq module to implement a simple priority
# queue:
print()
import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

# Here is an example of how it might be used:
class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())

# Having the index method helps avoid a TypeError: unorderable types:
a = (1, 0, Item('foo'))
b = (5, 1, Item('bar'))
c = (1, 2, Item('grok'))
print(a < b)
print(a < c)
print()
