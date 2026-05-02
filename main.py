from PyQt5.QtWidgets import QApplication

from app import MainWindow
from constants import resource_path
import sys


def main():
    app = QApplication(sys.argv)

    with open(resource_path('assets/style.qss'), 'r') as f:
        app.setStyleSheet(f.read())

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()