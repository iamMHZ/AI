import utility.MyNode

goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]


def is_goal(puzzle):
    return puzzle.data == goal


def get_hurestic1(puzzle):
    c = 0
    index = 0
    for i in puzzle.data:
        if i != goal[index]:
            c += 1
        index += 1
    return c


def get_hurestic2(puzzle):
    c = 0
    index = 0
    for i in range(0, 9):
        help = abs(goal.index(i) - puzzle.data.index(i))
        c += help // 3
        c += help % 3
    return c


def printer(pri: str):
    p_help = pri.split("\n")
    f = str(p_help).replace("]', '[", ", ").replace("['[", "[").replace("]']", "]")
    return f


def help_search(self, collect, puzzle, tree_quene):
    # add initial state to queue:
    collect.put(puzzle)
    tree = utility.MyNode(puzzle)
    tree_quene.put(tree)
    while not collect.empty():
        puzzle_help = collect.get()
        node_parent = tree_quene.get()
        print(puzzle_help)
        if is_goal(puzzle_help):
            return puzzle_help, tree

        possible_states = puzzle_help.expand()

        for state in possible_states:
            collect.put(state)
            node_help = utility.MyNode(state, parent=node_parent)
            tree_quene.put(node_help)
