from PyQt5.QtWidgets import QApplication

from constants import resource_path
from ui import MainWindow
import sys


def main():
    app = QApplication(sys.argv)

    with open(resource_path('assets/style.css'), 'r') as f:
        app.setStyleSheet(f.read())

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()