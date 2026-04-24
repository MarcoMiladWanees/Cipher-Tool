from PyQt5.QtWidgets import QApplication
from ui import MainWindow
import sys


def main():
    app = QApplication(sys.argv)

    with open(r"D:\PyCharm 2025.3.3\Projects\Cipher-Tool\assets\style.css", "r") as file:
        app.setStyleSheet(file.read())

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()