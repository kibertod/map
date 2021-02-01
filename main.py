import sys

from uic_loader import MyWidget
from map import Map

from PyQt5.QtWidgets import QApplication


def main():
    app = QApplication(sys.argv)
    ex = MyWidget()

    map = Map(['37.620070', '55.753630'], [450, 450], "map")

    with open("map.jpg", "wb") as file:
    	file.write(map.load())


    ex.set_image_file("map.jpg")
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
