from queue import Queue
from queue import LifoQueue
from Puzzle8 import Puzzle8


class Search:

    def __init__(self):
        pass

    def bfs(self, puzzle: Puzzle8):
        queue_bfs = Queue()
        # get current
        start = self.puzzle
        # add initial state to queue:
        queue_bfs.put(start)

        while not queue_bfs.empty():
            puzzle_help = queue_bfs.get()

            if self.is_goal(puzzle_help):
                print("GOAL Found ")
                return

            possible_states = puzzle_help.expand()

            for state in possible_states:
                queue_bfs.put(state)

    def dfs(self, puzzle: Puzzle8):
        stack = LifoQueue()
        # get current
        start = self.puzzle
        # add initial state to queue:
        stack.put(start)

        while not stack.empty():
            puzzle_help = stack.get()

            if self.is_goal(puzzle_help):
                print("GOAL Found ")
                return

            possible_states = puzzle_help.expand()

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
