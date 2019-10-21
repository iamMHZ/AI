import numpy as np


# it is class puzzle8


class Puzzle8:

    def __init__(self, data):
        self.data = data

    # def getData(self):
    #     return self.data

    def is_goal(self, state):
        goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        return state == goal

    def swap(self, list, to, _from):
        list[to], list[_from] = list[_from], list[to]

        return list

    def expand(self, state):
        # taking a copy of current state of this 8-puzzle
        list_copy = state.copy()

        possible_states = list()

        # we assume that 0 is our blank space in puzzle
        space_index = state.index(0)

        if space_index == 0:

            new_state = self.swap(list_copy, 0, 1)
            possible_states.append(new_state)
            new_state = self.swap(list_copy, 0, 3)
            possible_states.append(new_state)

            print(possible_states)
            print(state)

        elif space_index == 1:
            new_state = self.swap(list_copy, 1, 0)
            possible_states.append(new_state)
            new_state = self.swap(list_copy, 1, 4)
            possible_states.append(new_state)
        elif space_index == 2:
            new_state = self.swap(list_copy, 2, 1)
            possible_states.append(new_state)
            new_state = self.swap(list_copy, 2, 5)
            possible_states.append(new_state)

        elif space_index == 3:
            new_state = self.swap(list_copy, 3, 0)
            possible_states.append(new_state)
            new_state = self.swap(list_copy, 3, 4)
            possible_states.append(new_state)
            new_state = self.swap(list_copy, 3, 6)
            possible_states.append(new_state)

        elif space_index == 4:
            new_state = self.swap(list_copy, 4, 1)
            possible_states.append(new_state)
            new_state = self.swap(list_copy, 4, 5)
            possible_states.append(new_state)
            new_state = self.swap(list_copy, 4, 3)
            possible_states.append(new_state)
            new_state = self.swap(list_copy, 4, 7)
            possible_states.append(new_state)

        elif space_index == 5:
            new_state = self.swap(list_copy, 5, 2)
            possible_states.append(new_state)
            new_state = self.swap(list_copy, 5, 4)
            possible_states.append(new_state)
            new_state = self.swap(list_copy, 5, 8)
            possible_states.append(new_state)

        elif space_index == 6:
            new_state = self.swap(list_copy, 6, 3)
            possible_states.append(new_state)
            new_state = self.swap(list_copy, 6, 7)
            possible_states.append(new_state)

        elif space_index == 7:
            new_state = self.swap(list_copy, 7, 4)
            possible_states.append(new_state)
            new_state = self.swap(list_copy, 7, 6)
            possible_states.append(new_state)
            new_state = self.swap(list_copy, 7, 8)
            possible_states.append(new_state)

        elif space_index == 8:
            new_state = self.swap(list_copy, 8, 5)
            possible_states.append(new_state)
            new_state = self.swap(list_copy, 8, 7)
            possible_states.append(new_state)

        return possible_states
