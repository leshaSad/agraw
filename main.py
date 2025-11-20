import sys
from PyQt6.QtGui import QPainter, QColor, QPolygonF
from PyQt6.QtCore import Qt, QRectF, QPointF
from PyQt6.QtWidgets import QWidget, QApplication
from random import randint
from PyQt6 import uic


class Suprematism(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.run)
        self.do_paint = False
        self.x, self.y = -100, -100
        self.fig = 0
        self.setMouseTracking(True)

