from queue import Queue
from queue import LifoQueue
from Puzzle8 import Puzzle8


class Search:

    def __init__(self):
        pass

    def bfs(self, puzzle: Puzzle8):
        queueBfs = Queue()
        # get current
        start = self.puzzle.data
        # add initial state to queue:
        queueBfs.put(start)

        while not queueBfs.empty():
            current = queueBfs.get()

            if self.is_goal(current):
                print("GOAL Found ")
                return

            possible_states = puzzle.expand(current)

            for state in possible_states:
                queueBfs.put(state)

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
