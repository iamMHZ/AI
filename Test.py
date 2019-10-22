from Puzzle8 import Puzzle8
from Search import Search

test = [1, 2, 3, 4, 5, 6, 0, 7, 8]

p = Puzzle8(test)

search = Search()

search.bfs(p)
