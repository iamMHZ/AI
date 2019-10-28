# ♥
from PyQt5.QtWidgets import QFileDialog
from view.ui import Ui_MainWindow
from anytree import RenderTree
from anytree.exporter import DotExporter
import qdarkstyle
import random
from ImageProcessor.ImageProcessor import image_parser, load_image, show_image
from model.Search import Search
from model.Puzzle8 import Puzzle8
from model.Utility import printer
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import QtWidgets


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


class Window(QtWidgets.QMainWindow):

    def __init__(self, ):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        item_list = ["BFS", "DFS", "UCS", "A*", "IDS", "IDA*"]
        self.ui.comboBox.addItems(item_list)

        self.current_algorithm = self.ui.comboBox.currentText()
        # self.start_puzzle_date = self.get_random_list()
        self.start_puzzle_date = [2, 0, 4, 1, 5, 3, 7, 8, 6]

        # put labels together for better control
        self.labels = []
        self.labels.append(self.ui.label1)
        self.labels.append(self.ui.label2)
        self.labels.append(self.ui.label3)
        self.labels.append(self.ui.label4)
        self.labels.append(self.ui.label5)
        self.labels.append(self.ui.label6)
        self.labels.append(self.ui.label7)
        self.labels.append(self.ui.label8)
        self.labels.append(self.ui.label9)

        self.set_labels_text(self.start_puzzle_date)

        # event handling
        self.ui.loadImageBtn.clicked.connect(self.getfile)
        self.ui.randomBrn.clicked.connect(self.start_randomly)
        self.ui.startBtn.clicked.connect(self.start)
        self.ui.endBtn.clicked.connect(self.end)

        # self.ui.comboBox.currentIndexChanged.connect(self.combobox_changed)

        # if you don't put [str] it return the index of combobox selected item
        self.ui.comboBox.activated[str].connect(self.combobox_changed)

        # initialize threads
        # algorithm threads
        self.algorithm_thread = AlgorithmThread(Puzzle8(self.start_puzzle_date))
        self.algorithm_thread.signal.connect(self.on_received)
        # Image thread:
        self.image_thread = ImageThread(self.current_algorithm)
        self.image_thread.signal.connect(self.on_tree_recived)

    def combobox_changed(self, text):
        self.current_algorithm = text
        # updating ui in case of ruing algorithms continuously
        self.set_labels_text(self.start_puzzle_date)

    def start_randomly(self):
        random_list = self.get_random_list()
        self.start_puzzle_date = random_list
        self.set_labels_text(random_list)

    def getfile(self):
        file = QFileDialog.getOpenFileName(None, 'Open file', '../ImageProcessor/', "Image files (*.jpg *.png)")

        path = file[0]
        # checking if image path is valid
        if len(path) > 0:
            print(file)

            # load image:
            number_list = image_parser(path)
            print(number_list)

            self.start_puzzle_date = number_list
            self.set_labels_text(number_list)

    def get_random_list(self):
        random_list = random.sample(range(0, 9), 9)

        return random_list

    def set_labels_text(self, number_list):
        for i, label in enumerate(self.labels):
            label.setText(str(number_list[i]))

    def start(self):
        puzzle = Puzzle8(self.start_puzzle_date)
        print(self.current_algorithm)

        # Terminate threads that may run
        self.algorithm_thread.terminate()
        self.image_thread.terminate()

        self.algorithm_thread.set_algorithm_type(self.current_algorithm)
        self.algorithm_thread.set_puzzle(puzzle)
        if self.current_algorithm == 'BFS':
            self.algorithm_thread.start()

        elif self.current_algorithm == 'DFS':
            # self.process = Process(target=self.search.dfs, args=(puzzle,))
            # self.process.start()

            self.algorithm_thread.start()

        elif self.current_algorithm == 'UCS':
            self.algorithm_thread.start()

        elif self.current_algorithm == 'A*':
            self.algorithm_thread.start()

        elif self.current_algorithm == 'IDS':
            self.algorithm_thread.start()

        elif self.current_algorithm == 'IDA*':
            self.algorithm_thread.start()

    def end(self):
        self.algorithm_thread.terminate()
        self.image_thread.terminate()

    def set_label_when_find_goal(self, stack):
        for item in stack:
            index0 = item[0]
            index1 = item[1]
            data1 = self.labels[index0].text()
            data2 = self.labels[index1].text()
            self.labels[index0].setText(data2)
            self.labels[index1].setText(data1)

    def show_tree_to_text(self, tree):
        text = ""
        for pre, fill, node in RenderTree(tree):
            text += ("%s%s\n" % (pre, printer(str(node.name))))

        self.ui.textEdit.setText(text)

    def on_received(self, item):
        tree = item[1]
        self.image_thread.set_algorithm_name(self.current_algorithm)
        self.image_thread.set_tree(tree)
        self.image_thread.start()

        self.show_tree_to_text(tree)
        self.set_label_when_find_goal(item[0].state_stack)

    def on_tree_recived(self, path):
        image = load_image(path)
        show_image(self.current_algorithm, image, 0)


def main():
    app = QtWidgets.QApplication([])
    window = Window()
    window.show()

    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()


if __name__ == "__main__":
    main()
