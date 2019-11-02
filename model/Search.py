from queue import Queue, LifoQueue, PriorityQueue
from utility.MyNode import MyNode
from model.Puzzle8 import Puzzle8
from utility import Utility


class Search:

    def __init__(self):
        pass

    def bfs(self, puzzle: Puzzle8):
        queue_tree = Queue()
        queue_bfs = Queue()
        return help_search(queue_bfs, puzzle, queue_tree)

    def dfs(self, puzzle: Puzzle8):
        queue_tree = LifoQueue()
        stack = LifoQueue()
        return help_search(stack, puzzle, queue_tree)

    def ucs(self, puzzle: Puzzle8):
        tree_quene = PriorityQueue()
        queue_pro = PriorityQueue()

        tree = MyNode(puzzle)
        tree_quene.put((puzzle.get_priority(), tree))
        queue_pro.put((puzzle.get_priority(), puzzle))

        while not queue_pro.empty():
            puzzle_help = queue_pro.get()[1]
            node_parent = tree_quene.get()[1]
            print(puzzle_help)
            if Utility.is_goal(puzzle_help):
                return puzzle_help, tree

            possible_states = puzzle_help.expand()

            for p in possible_states:
                queue_pro.put((puzzle.get_priority(), p))
                node_help = MyNode(p, parent=node_parent)
                tree_quene.put((puzzle.get_priority(), node_help))

    def a_star(self, puzzle: Puzzle8):
        tree_quene = PriorityQueue()
        queue_pro = PriorityQueue()

        tree = MyNode(puzzle)
        tree_quene.put((puzzle.get_priority() + Utility.get_hurestic1(puzzle), tree))
        queue_pro.put((puzzle.get_priority() + Utility.get_hurestic1(puzzle), puzzle))

        while not queue_pro.empty():

            puzzle_help = queue_pro.get()[1]
            node_parent = tree_quene.get()[1]
            print(puzzle_help)
            if Utility.is_goal(puzzle_help):
                return puzzle_help, tree

            possible_states = puzzle_help.expand()

            for item in possible_states:
                queue_pro.put((item.get_priority() + Utility.get_hurestic1(item), item))
                node_help = MyNode(item, parent=node_parent)
                tree_quene.put((item.get_priority() + Utility.get_hurestic1(item), node_help))

    def a_star_heuristic_2(self, puzzle: Puzzle8):
        tree_quene = PriorityQueue()
        queue_pro = PriorityQueue()

        tree = MyNode(puzzle)
        tree_quene.put((puzzle.get_priority() + Utility.get_hurestic2(puzzle), tree))
        queue_pro.put((puzzle.get_priority() + Utility.get_hurestic2(puzzle), puzzle))

        while not queue_pro.empty():

            puzzle_help = queue_pro.get()[1]
            node_parent = tree_quene.get()[1]
            print(puzzle_help)
            if Utility.is_goal(puzzle_help):
                return puzzle_help, tree

            possible_states = puzzle_help.expand()

            for item in possible_states:
                queue_pro.put((item.get_priority() + Utility.get_hurestic2(item), item))
                node_help = MyNode(item, parent=node_parent)
                tree_quene.put((item.get_priority() + Utility.get_hurestic2(item), node_help))

    def ids(self, puzzle: Puzzle8):

        counter = 0

        while True:

            # add initial state to queue:
            tree_quene = LifoQueue()
            stack = LifoQueue()

            tree = MyNode(puzzle)

            tree_quene.put(tree)
            stack.put(puzzle)

            while not stack.empty():
                puzzle_help = stack.get()
                node_parent = tree_quene.get()
                print(puzzle_help)
                if Utility.is_goal(puzzle_help):
                    return puzzle_help, tree

                possible_states = puzzle_help.expand()

                for state in possible_states:
                    if state.get_priority() <= counter:
                        stack.put(state)
                        node_help = MyNode(state, parent=node_parent)
                        tree_quene.put(node_help)
            counter += 1

    def ida_star(self, puzzle: Puzzle8):
        cutoff = Utility.get_hurestic1(puzzle)

        while True:

            tree_quene = LifoQueue()
            stack = LifoQueue()

            tree = MyNode(puzzle)

            tree_quene.put(tree)
            stack.put(puzzle)

            while not stack.empty():
                puzzle_help = stack.get()
                node_parent = tree_quene.get()
                print(puzzle_help)
                if Utility.is_goal(puzzle_help):
                    return puzzle_help, tree

                possible_states = puzzle_help.expand()

                for state in possible_states:
                    pri = state.get_priority() + Utility.get_hurestic1(state)
                    if pri < cutoff:
                        stack.put(state)
                        node_help = MyNode(state, parent=node_parent)
                        tree_quene.put(node_help)
            cutoff += 1


def help_search(collect, puzzle, tree_quene):
    # add initial state to queue:
    collect.put(puzzle)
    tree = MyNode(puzzle)
    tree_quene.put(tree)
    while not collect.empty():
        puzzle_help = collect.get()
        node_parent = tree_quene.get()
        print(puzzle_help)
        if Utility.is_goal(puzzle_help):
            return puzzle_help, tree

        possible_states = puzzle_help.expand()

        for state in possible_states:
            collect.put(state)
            node_help = MyNode(state, parent=node_parent)
            tree_quene.put(node_help)

# def RBFS(self, puzzle: Puzzle8, f_limit):
#     if Utility.is_goal(puzzle):
#         return puzzle
#     f = {}
#     successors = puzzle.expand()
#     if successors.__len__():
#         return None, sys.maxsize
#     for s in successors:
#         f[s] = max(s.get_priority() + Utility.get_hurestic1(s), f[puzzle])
#     while True:
#         best = lowestValue(f)
#         if f[best] > f_limit:
#             return None, f[best]
#         alternative = secondValue(f)
#         result, f[best] = self.RBFS(best, min(f_limit, alternative))
#         if result is not None:
#             return result

#     def RBFS(self, puzzle: Puzzle8):
#         pass
#
#     def sma_star(self, puzzle: Puzzle8, max_size):
#
#         queue = PriorityQueue(maxsize=max_size)
#         queue.put((puzzle.get_priority() + Utility.get_hurestic1(puzzle), puzzle))
#
#         while not queue.empty():
#             puzzle_help = queue.get()[1]
#             parent_puzzle = queue.get()[0]
#
#             if Utility.is_goal(puzzle_help):
#                 return
#
#             possible_states = puzzle_help.expand()
#
#             minimum = sys.maxsize
#             dic_expnd = {}
#             for state in possible_states:
#                 pri = state.get_priority() + Utility.get_hurestic1(state)
#                 dic_expnd[state] = pri
#                 if minimum < pri:
#                     minimum = pri
#
#             queue.put((parent_puzzle, puzzle_help))
#             for state, pri in dic_expnd:
#                 queue.put((pri, state))
#
#
# def lowestValue(f: dict):
#     lowest = None
#     min_help = sys.maxsize
#     for key, value in f.items():
#         if value < min_help:
#             lowest = key
#             min_help = value
#     return lowest
#
#
# def secondValue(f: dict):
#     lowest = None
#     lowest2 = None
#     min_help = sys.maxsize
#     min_help = sys.maxsize
#
#     for key, value in f.items():
#         if value < min_help:
#             lowest2 = lowest
#             lowest = key
#             min_help2 = min_help
#             min_help = value
#
#     return lowest2
