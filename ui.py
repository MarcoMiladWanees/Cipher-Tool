import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QPushButton, QCheckBox, QWidget, QVBoxLayout, QRadioButton, QButtonGroup, QLineEdit,
                             QHBoxLayout, QComboBox, QGroupBox, QTextEdit)
from   PyQt5.QtGui     import QIcon, QFont
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from   PyQt5.QtGui     import QPixmap

from constants import UICONSTANTS, resource_path

class MainWindow(QMainWindow):

    def update_widget_style(self, widget, is_urgent):
        widget.setProperty("urgent", is_urgent)
        widget.style().unpolish(widget)
        widget.style().polish(widget)
        widget.update()

    def handle_errors_send_data(self):
        self.output_bar.clear()
        plain_text = self.input_bar.toPlainText().strip().replace(" ", "")
        key = self.key_bar.text().strip().replace(" ", "")
        algorithm = self.drop_down_menu.currentData()
        flag = False
        key_urgent = False
        input_urgent = False

        match algorithm:
            case 1:
                if not key.isdigit() or not key:
                    key_urgent = True
                if not plain_text.isalpha():
                    input_urgent = True
            case 2 | 3 | 4 | 5 | 6:
                if not key.isalpha() or not key :
                    key_urgent = True
                if not plain_text.isalpha():
                    input_urgent = True
            case 7 :
                if not set(key).issubset({"0" , "1"}) or not key:
                    key_urgent = True
                if not set(plain_text).issubset({"0" , "1"}):
                    input_urgent = True
            case 8:
                if not set(key).issubset({"0" , "1"}):
                    key_urgent = True
                if not set(plain_text).issubset({"0", "1"}):
                    input_urgent = True
                if not key:
                    key_urgent = False
            case 9:
                if not key or not key.isdigit() or not int(key) > 1:
                    key_urgent = True
            case 10:
                if not key or key.isalpha() and key.isdigit():
                    key_urgent = True

        if not plain_text:
            input_urgent = True

        self.update_widget_style(self.key_bar, key_urgent)
        self.update_widget_style(self.input_bar, input_urgent)

    def draw_config_layer(self):
        # drop_down
        self.drop_down_menu = QComboBox()
        self.drop_down_menu.addItem("Ceaser Cipher", 1)
        self.drop_down_menu.addItem("Monoalphabetic Cipher", 2)
        self.drop_down_menu.addItem("Playfair Cipher", 3)
        self.drop_down_menu.addItem("Vigenère Cipher", 4)
        self.drop_down_menu.addItem("Vigenère auto (Plain) key", 5)
        self.drop_down_menu.addItem("Vigenère auto (Cipher) key", 6)
        self.drop_down_menu.addItem("Vernam Cipher", 7)
        self.drop_down_menu.addItem("One time pad Cipher", 8)
        self.drop_down_menu.addItem("Rail Fence Cipher", 9)
        self.drop_down_menu.addItem("Row Transposition Cipher", 10)