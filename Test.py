from Puzzle8 import Puzzle8
from Search import Search
import Utility
import heapq

test = [1, 2, 3, 4, 5, 0, 6, 7, 8]

p = Puzzle8(test)

search = Search()

search.ids(p)

# stack = []
#
# stack.append(1)
# stack.append(12)
# stack.append(3)
#
# print(stack.pop())
# stack.append(0)
# print(stack.pop())
# stack.append(30)

# print(stack)
#
# l1 = []
#
# l1.append(1)
# l1.append(2)
#
# l2 = l1.copy()
#
# print(l1)
# print(l2)
#
# l1.pop()
#
# print(l1)
# print(l2)
