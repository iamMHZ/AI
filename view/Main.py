import cv2
import threading
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap, QImage
from view.ui import Ui_MainWindow

import sys
import qdarkstyle
import qimage2ndarray
import multiprocessing
from multiprocessing import Process
import random
from ImageProcessor.ImageProcessor import image_parser, load_image


# ♥
class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

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

        # event handling
        self.ui.loadImageBtn.clicked.connect(self.getfile)
        self.ui.randomBrn.clicked.connect(self.start_randomly)

    def start_randomly(self):
        random_list = self.get_random_list()
        print(random_list)
        self.set_labels_text(random_list)

    def getfile(self):
        file = QFileDialog.getOpenFileName(None, 'Open file', '../ImageProcessor/', "Image files (*.jpg *.png)")

        # checking if loaded an image
        if len(file[0]) > 0:
            print(file)
            path = file[0]

            # load image:
            number_list = image_parser(path)
            print(number_list)

            self.set_labels_text(number_list)

    def get_random_list(self):
        random_list = random.sample(range(0, 9), 9)

        return random_list

    def set_labels_text(self, number_list):
        for i, label in enumerate(self.labels):
            label.setText(str(number_list[i]))


def main():
    app = QtWidgets.QApplication([])
    window = Window()
    window.show()

    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()


if __name__ == "__main__":
    main()
