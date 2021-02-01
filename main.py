import sys

from uic_loader import MyWidget
import map

from PyQt5.QtWidgets import QApplication


def main():
    app = QApplication(sys.argv)
    ex = MyWidget()
    # print(map.test())
    ex.set_image(map.test())
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
