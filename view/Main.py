# ♥
import threading

from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap, QImage
from view.ui import Ui_MainWindow

import qdarkstyle

import random
from ImageProcessor.ImageProcessor import image_parser
from model.Search import Search
from model.Puzzle8 import Puzzle8
from multiprocessing.pool import ThreadPool
from multiprocessing import Process, Queue
from concurrent.futures import ThreadPoolExecutor
from interface import implements
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QPushButton


class ThreadHandler(QThread):
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
        self.search = Search()
        self.process = None
        self.pool = ThreadPool(processes=1)
        self.result = []

        item_list = ["BFS", "DFS", "UCS", "A*", "IDS", "IDA*"]
        self.ui.comboBox.addItems(item_list)

        self.current_algorithm = self.ui.comboBox.currentText()
        # self.start_puzzle_date = self.get_random_list()
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

        self.qThread = ThreadHandler(Puzzle8(self.start_puzzle_date))
        self.qThread.signal.connect(self.on_received)

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

    def on_received(self, item):
        print()
        print("DONE")

    def start(self):
        puzzle = Puzzle8(self.start_puzzle_date)
        print(self.current_algorithm)

        queue = Queue()

        self.qThread.terminate()

        self.qThread.set_algorithm_type(self.current_algorithm)
        self.qThread.set_puzzle(puzzle)
        if self.current_algorithm == 'BFS':

            # self.process = Process(target=self.search.bfs, args=(puzzle,))
            # self.process.start()

            # apply_async = self.pool.apply_async(target=self.search.dfs, args=(puzzle,))
            # puzzle = apply_async.get()

            # executor = ThreadPoolExecutor(2)
            # future = executor.submit(self.search.bfs, (puzzle,))
            # print(future.done())
            # print(future.result())

            # qThread = ThreadHandler(puzzle)
            # qThread.signal.connect(self.on_received)

            self.qThread.start()

        elif self.current_algorithm == 'DFS':
            # self.process = Process(target=self.search.dfs, args=(puzzle,))
            # self.process.start()

            self.qThread.start()

        elif self.current_algorithm == 'UCS':
            # self.process = Process(target=self.search.ucs, args=(puzzle,))
            # self.process.start()

            self.qThread.start()

        elif self.current_algorithm == 'A*':
            # self.process = Process(target=self.search.a_star, args=(puzzle,))
            # self.process.start()

            self.qThread.start()

        elif self.current_algorithm == 'IDS':
            # self.process = Process(target=self.search.ids, args=(puzzle,))
            # self.process.start()

            self.qThread.start()

        elif self.current_algorithm == 'IDA*':
            # self.process = Process(target=self.search.ida_star, args=(puzzle,))
            # self.process.start()

            self.qThread.start()

    def end(self):
        # if self.process:
        #     self.process.terminate()
        #     # self.pool.close()
        #     # deleting process from memory
        #     del self.process

        self.qThread.terminate()


def main():
    app = QtWidgets.QApplication([])
    window = Window()
    window.show()

    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()


if __name__ == "__main__":
    main()
