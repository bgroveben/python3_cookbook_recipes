# You want to make a list of the smallest or largest N items in a collection.

# The heapq module has two functions - nlargest() and nsmallest() - that do
# exactly what you want:
import heapq

print()
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))
print()

# Both functions also accept a key parameter that alows them to be used with
# more complicated data structures:
portfolio = [
   {'name': 'IBM', 'shares': 100, 'price': 91.1},
   {'name': 'AAPL', 'shares': 50, 'price': 543.22},
   {'name': 'FB', 'shares': 200, 'price': 21.09},
   {'name': 'HPQ', 'shares': 35, 'price': 31.75},
   {'name': 'YHOO', 'shares': 45, 'price': 16.35},
   {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
print(cheap)
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print(expensive)
print()

# If you are looking for the N smallest or largest items and N is small
# compared to the overall size of the collection, these functions offer
# superior performance.
# Underneath the covers, they work by first converting the data into a list
# where items are ordered as a heap:
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(nums)
heap = list(nums)
print(heap)
heapq.heapify(heap)
print(heap)
print(type(heap))
print()

# The most significant feature of a heap is that heap[0] is always the smallest
# item.
# Moreover, subsequent items can be easily found using the heapq.heappop()
# method, which pops off the first item and replaces it with the next smallest
# item (an operation that requires O(log N) operations where N is the size of
# the heap).
# For example, find the 3 smallest items in heap:
print(heap)
heapq.heappop(heap)
print(heap)
heapq.heappop(heap)
print(heap)
heapq.heappop(heap)
print(heap)
print()
