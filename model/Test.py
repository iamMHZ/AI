from model.Puzzle8 import Puzzle8
from model.Search import Search

test = [1, 2, 3, 4, 5, 6, 0, 7, 8]

test2 = [2, 1, 3, 4, 5, 6, 0, 7, 8]

# print(test.__cmp__(test2))
p = Puzzle8(test)
p1 = Puzzle8(test2)

# print(p.__cmp__(p1))
search = Search()
# print( p < p1)
search.a_star(p)

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
