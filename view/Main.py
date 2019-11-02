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
from utility.Utility import printer
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import QtWidgets
from utility.Thread import ImageThread, AlgorithmThread
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QPropertyAnimation
import time


class Window(QtWidgets.QMainWindow):

    def update_after_drag(self):

        new_list = []
        for label in self.labels:
            text = label.text()
            new_list.append(int(text))

        self.start_puzzle_date = new_list
        print(new_list)

    def __init__(self, ):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        item_list = ["BFS", "DFS", "UCS", "A*", "IDS", "IDA*"]
        self.ui.comboBox.addItems(item_list)

        self.current_algorithm = self.ui.comboBox.currentText()
        # self.start_puzzle_date = self.get_random_list()
        self.start_puzzle_date = [1, 2, 3, 4, 5, 6, 7, 0, 8]

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
        file = QFileDialog.getOpenFileName(None, 'Open file', '../ImageProcessor/imageTemplates/',
                                           "Image files (*.jpg *.png)")

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
        self.update_after_drag()

        puzzle = Puzzle8(self.start_puzzle_date)
        print(self.current_algorithm)

        # Terminate threads that may run
        self.algorithm_thread.terminate()
        self.image_thread.terminate()

        self.algorithm_thread.set_algorithm_type(self.current_algorithm)
        self.algorithm_thread.set_puzzle(puzzle)
        self.algorithm_thread.start()

    def end(self):
        self.algorithm_thread.terminate()
        self.image_thread.terminate()

    def set_label_when_find_goal(self, stack):
        for item in stack:
            index0 = item[0]
            index1 = item[1]

            # self.labels[index0].animation.start()
            # self.labels[index1].animation.start()

            data1 = self.labels[index0].text()
            data2 = self.labels[index1].text()

            self.labels[index0].setText(data2)
            self.labels[index1].setText(data1)
            # time.sleep(1)

    def show_tree_to_text(self, tree):
        text = ""
        for pre, fill, node in RenderTree(tree):
            text += ("%s%s\n" % (pre, printer(str(node.name))))

        self.ui.textLabel.setText(text)

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
