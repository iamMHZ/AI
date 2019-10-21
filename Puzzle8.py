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

    def expand(self, state):
        array = np.array(state)

        array = np.reshape(array, (3, 3))

        # we assume that the 0 in list is the blank space
        space_index = np.where(array == 0)
        print(space_index)
