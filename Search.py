from queue import Queue
from queue import LifoQueue

import Utility
from Puzzle8 import Puzzle8


class Search:

    def __init__(self):
        pass

    def bfs(self, puzzle: Puzzle8):
        queue_bfs = Queue()
        self.help_search(queue_bfs, puzzle)

    def dfs(self, puzzle: Puzzle8):
        stack = LifoQueue()
        self.help_search(stack, puzzle)

    def ucs(self):
        pass

    def a_star(self):
        pass

    def dls(self):
        pass

    def ids(self):
        pass

    def help_search(self, collect, puzzle):
        # add initial state to queue:
        collect.put(puzzle)

        while not collect.empty():
            puzzle_help = collect.get()
            print(puzzle_help)

            if Utility.is_goal(puzzle_help):
                print("GOAL Found ")
                return

            possible_states = puzzle_help.expand()

            for state in possible_states:
                collect.put(state)
