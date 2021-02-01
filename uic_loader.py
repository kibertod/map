import sys

from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel


class MyWidget(QMainWindow):
    # map_visualisation - это QLabel для отрисовки QPixmap
    def __init__(self, map):
        super().__init__()
        uic.loadUi('data/main.ui', self)
        self.set_image_file(map.load())
        self.map = map

    def set_image_bytes(self, image_data):
        payload = QtCore.QByteArray(image_data)
        pixmap = QPixmap()
        pixmap.loadFromData(payload, "PNG")

    def set_image_file(self, image_data):
        with open("map.jpg", "wb") as file:
            file.write(image_data)
        pixmap = QPixmap("map.jpg")
        self.map_visualisation.setPixmap(pixmap)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp:
            self.map.update(zoom=self.map.zoom + 1)
            self.set_image_file(self.map.load())
        
        elif event.key() == Qt.Key_PageDown:
            self.map.update(zoom=self.map.zoom - 1)
            self.set_image_file(self.map.load())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
