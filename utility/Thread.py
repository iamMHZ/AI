from PyQt5.QtCore import QThread, pyqtSignal, Qt
from anytree.exporter import DotExporter
from model.Search import Search


# using this class for creating tree image
class ImageThread(QThread):
    signal = pyqtSignal('PyQt_PyObject')

    def __init__(self, algorithm_name, tree=None):
        QThread.__init__(self)
        self.algorithm_name = algorithm_name
        self.tree = tree

    def set_tree(self, tree):
        self.tree = tree

    def set_algorithm_name(self, algorithm_name):
        self.algorithm_name = algorithm_name

    def run(self):
        # checking if we have * in names
        if self.algorithm_name[-1] == '*':
            path = "./treeImages/" + str(self.algorithm_name[0:-1]) + " tree.png"
        else:
            path = "./treeImages/" + str(self.algorithm_name) + " tree.png"
        DotExporter(self.tree).to_picture(path)
        self.signal.emit(path)


class AlgorithmThread(QThread):
    signal = pyqtSignal('PyQt_PyObject')

    def __init__(self, puzzle):
        QThread.__init__(self)
        self.algorithm = "BFS"
        self.search = Search()
        self.puzzle = puzzle

    def set_algorithm_type(self, new_algorithm):
        self.algorithm = new_algorithm

    def set_puzzle(self, puzzle):
        self.puzzle = puzzle

    def run(self):
        if self.algorithm == "BFS":
            result = self.search.bfs(self.puzzle)
            self.signal.emit(result)
        elif self.algorithm == "DFS":
            result = self.search.dfs(self.puzzle)
            self.signal.emit(result)

        elif self.algorithm == "UCS":
            result = self.search.ucs(self.puzzle)
            self.signal.emit(result)

        elif self.algorithm == "A*":
            result = self.search.a_star(self.puzzle)
            self.signal.emit(result)

        elif self.algorithm == "IDS":
            result = self.search.ids(self.puzzle)
            self.signal.emit(result)

        elif self.algorithm == "IDA*":
            result = self.search.ida_star(self.puzzle)
            self.signal.emit(result)
