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
