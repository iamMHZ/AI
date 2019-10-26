import queue
from Movement import Movement


# it is class puzzle8


class Puzzle8:

    def __init__(self, data, state_stack=[]):
        self.data = data
        self.state_stack = state_stack

    def __str__(self):
        return str(self.data) + "\n\n"

    def __eq__(self, other):
        if self.data == other.data:
            return True
        else:
            return False

    def __lt__(self, other):
        if len(self.state_stack) < len(other.state_stack):
            return True
        else:
            return False

    def swap(self, _list, to, _from):
        _list[to], _list[_from] = _list[_from], _list[to]
        return _list

    def get_priority(self):
        return len(self.state_stack)

    # comparing two objects
    def __lt__(self, other):
        if len(other.state_stack) > len(self.state_stack):
            return False

        return True

    def expand(self):
        # taking a copy of current state of this 8-puzzle

        possible_states = list()

        # we assume that 0 is our blank space in puzzle
        space_index = self.data.copy().index(0)

        # print(self.state_stack.queue)
        if space_index == 0:

            new_state = self.swap(self.data.copy(), 0, 1)
            stack = self.state_stack.copy()
            stack.append(Movement.RIGHT)
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

            new_state = self.swap(self.data.copy(), 0, 3)
            stack = self.state_stack.copy()
            stack.append(Movement.DOWN)
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

        elif space_index == 1:
            new_state = self.swap(self.data.copy(), 1, 0)
            stack = self.state_stack.copy()
            stack.append(Movement.LEFT)
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

            new_state = self.swap(self.data.copy(), 1, 4)
            stack = self.state_stack.copy()
            stack.append(Movement.DOWN)
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

        elif space_index == 2:
            new_state = self.swap(self.data.copy(), 2, 1)
            stack = self.state_stack.copy()
            stack.append(Movement.LEFT)
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

            new_state = self.swap(self.data.copy(), 2, 5)
            stack = self.state_stack.copy()
            stack.append(Movement.DOWN)
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

        elif space_index == 3:
            new_state = self.swap(self.data.copy(), 3, 0)
            stack = self.state_stack.copy()
            stack.append(Movement.UP)
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

            new_state = self.swap(self.data.copy(), 3, 4)
            stack = self.state_stack.copy()
            stack.append(Movement.RIGHT)
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

            new_state = self.swap(self.data.copy(), 3, 6)
            stack = self.state_stack.copy()
            stack.append(Movement.DOWN)
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

        elif space_index == 4:
            new_state = self.swap(self.data.copy(), 4, 1)
            stack = self.state_stack.copy()
            stack.append(Movement.UP)
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

            new_state = self.swap(self.data.copy(), 4, 5)
            stack = self.state_stack.copy()
            stack.append(Movement.RIGHT)
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

            new_state = self.swap(self.data.copy(), 4, 3)
            stack = self.state_stack.copy()
            stack.append(Movement.LEFT)
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

            new_state = self.swap(self.data.copy(), 4, 7)
            stack = self.state_stack.copy()
            stack.append(Movement.DOWN)
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

        elif space_index == 5:
            new_state = self.swap(self.data.copy(), 5, 2)
            stack = self.state_stack.copy()
            stack.append(Movement.UP)
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

            new_state = self.swap(self.data.copy(), 5, 4)
            stack = self.state_stack.copy()
            stack.append(Movement.LEFT)
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

            new_state = self.swap(self.data.copy(), 5, 8)
            stack = self.state_stack.copy()
            stack.append(Movement.DOWN)
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

        elif space_index == 6:
            new_state = self.swap(self.data.copy(), 6, 3)
            stack = self.state_stack.copy()
            stack.append(Movement.UP)
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

            new_state = self.swap(self.data.copy(), 6, 7)
            stack = self.state_stack.copy()
            stack.append(Movement.RIGHT)
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

        elif space_index == 7:
            new_state = self.swap(self.data.copy(), 7, 4)
            stack = self.state_stack.copy()
            stack.append(Movement.UP)
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

            new_state = self.swap(self.data.copy(), 7, 6)
            stack = self.state_stack.copy()
            stack.append(Movement.LEFT)
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

            new_state = self.swap(self.data.copy(), 7, 8)
            stack = self.state_stack.copy()
            stack.append(Movement.RIGHT)
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

        elif space_index == 8:
            new_state = self.swap(self.data.copy(), 8, 5)
            stack = self.state_stack.copy()
            stack.append(Movement.UP)
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

            new_state = self.swap(self.data.copy(), 8, 7)
            stack = self.state_stack.copy()
            stack.append(Movement.LEFT)
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

        return possible_states


# method for cloning a stack into two stacks
def my_copy(stack: queue.LifoQueue):
    stack2 = queue.LifoQueue()
    stack3 = queue.LifoQueue()

    stack4 = queue.LifoQueue()
    stack5 = queue.LifoQueue()

    while not stack.empty():
        item = stack.get()
        stack2.put(item)
        stack3.put(item)

    while not stack2.empty():
        stack4.put(stack2.get())
        stack5.put(stack3.get())

    return stack4, stack5
