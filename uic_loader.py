import sys

from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QCheckBox


class MyWidget(QMainWindow):
    # map_visualisation - это QLabel для отрисовки QPixmap
    def __init__(self):
        super().__init__()
        uic.loadUi('data/main.ui', self)
        self.map = None
        self.map_type = 'Схема'
        self.coords = None, None

        self.cb1.setEnabled(False)
        self.cb1.clicked.connect(self.map_type_changed)
        self.cb2.clicked.connect(self.map_type_changed)
        self.cb3.clicked.connect(self.map_type_changed)
        self.search_btn.clicked.connect(self.find_address)
        # self.clr_btn

    def set_map(self, map_obj):
        self.map = map_obj
        self.set_image(self.map.load())

    def set_image(self, image_data):
        pixmap = QPixmap()
        pixmap.loadFromData(image_data)
        self.map_visualisation.setPixmap(pixmap)

    # def set_image_file(self, image_data):
    #     # with open("map.jpg", "wb") as file:
    #     #     file.write(image_data)
    #     pixmap = QPixmap()
    #     pixmap.loadFromData(image_data)
    #     self.map_visualisation.setPixmap(pixmap)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp:
            self.map.update(zoom=self.map.zoom + 1)
        
        elif event.key() == Qt.Key_PageDown:
            self.map.update(zoom=self.map.zoom - 1)

        elif event.key() == Qt.Key_Left:
            self.map.update(cords=[self.map.cords[0] - 0.00001 * (10 ** (6 - self.map.zoom // 4)),
                                   self.map.cords[1]])

        elif event.key() == Qt.Key_Right:
            self.map.update(cords=[self.map.cords[0] + 0.00001 * (10 ** (6 - self.map.zoom // 4)),
                                   self.map.cords[1]])

        elif event.key() == Qt.Key_Up:
            self.map.update(cords=[self.map.cords[0],
                                   self.map.cords[1] + 0.00001 * (10 ** (6 - self.map.zoom // 4))])

        elif event.key() == Qt.Key_Down:
            self.map.update(cords=[self.map.cords[0],
                                   self.map.cords[1] - 0.00001 * (10 ** (6 - self.map.zoom // 4))])
        self.update_map()

    def map_type_changed(self, state):
        sender_name = self.sender().text()
        if str(sender_name) == self.cb1.text():
            if self.cb2.isChecked():
                self.cb2.toggle()
                self.cb2.setEnabled(True)
            if self.cb3.isChecked():
                self.cb3.toggle()
                self.cb3.setEnabled(True)
            self.cb1.setEnabled(False)

        if str(sender_name) == self.cb2.text():
            if self.cb1.isChecked():
                self.cb1.toggle()
                self.cb1.setEnabled(True)
            if self.cb3.isChecked():
                self.cb3.toggle()
                self.cb3.setEnabled(True)
            self.cb2.setEnabled(False)

        if str(sender_name) == self.cb3.text():
            if self.cb1.isChecked():
                self.cb1.toggle()
                self.cb1.setEnabled(True)
            if self.cb2.isChecked():
                self.cb2.toggle()
                self.cb2.setEnabled(True)
            self.cb3.setEnabled(False)

        self.map_type = sender_name
        self.map.update(layer=self.get_map_type())
        self.update_map()

    def get_map_type(self):
        if self.map_type == 'Схема':
            return 'map'
        elif self.map_type == 'Спутник':
            return 'sat'
        elif self.map_type == 'Гибрид':
            return 'sat,skl'

    def update_map(self):
        # try:
        self.set_image(self.map.load())
        # except Exception:
        #     pass

    def find_address(self):
        address = self.search_str.text()
        self.coords = tuple(map(float, self.map.find(address).split()))
        self.map.update(cords=self.coords)
        self.map.point_func(self.coords)
        self.update_map()

    def clear_points(self):
        self.map.clear_points_func()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
