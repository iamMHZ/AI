import numpy as np


# it is class puzzle8


class Puzzle8:
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    def __init__(self):
        self.data = list()

    # def getData(self):
    #     return self.data

    def is_goal(self, state):
        return state == Puzzle8.goal

    def expand(self, state):
        array = np.array(state)

        array = np.reshape(array, 3, 3)

        print(array)
        print(array[0][0])
