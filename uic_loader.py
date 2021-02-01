import sys

from PyQt5 import uic
from PyQt5.QtCore import QByteArray
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('data/main.ui', self)

    def set_image(self, image_data):
        payload = QByteArray(image_data)
        pixmap = QPixmap()
        pixmap.loadFromData(payload)
        self.map_visualisation.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
