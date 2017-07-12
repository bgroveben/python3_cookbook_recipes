# You want to keep a limited history of the last few items seen during
# iteration or during some other kind of processing.

# Keeping a limited history is a perfect use for a collections.deque.
# For example, the following code performs a simple text match on a sequence of
# lines and yields the matching line along with the previous N lines of context
# when found:
print()
from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

# Example use on a file:
if __name__=="__main__":
    with open('example.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)

# Using deque(maxlen=N) creates a fixed-sized queue.
# When new items are added and the queue is full, the oldest item is
# automatically removed:
print()
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)
q.append(5)
print(q)
print()

# More generally, a deque can be used whenever you need a simple queue
# structure.
# If you don't give it a maximum size, you get an unbounded queue that lets you
# append and pop items on either end:
q = deque()
q.append(1)
q.append(2)
q.append(3)
print(q)
q.appendleft(4)
print(q)
q.pop()
print(q)
q.popleft()
print(q)
print()

# Adding or popping items from either end of a queue has O(1) complexity.
# Inserting or removing items from the front of the list is O(N).
