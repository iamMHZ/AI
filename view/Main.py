import threading
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap, QImage
from view.ui import Ui_MainWindow

import qdarkstyle

import random
from ImageProcessor.ImageProcessor import image_parser
from model.Search import Search
from model.Puzzle8 import Puzzle8
from multiprocessing.pool import ThreadPool
from multiprocessing import Process


# ♥
class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.search = Search()
        self.process = None

        item_list = ["BFS", "DFS", "UCS", "A*", "IDS", "IDA*"]
        self.ui.comboBox.addItems(item_list)

        self.current_algorithm = self.ui.comboBox.currentText()
        self.start_puzzle_date = self.get_random_list()

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

    def combobox_changed(self, text):
        self.current_algorithm = text

    def start_randomly(self):
        random_list = self.get_random_list()
        self.start_puzzle_date = random_list
        print(random_list)
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
        if self.current_algorithm == 'BFS':

            self.process = Process(target=self.search.bfs, args=(puzzle,))
            self.process.start()

        elif self.current_algorithm == 'DFS':
            self.process = Process(target=self.search.dfs, args=(puzzle,))
            self.process.start()
        elif self.current_algorithm == 'UCS':
            self.process = Process(target=self.search.ucs, args=(puzzle,))
            self.process.start()
        elif self.current_algorithm == 'A*':
            self.process = Process(target=self.search.a_star, args=(puzzle,))
            self.process.start()
        elif self.current_algorithm == 'IDS':
            self.process = Process(target=self.search.ids, args=(puzzle,))
            self.process.start()
        elif self.current_algorithm == 'IDA*':
            self.process = Process(target=self.search.ida_star, args=(puzzle,))
            self.process.start()

    def end(self):
        if self.process:
            self.process.terminate()
            # deleting process from memory
            del self.process


def main():
    app = QtWidgets.QApplication([])
    window = Window()
    window.show()

    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()


if __name__ == "__main__":
    main()
