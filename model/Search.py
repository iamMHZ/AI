from anytree import Node, RenderTree
from queue import Queue
from queue import LifoQueue
from queue import PriorityQueue
from model import Utility
from model.Puzzle8 import Puzzle8


class Search:

    def __init__(self):
        pass

    def bfs(self, puzzle: Puzzle8):
        queue_tree = Queue()
        queue_bfs = Queue()
        return self.help_search(queue_bfs, puzzle, queue_tree)

    def dfs(self, puzzle: Puzzle8):
        queue_tree = LifoQueue()
        stack = LifoQueue()
        return self.help_search(stack, puzzle, queue_tree)

    def ucs(self, puzzle: Puzzle8):
        tree_quene = PriorityQueue()
        queue_pro = PriorityQueue()

        tree = Node(puzzle)
        tree_quene.put((puzzle.get_priority(), tree))
        queue_pro.put((puzzle.get_priority(), puzzle))

        while not queue_pro.empty():
            puzzle_help = queue_pro.get()[1]
            node_parent = tree_quene.get()[1]

            if Utility.is_goal(puzzle_help):
                return puzzle_help, tree

            possible_states = puzzle_help.expand()

            for p in possible_states:
                queue_pro.put((puzzle.get_priority(), p))
                node_help = Node(p, parent=node_parent)
                tree_quene.put((puzzle.get_priority(), node_help))

    def a_star(self, puzzle: Puzzle8):
        tree_quene = PriorityQueue()
        queue_pro = PriorityQueue()

        tree = Node(puzzle)
        tree_quene.put((puzzle.get_priority() + Utility.get_hurestic1(puzzle), tree))
        queue_pro.put((puzzle.get_priority() + Utility.get_hurestic1(puzzle), puzzle))

        while not queue_pro.empty():

            puzzle_help = queue_pro.get()[1]
            node_parent = tree_quene.get()[1]

            if Utility.is_goal(puzzle_help):
                return puzzle_help, tree

            possible_states = puzzle_help.expand()

            for item in possible_states:
                queue_pro.put((item.get_priority() + Utility.get_hurestic1(item), item))
                node_help = Node(item, parent=node_parent)
                tree_quene.put((item.get_priority() + Utility.get_hurestic1(item), node_help))

    def a_star_heuristic_2(self, puzzle: Puzzle8):
        tree_quene = PriorityQueue()
        queue_pro = PriorityQueue()

        tree = Node(puzzle)
        tree_quene.put((puzzle.get_priority() + Utility.get_hurestic2(puzzle), tree))
        queue_pro.put((puzzle.get_priority() + Utility.get_hurestic2(puzzle), puzzle))

        while not queue_pro.empty():

            puzzle_help = queue_pro.get()[1]
            node_parent = tree_quene.get()[1]

            if Utility.is_goal(puzzle_help):
                return puzzle_help, tree

            possible_states = puzzle_help.expand()

            for item in possible_states:
                queue_pro.put((item.get_priority() + Utility.get_hurestic2(item), item))
                node_help = Node(item, parent=node_parent)
                tree_quene.put((item.get_priority() + Utility.get_hurestic2(item), node_help))

    def ids(self, puzzle: Puzzle8):

        counter = 0

        while True:

            # add initial state to queue:
            tree_quene = LifoQueue()
            stack = LifoQueue()

            tree = Node(puzzle)

            tree_quene.put(tree)
            stack.put(puzzle)

            while not stack.empty():
                puzzle_help = stack.get()
                node_parent = tree_quene.get()

                if Utility.is_goal(puzzle_help):
                    return puzzle_help, tree

                possible_states = puzzle_help.expand()

                for state in possible_states:
                    if state.get_priority() <= counter:
                        stack.put(state)
                        node_help = Node(state, parent=node_parent)
                        tree_quene.put(node_help)
            counter += 1

    def ida_star(self, puzzle: Puzzle8):
        cutoff = Utility.get_hurestic1(puzzle)

        while True:

            tree_quene = LifoQueue()
            stack = LifoQueue()

            tree = Node(puzzle)

            tree_quene.put(tree)
            stack.put(puzzle)

            while not stack.empty():
                puzzle_help = stack.get()
                node_parent = tree_quene.get()

                if Utility.is_goal(puzzle_help):
                    return puzzle_help, tree

                possible_states = puzzle_help.expand()

                for state in possible_states:
                    pri = state.get_priority() + Utility.get_hurestic1(state)
                    if pri < cutoff:
                        stack.put(state)
                        node_help = Node(state, parent=node_parent)
                        tree_quene.put(node_help)
            cutoff += 1

    def help_search(self, collect, puzzle, tree_quene):
        # add initial state to queue:
        collect.put(puzzle)
        tree = Node(puzzle)
        tree_quene.put(tree)
        while not collect.empty():
            puzzle_help = collect.get()
            node_parent = tree_quene.get()

            if Utility.is_goal(puzzle_help):
                return puzzle_help, tree

            possible_states = puzzle_help.expand()

            for state in possible_states:
                collect.put(state)
                node_help = Node(state, parent=node_parent)
                tree_quene.put(node_help)
