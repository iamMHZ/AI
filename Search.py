from queue import Queue
from queue import LifoQueue
from Puzzle8 import Puzzle8


class Search:

    def __init__(self):
        pass

    def bfs(self, puzzle: Puzzle8):
        queueBfs = Queue()
        # get current
        start = self.puzzle
        # add initial state to queue:
        queueBfs.put(start)

        while not queueBfs.empty():
            puzzleHelp = queueBfs.get()

            if self.is_goal(puzzleHelp):
                print("GOAL Found ")
                return

            possible_states = puzzleHelp.expand()

            for state in possible_states:
                queueBfs.put(state)

    def dfs(self, puzzle: Puzzle8):
        stack = LifoQueue()
        # get current
        start = self.puzzle
        # add initial state to queue:
        stack.put(start)

        while not stack.empty():
            puzzleHelp = stack.get()

            if self.is_goal(puzzleHelp):
                print("GOAL Found ")
                return

            possible_states = puzzleHelp.expand()

            for state in possible_states:
                stack.put(state)

    def ucs(self):
        pass

    def astar(self):
        pass

    def dls(self):
        pass

    def ids(self):
        pass
