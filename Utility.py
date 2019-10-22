class Utility:
    # def getData(self):
    #     return self.data
    @staticmethod
    def is_goal(puzzle):
        goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        return puzzle.data == goal
