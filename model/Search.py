from queue import Queue
from queue import LifoQueue
from queue import PriorityQueue
from model import Utility
from model.Puzzle8 import Puzzle8


class Search:

    def __init__(self):
        pass

    def bfs(self, puzzle: Puzzle8):
        queue_bfs = Queue()
        self.help_search(queue_bfs, puzzle)

    def dfs(self, puzzle: Puzzle8):
        stack = LifoQueue()
        self.help_search(stack, puzzle)

    def ucs(self, puzzle: Puzzle8):
        queue_pro = PriorityQueue()

        queue_pro.put((puzzle.get_priority(), puzzle))

        while not queue_pro.empty():
            puzzle_help = queue_pro.get()[1]
            print(puzzle_help)

            if Utility.is_goal(puzzle_help):
                print("GOAL Found ")
                return

            possible_states = puzzle_help.expand()

            for p in possible_states:
                queue_pro.put((puzzle.get_priority(), p))

    def a_star(self, puzzle: Puzzle8):

        queue_pro = PriorityQueue()

        queue_pro.put((puzzle.get_priority() + Utility.get_hurestic1(puzzle), puzzle))

        while not queue_pro.empty():

            puzzle_help = queue_pro.get()[1]
            print(puzzle_help)

            if Utility.is_goal(puzzle_help):
                print("GOAL Found ")
                return

            possible_states = puzzle_help.expand()

            for item in possible_states:
                queue_pro.put((item.get_priority() + Utility.get_hurestic1(item), item))

    def a_star_heuristic_2(self, puzzle: Puzzle8):

        queue_pro = PriorityQueue()

        queue_pro.put((puzzle.get_priority() + Utility.get_hurestic2(puzzle), puzzle))

        while not queue_pro.empty():

            puzzle_help = queue_pro.get()[1]

            if Utility.is_goal(puzzle_help):
                print("GOAL Found ")
                return

            possible_states = puzzle_help.expand()

            for item in possible_states:
                queue_pro.put((item.get_priority() + Utility.get_hurestic2(item), item))

    def ids(self, puzzle: Puzzle8):

        counter = 0

        while True:

            # add initial state to queue:
            stack = LifoQueue()
            stack.put(puzzle)
            while not stack.empty():
                puzzle_help = stack.get()
                print(puzzle_help)

                if Utility.is_goal(puzzle_help):
                    print("GOAL Found ")
                    return

                possible_states = puzzle_help.expand()

                for state in possible_states:
                    if state.get_priority() <= counter:
                        stack.put(state)
            counter += 1

    def ida_star(self, puzzle: Puzzle8):
        cutoff = Utility.get_hurestic1(puzzle)

        while True:
            stack = LifoQueue()
            stack.put(puzzle)

            while not stack.empty():
                puzzle_help = stack.get()
                print(puzzle_help)

                if Utility.is_goal(puzzle_help):
                    print("GOAL Found ")
                    return

                possible_states = puzzle_help.expand()

                for state in possible_states:
                    pri = state.get_priority() + Utility.get_hurestic1(state)
                    if pri < cutoff:
                        stack.put(state)
            cutoff += 1

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
