import cv2
import threading
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap, QImage
from view.ui import Ui_MainWindow

import sys
import qdarkstyle
import qimage2ndarray
import multiprocessing
from multiprocessing import Process


class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


def main():
    app = QtWidgets.QApplication([])
    window = Window()
    window.show()

    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()


if __name__ == "__main__":
    main()
