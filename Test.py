from Puzzle8 import Puzzle8
from Search import Search
import Utility

test = [3, 2, 1, 4, 5, 6, 0, 7, 8]

p = Puzzle8(test)

search = Search()

print(Utility.get_hurestic1(p))
print(Utility.get_hurestic2(p))
