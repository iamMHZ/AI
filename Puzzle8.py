import numpy as np
import queue


# it is class puzzle8


class Puzzle8:

    def __init__(self, data):
        self.data = data
        self.state_stack = queue.LifoQueue()

    # def getData(self):
    #     return self.data
    @staticmethod
    def is_goal(puzzle):
        goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        return puzzle.data == goal

    def swap(self, _list, to, _from):
        _list[to], _list[_from] = _list[_from], _list[to]

        return _list

    def expand(self):
        # taking a copy of current state of this 8-puzzle
        list_copy = self.data.copy()

        possible_states = list()

        # we assume that 0 is our blank space in puzzle
        space_index = list_copy.index(0)

        if space_index == 0:

            new_state = self.swap(list_copy, 0, 1)
            puzzle = Puzzle8(new_state)
            possible_states.append(puzzle)
            new_state = self.swap(list_copy, 0, 3)
            puzzle = Puzzle8(new_state)
            possible_states.append(puzzle)

        elif space_index == 1:
            new_state = self.swap(list_copy, 1, 0)
            puzzle = Puzzle8(new_state)
            possible_states.append(puzzle)
            new_state = self.swap(list_copy, 1, 4)
            puzzle = Puzzle8(new_state)
            possible_states.append(puzzle)
        elif space_index == 2:
            new_state = self.swap(list_copy, 2, 1)
            puzzle = Puzzle8(new_state)
            possible_states.append(puzzle)
            new_state = self.swap(list_copy, 2, 5)
            puzzle = Puzzle8(new_state)
            possible_states.append(puzzle)

        elif space_index == 3:
            new_state = self.swap(list_copy, 3, 0)
            puzzle = Puzzle8(new_state)
            possible_states.append(puzzle)
            new_state = self.swap(list_copy, 3, 4)
            puzzle = Puzzle8(new_state)
            possible_states.append(puzzle)
            new_state = self.swap(list_copy, 3, 6)
            puzzle = Puzzle8(new_state)
            possible_states.append(puzzle)

        elif space_index == 4:
            new_state = self.swap(list_copy, 4, 1)
            puzzle = Puzzle8(new_state)
            possible_states.append(puzzle)
            new_state = self.swap(list_copy, 4, 5)
            puzzle = Puzzle8(new_state)
            possible_states.append(puzzle)
            new_state = self.swap(list_copy, 4, 3)
            puzzle = Puzzle8(new_state)
            possible_states.append(puzzle)
            new_state = self.swap(list_copy, 4, 7)
            puzzle = Puzzle8(new_state)
            possible_states.append(puzzle)

        elif space_index == 5:
            new_state = self.swap(list_copy, 5, 2)
            puzzle = Puzzle8(new_state)
            possible_states.append(puzzle)
            new_state = self.swap(list_copy, 5, 4)
            puzzle = Puzzle8(new_state)
            possible_states.append(puzzle)
            new_state = self.swap(list_copy, 5, 8)
            puzzle = Puzzle8(new_state)
            possible_states.append(puzzle)

        elif space_index == 6:
            new_state = self.swap(list_copy, 6, 3)
            puzzle = Puzzle8(new_state)
            possible_states.append(puzzle)
            new_state = self.swap(list_copy, 6, 7)
            puzzle = Puzzle8(new_state)
            possible_states.append(puzzle)

        elif space_index == 7:
            new_state = self.swap(list_copy, 7, 4)
            puzzle = Puzzle8(new_state)
            possible_states.append(puzzle)
            new_state = self.swap(list_copy, 7, 6)
            puzzle = Puzzle8(new_state)
            possible_states.append(puzzle)
            new_state = self.swap(list_copy, 7, 8)
            puzzle = Puzzle8(new_state)
            possible_states.append(puzzle)

        elif space_index == 8:
            new_state = self.swap(list_copy, 8, 5)
            puzzle = Puzzle8(new_state)
            possible_states.append(puzzle)
            new_state = self.swap(list_copy, 8, 7)
            puzzle = Puzzle8(new_state)
            possible_states.append(puzzle)

        return possible_states
