from Puzzle8 import Puzzle8
from Search import Search
import Utility

test = [3, 2, 1, 4, 5, 6, 0, 7, 8]

p = Puzzle8(test)

search = Search()

search.a_star(p)