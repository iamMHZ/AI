import queue
from puzzle8 import Puzzle8


class Search:

    def __init__(self):
        pass

    def bfs(self, puzzle: Puzzle8):
        q = queue.Queue()
        # get current
        start = self.puzzle.data
        # add initial state to queue:
        queue.put(start)

        while not queue.empty():
            current = q.get()

            if self.is_goal(current):
                print("GOAL Found ")
                return

            possible_states = puzzle.expand(current)

            for state in possible_states:
                q.put(state)

    def dfs(self):
        pass

    def ucs(self):
        pass

    def astar(self):
        pass

    def dls(self):
        pass

    def ids(self):
        pass
