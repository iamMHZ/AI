from queue import Queue
from queue import LifoQueue
from queue import PriorityQueue
from multiprocessing import Queue as multQueue
import threading
import Utility
from Puzzle8 import Puzzle8
import heapq


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
        heap = []

        pro = puzzle.get_priority()
        heapq.heappush(heap, (pro + Utility.get_hurestic1(puzzle), puzzle))

        while heap.__sizeof__() > 0:
            tup = heapq.heappop(heap)
            puzzle_help = tup[1]
            print(type(tup[0]))
            print(type(tup[1]))
            print(f"TUPLE:({str(tup[0] )},{str(tup[1])})\n and Puzzle  :  {puzzle_help}")

            if Utility.is_goal(puzzle_help):
                print("GOAL Found ")
                return

            possible_states = puzzle_help.expand()

            for item in possible_states:
                if isinstance(item, Puzzle8):
                    huristic = Utility.get_hurestic1(item)
                    pro = item.get_priority() + huristic
                    # while True:
                    #     if queue_pro.task_done():
                    #         pass
                    heapq.heappush(heap, (pro + Utility.get_hurestic1(puzzle), item))

    def enqueue_helper(self, queue_pro, pro, item):
        pass

    def a_star_heuristic_2(self, puzzle: Puzzle8):
        queue_pro = PriorityQueue()

        queue_pro.put((puzzle.get_priority() + Utility.get_hurestic2(puzzle), puzzle))

        while not queue_pro.empty():
            puzzle_help = queue_pro.get()[1]
            print(puzzle_help)

            if Utility.is_goal(puzzle_help):
                print("GOAL Found ")
                return

            possible_states = puzzle_help.expand()

            for p in possible_states:
                queue_pro.put((p.get_priority() + Utility.get_hurestic2(p), p))

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
