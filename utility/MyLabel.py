import sys

from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QDrag, QPixmap, QPainter, QColor
from PyQt5.QtCore import QMimeData, Qt, QPropertyAnimation, QRect, QVariantAnimation


class DraggableDroppableLabel(QLabel):

    def __init__(self, widget_type):
        super().__init__(widget_type)

        # self.animation = QPropertyAnimation(self, b'color')
        # self.animation.setDuration(1000)
        # self.animation.setLoopCount(2)
        # self.animation.setStartValue(QColor(0, 0, 0))
        # self.animation.setEndValue(QColor(250, 250, 250))

        # self.anim = QPropertyAnimation(self, b"geometry")
        # self.anim.setDuration(10000)
        # self.anim.setStartValue(QRect(150, 30, 100, 100))
        # self.anim.setEndValue(QRect(150, 30, 200, 200))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.pos()
            self.setAcceptDrops(True)

    def mouseMoveEvent(self, event):
        if not (event.buttons() & Qt.LeftButton):
            return
        if (event.pos() - self.drag_start_position).manhattanLength() < QApplication.startDragDistance():
            return
        drag = QDrag(self)
        mimedata = QMimeData()
        mimedata.setText(self.text())
        drag.setMimeData(mimedata)
        pixmap = QPixmap(self.size())
        painter = QPainter(pixmap)
        painter.drawPixmap(self.rect(), self.grab())
        painter.end()
        drag.setPixmap(pixmap)
        drag.setHotSpot(event.pos())
        drag.exec_(Qt.MoveAction)

    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.acceptProposedAction()
            # print(event.mimeData().text())

    def dropEvent(self, event):
        old_text = self.text()
        # print(type(event))
        # swapping label values
        source = event.source()
        # print("OLD Text : " + old_text)
        pos = event.pos()
        # print(pos)
        text = event.mimeData().text()
        # print("New text :" + text)
        self.setText(text)

        source.setText(old_text)

        event.acceptProposedAction()
