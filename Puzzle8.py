import numpy as np
import queue
from Movement import Movement
from copy import copy


# it is class puzzle8


class Puzzle8:

    def __init__(self, data, state_stack=queue.LifoQueue()):
        self.data = data
        self.state_stack = state_stack

    def __str__(self):
        return str(self.data) + "\n\n"

    def swap(self, _list, to, _from):
        _list[to], _list[_from] = _list[_from], _list[to]
        return _list

    def get_priority(self):
        return self.state_stack.qsize()

    def expand(self):
        # taking a copy of current state of this 8-puzzle

        possible_states = list()

        # we assume that 0 is our blank space in puzzle
        space_index = self.data.copy().index(0)

        if space_index == 0:

            new_state = self.swap(self.data.copy(), 0, 1)
            stack = copy(self.state_stack)
            stack.put(Movement.RIGHT)
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

            new_state = self.swap(self.data.copy(), 0, 3)
            stack = copy(self.state_stack)
            stack.put(Movement.DOWN)
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

        elif space_index == 1:
            new_state = self.swap(self.data.copy(), 1, 0)
            stack = copy(self.state_stack)
            stack.put(Movement.LEFT)
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

            new_state = self.swap(self.data.copy(), 1, 4)
            stack = copy(self.state_stack)
            stack.put(Movement.DOWN)
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

        elif space_index == 2:
            new_state = self.swap(self.data.copy(), 2, 1)
            stack = copy(self.state_stack)
            stack.put(Movement.LEFT)
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

            new_state = self.swap(self.data.copy(), 2, 5)
            stack = copy(self.state_stack)
            stack.put(Movement.DOWN)
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

        elif space_index == 3:
            new_state = self.swap(self.data.copy(), 3, 0)
            stack = copy(self.state_stack)
            stack.put(Movement.UP)
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

            new_state = self.swap(self.data.copy(), 3, 4)
            stack = copy(self.state_stack)
            stack.put(Movement.RIGHT)
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

            new_state = self.swap(self.data.copy(), 3, 6)
            stack = copy(self.state_stack)
            stack.put(Movement.DOWN)
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

        elif space_index == 4:
            new_state = self.swap(self.data.copy(), 4, 1)
            stack = copy(self.state_stack)
            stack.put(Movement.UP)
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

            new_state = self.swap(self.data.copy(), 4, 5)
            stack = copy(self.state_stack)
            stack.put(Movement.RIGHT)
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

            new_state = self.swap(self.data.copy(), 4, 3)
            stack = copy(self.state_stack)
            stack.put(Movement.LEFT)
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

            new_state = self.swap(self.data.copy(), 4, 7)
            stack = copy(self.state_stack)
            stack.put(Movement.DOWN)
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

        elif space_index == 5:
            new_state = self.swap(self.data.copy(), 5, 2)
            stack = copy(self.state_stack)
            stack.put(Movement.UP)
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

            new_state = self.swap(self.data.copy(), 5, 4)
            stack = copy(self.state_stack)
            stack.put(Movement.LEFT)
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

            new_state = self.swap(self.data.copy(), 5, 8)
            stack = copy(self.state_stack)
            stack.put(Movement.DOWN)
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

        elif space_index == 6:
            new_state = self.swap(self.data.copy(), 6, 3)
            stack = copy(self.state_stack)
            stack.put(Movement.UP)
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

            new_state = self.swap(self.data.copy(), 6, 7)
            stack = copy(self.state_stack)
            stack.put(Movement.RIGHT)
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

        elif space_index == 7:
            new_state = self.swap(self.data.copy(), 7, 4)
            stack = copy(self.state_stack)
            stack.put(Movement.UP)
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

            new_state = self.swap(self.data.copy(), 7, 6)
            stack = copy(self.state_stack)
            stack.put(Movement.LEFT)
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

            new_state = self.swap(self.data.copy(), 7, 8)
            stack = copy(self.state_stack)
            stack.put(Movement.RIGHT)
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

        elif space_index == 8:
            new_state = self.swap(self.data.copy(), 8, 5)
            stack = copy(self.state_stack)
            stack.put(Movement.UP)
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

            new_state = self.swap(self.data.copy(), 8, 7)
            stack = copy(self.state_stack)
            stack.put(Movement.LEFT)
            puzzle = Puzzle8(new_state, stack)
            possible_states.append(puzzle)

        return possible_states
