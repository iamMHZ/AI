# it is class puzzle8
import numpy as np


class Puzzle8:

    def __init__(self, data=[], state_stack=[]):
        self.data = data
        self.state_stack = state_stack

    def __str__(self):
        matrix = []
        matrix = np.reshape(self.data, (3, 3))
        return str(self.data[0:3]) + '\n' + str(self.data[3:6]) + '\n' + str(self.data[6:9])

    def __eq__(self, other):
        return self.data == other.data

    # comparing two objects
    def __lt__(self, other):
        return len(other.state_stack) > len(self.state_stack)

    def get_priority(self):
        return len(self.state_stack)

    def expand(self):
        # taking a copy of current state of this 8-puzzle

        possible_states = list()

        # we assume that 0 is our blank space in puzzle
        space_index = self.data.copy().index(0)

        # print(self.state_stack.queue)
        if space_index == 0:

            new_state = self.swap(self.data.copy(), 0, 1)
            stack = self.state_stack.copy()
            stack.append((0, 1))
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

            new_state = self.swap(self.data.copy(), 0, 3)
            stack = self.state_stack.copy()
            stack.append((0, 3))
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

        elif space_index == 1:
            new_state = self.swap(self.data.copy(), 1, 0)
            stack = self.state_stack.copy()
            stack.append((1, 0))
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

            new_state = self.swap(self.data.copy(), 1, 4)
            stack = self.state_stack.copy()
            stack.append((1, 4))
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

        elif space_index == 2:
            new_state = self.swap(self.data.copy(), 2, 1)
            stack = self.state_stack.copy()
            stack.append((2, 1))
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

            new_state = self.swap(self.data.copy(), 2, 5)
            stack = self.state_stack.copy()
            stack.append((2, 5))
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

        elif space_index == 3:
            new_state = self.swap(self.data.copy(), 3, 0)
            stack = self.state_stack.copy()
            stack.append((3, 0))
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

            new_state = self.swap(self.data.copy(), 3, 4)
            stack = self.state_stack.copy()
            stack.append((3, 4))
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

            new_state = self.swap(self.data.copy(), 3, 6)
            stack = self.state_stack.copy()
            stack.append((3, 6))
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

        elif space_index == 4:
            new_state = self.swap(self.data.copy(), 4, 1)
            stack = self.state_stack.copy()
            stack.append((4, 1))
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

            new_state = self.swap(self.data.copy(), 4, 5)
            stack = self.state_stack.copy()
            stack.append((4, 5))
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

            new_state = self.swap(self.data.copy(), 4, 3)
            stack = self.state_stack.copy()
            stack.append((4, 3))
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

            new_state = self.swap(self.data.copy(), 4, 7)
            stack = self.state_stack.copy()
            stack.append((4, 7))
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

        elif space_index == 5:
            new_state = self.swap(self.data.copy(), 5, 2)
            stack = self.state_stack.copy()
            stack.append((5, 2))
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

            new_state = self.swap(self.data.copy(), 5, 4)
            stack = self.state_stack.copy()
            stack.append((5, 4))
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

            new_state = self.swap(self.data.copy(), 5, 8)
            stack = self.state_stack.copy()
            stack.append((5, 8))
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

        elif space_index == 6:
            new_state = self.swap(self.data.copy(), 6, 3)
            stack = self.state_stack.copy()
            stack.append((6, 3))
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

            new_state = self.swap(self.data.copy(), 6, 7)
            stack = self.state_stack.copy()
            stack.append((6, 7))
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

        elif space_index == 7:
            new_state = self.swap(self.data.copy(), 7, 4)
            stack = self.state_stack.copy()
            stack.append((7, 4))
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

            new_state = self.swap(self.data.copy(), 7, 6)
            stack = self.state_stack.copy()
            stack.append((7, 6))
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

            new_state = self.swap(self.data.copy(), 7, 8)
            stack = self.state_stack.copy()
            stack.append((7, 8))
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

        elif space_index == 8:
            new_state = self.swap(self.data.copy(), 8, 5)
            stack = self.state_stack.copy()
            stack.append((8, 5))
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

            new_state = self.swap(self.data.copy(), 8, 7)
            stack = self.state_stack.copy()
            stack.append((8, 7))
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

        return possible_states

    def swap(self, _list, to, _from):
        _list[to], _list[_from] = _list[_from], _list[to]
        return _list
