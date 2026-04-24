import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QPushButton, QCheckBox, QWidget, QVBoxLayout, QRadioButton, QButtonGroup, QLineEdit,
                             QHBoxLayout, QComboBox, QGroupBox, QTextEdit)
from   PyQt5.QtGui     import QIcon, QFont
from PyQt5.QtCore import Qt, QThread
from   PyQt5.QtGui     import QPixmap

from constants import UICONSTANTS
from Worker import Worker

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.backend_thread = QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.backend_thread)

        self.initUI()

        self.encrypt_button.clicked.connect(self.algo_picker)
        self.decrypt_button.clicked.connect(self.algo_picker)
        self.bruteforce_button.clicked.connect(self.algo_picker)
        self.drop_down_menu.currentIndexChanged.connect(self.algo_picker)

    def algo_picker(self):
        algo = self.drop_down_menu.currentData()
        self.worker.input = self.input_bar.toPlainText()
        self.worker.key   = self.key_bar.text()

        match algo:
            case 1:
                self.key_bar.setPlaceholderText("Enter a key (0 -> 25):")
                self.bruteforce_button.setEnabled(True)
                self.encrypt_button.clicked.connect(self.ceaser_encrypt)
                self.decrypt_button.clicked.connect(self.ceaser_decrypt)
                self.bruteforce_button.clicked.connect(self.ceaser_bruteforce)

            case 2:
                self.key_bar.setPlaceholderText("Enter a keyword:")
                self.bruteforce_button.setEnabled(False)
                self.encrypt_button.clicked.connect(self.mono_encrypt)
                self.decrypt_button.clicked.connect(self.mono_decrypt)

    def ceaser_encrypt(self):
        cipher = self.worker.Ceaser_Encrypt()
        self.output_bar.setText(cipher)

    def ceaser_decrypt(self):
        plain = self.worker.Ceaser_Decrypt()
        self.output_bar.setText(plain)

    def ceaser_bruteforce(self):
        out = ""
        for k in range(25):
            self.worker.key = k
            out += f"\n[{k}] {self.worker.Ceaser_Decrypt()}\n"
            out += "---------------------------------"
        self.output_bar.setText(out)

    def mono_encrypt(self):
        cipher = self.worker.Mono_Encrypt()
        self.output_bar.setText(cipher)

    def mono_decrypt(self):
        plain = self.worker.Mono_Decrypt()
        self.output_bar.setText(plain)

    def initUI(self):
        #window setup
        self.setWindowTitle("Cipher Tool")
        self.setFixedSize(UICONSTANTS.WINOW_WIDTH,UICONSTANTS.WINOW_HEIGHT)
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
        self.input_bar = QTextEdit()
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
        self.drop_down_menu.addItem("Ceaser Cipher", 1)
        self.drop_down_menu.addItem("Monoalphabetic Cipher", 2)

        #key_bar
        self.key_bar = QLineEdit()
        self.key_bar.setPlaceholderText("Enter a key (0 -> 25)")

        #encrypt button
        self.encrypt_button = QPushButton("Encrypt")

        #decrypt button
        self.decrypt_button = QPushButton("Decrypt")

        #bruteforce button
        self.bruteforce_button = QPushButton("Bruteforce")

        #middle layout
        self.middle_layout = QVBoxLayout()
        self.middle_layout.addWidget(self.drop_down_menu)
        self.middle_layout.addWidget(self.key_bar)
        self.middle_layout.addWidget(self.encrypt_button)
        self.middle_layout.addWidget(self.decrypt_button)
        self.middle_layout.addWidget(self.bruteforce_button)

        # middle group box
        self.middle_group = QGroupBox("Operations")
        self.middle_group.setLayout(self.middle_layout)
        self.main_layout.addWidget(self.middle_group)

    def draw_right_column(self):
        # output bar
        self.output_bar = QTextEdit()
        self.output_bar.setReadOnly(True)
        self.output_bar.setFixedSize(int(UICONSTANTS.WINOW_WIDTH / 3), UICONSTANTS.WINOW_HEIGHT - 100)

        #right layout
        self.right_layout = QVBoxLayout()
        self.right_layout.addWidget(self.output_bar)

        # right group box
        self.right_group = QGroupBox("Output")
        self.right_group.setLayout(self.right_layout)
        self.main_layout.addWidget(self.right_group)