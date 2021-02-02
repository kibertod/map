import sys

from uic_loader import MyWidget
from map import Map

from PyQt5.QtWidgets import QApplication


def main():
	zoom = 13
	app = QApplication(sys.argv)
	ex = MyWidget()
	ex.set_map(Map([37.620070, 55.753630], [450, 450], ex.get_map_type(), 5))
	ex.show()
	sys.exit(app.exec_())


if __name__ == '__main__':
    main()
