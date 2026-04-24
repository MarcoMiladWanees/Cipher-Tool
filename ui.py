import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QPushButton, QCheckBox, QWidget, QVBoxLayout, QRadioButton, QButtonGroup, QLineEdit,
                             QHBoxLayout, QComboBox, QGroupBox, QTextEdit)
from   PyQt5.QtGui     import QIcon, QFont
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from   PyQt5.QtGui     import QPixmap

from constants import UICONSTANTS
from Worker import Worker

class MainWindow(QMainWindow):

    data_signal = pyqtSignal(str, str, int, int)

    def __init__(self):
        super().__init__()
        self.backend_thread = QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.backend_thread)

        #Initializing the UI
        self.initUI()

        self.backend_thread.start()

        self.data_signal.connect(self.worker.router)

        #frontend signals
        self.encrypt_button.clicked.connect(self.send_data)
        self.decrypt_button.clicked.connect(self.send_data)

        #backend signals
        self.worker.done_signal.connect(self.update_output)

    def send_data(self):
        input     = self.input_bar.toPlainText()
        key       = self.key_bar.text()
        algorithm = self.drop_down_menu.currentData()

        if self.sender() == self.encrypt_button:
            mode = 1
        else:
            mode = 2

        self.data_signal.emit(input, key, algorithm, mode)

    def update_output(self, output):
        self.output_bar.clear()
        self.output_bar.setPlainText(output)

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