import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QPushButton, QCheckBox, QWidget, QVBoxLayout, QRadioButton, QButtonGroup, QLineEdit,
                             QHBoxLayout, QComboBox, QGroupBox)
from   PyQt5.QtGui     import QIcon, QFont
from   PyQt5.QtCore    import Qt
from   PyQt5.QtGui     import QPixmap

from constants import UICONSTANTS

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #window setup
        self.setWindowTitle("Cipher Tool")
        self.setFixedSize(UICONSTANTS.WINOW_WIDTH,UICONSTANTS.WINOW_HEIGHT)
        self.setStyleSheet(self.getStyleSheet())
        self.setWindowIcon(QIcon('assets/icon.png'))

        #main layout and widget
        self.main_widget = QWidget()
        self.main_layout = QHBoxLayout(self.main_widget)

        #drawing the three columns
        self.draw_left_column()
        self.draw_middle_column()
        self.draw_right_column()

        self.setCentralWidget(self.main_widget)

    def draw_left_column(self):
        # input bar
        self.input_bar = QLineEdit()
        self.input_bar.setFixedSize(int(UICONSTANTS.WINOW_WIDTH / 3), UICONSTANTS.WINOW_HEIGHT - 100)

        #left layout
        self.left_layout = QVBoxLayout()
        self.left_layout.addWidget(self.input_bar)

        #left group box
        self.left_group = QGroupBox("Input")
        self.left_group.setLayout(self.left_layout)
        self.main_layout.addWidget(self.left_group)

    def draw_middle_column(self):
        # drop_down
        self.drop_down_menu = QComboBox()
        self.drop_down_menu.addItem("Ceaser Cipher")
        self.drop_down_menu.addItem("Monoalphabetic Cipher")

        #encrypt button
        self.encrypt_button = QPushButton("Encrypt")

        #decrypt button
        self.decrypt_button = QPushButton("Decrypt")

        #bruteforce button
        self.bruteforce_button = QPushButton("Bruteforce")

        #middle layout
        self.middle_layout = QVBoxLayout()
        self.middle_layout.addWidget(self.drop_down_menu)
        self.middle_layout.addWidget(self.encrypt_button)
        self.middle_layout.addWidget(self.decrypt_button)
        self.middle_layout.addWidget(self.bruteforce_button)

        # middle group box
        self.middle_group = QGroupBox("Operations")
        self.middle_group.setLayout(self.middle_layout)
        self.main_layout.addWidget(self.middle_group)

    def draw_right_column(self):
        # output bar
        self.output_bar = QLineEdit()
        self.output_bar.setReadOnly(True)
        self.output_bar.setFixedSize(int(UICONSTANTS.WINOW_WIDTH / 3), UICONSTANTS.WINOW_HEIGHT - 100)

        #right layout
        self.right_layout = QVBoxLayout()
        self.right_layout.addWidget(self.output_bar)

        # right group box
        self.right_group = QGroupBox("Output")
        self.right_group.setLayout(self.right_layout)
        self.main_layout.addWidget(self.right_group)

    def getStyleSheet(self):
        return """ """
