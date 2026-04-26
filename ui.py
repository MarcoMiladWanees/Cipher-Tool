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
        self.drop_down_menu.currentIndexChanged.connect(self.update_ui)
        self.encrypt_button.clicked.connect(self.handle_errors_send_data)
        self.decrypt_button.clicked.connect(self.handle_errors_send_data)
        self.bruteforce_button.clicked.connect(self.handle_errors_send_data)
        self.input_bar.textChanged.connect(lambda: self.update_widget_style(self.input_bar, False))
        self.key_bar.textChanged.connect(lambda: self.update_widget_style(self.key_bar, False))

        #backend signals
        self.worker.done_signal.connect(self.update_output)

    def update_ui(self):
        self.input_bar.clear()
        self.output_bar.clear()
        self.key_bar.clear()
        self.update_widget_style(self.input_bar, False)
        self.update_widget_style(self.key_bar, False)

        algo = self.drop_down_menu.currentData()
        match algo:
            case 1:
                self.bruteforce_button.show()
                self.key_bar.setPlaceholderText("Enter a key (0 -> 25)")
            case 2 | 3 | 4 | 5 | 6:
                self.bruteforce_button.hide()
                self.key_bar.setPlaceholderText("Enter a keyword...")

    def update_widget_style(self, widget, is_urgent):
        widget.setProperty("urgent", is_urgent)
        widget.style().unpolish(widget)
        widget.style().polish(widget)
        widget.update()

    def handle_errors_send_data(self):
        self.output_bar.clear()
        plain_text = self.input_bar.toPlainText()
        key = self.key_bar.text()
        algorithm = self.drop_down_menu.currentData()
        flag = False
        key_urgent = False
        input_urgent = False

        match algorithm:
            case 1 :
                if not key.isdigit() or not key:
                    key_urgent = True
            case 2:
                if key.isdigit() or not key:
                    key_urgent = True
            case 4 | 5 | 6:
                if not key.isalpha() or not key :
                    key_urgent = True

        if not plain_text or not plain_text.replace(" ", "").isalpha():
            input_urgent = True

        if not key_urgent and not input_urgent:
            flag = True
        else:
            flag = False

        if self.sender() == self.encrypt_button:
            mode = 1
        elif self.sender() == self.decrypt_button:
            mode = 2
        else:
            mode = 3
            key_urgent = False
            if not input_urgent: flag = True

        self.update_widget_style(self.key_bar, key_urgent)
        self.update_widget_style(self.input_bar, input_urgent)

        if flag:
            self.data_signal.emit(plain_text, key, algorithm, mode)

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
        self.main_layout = QVBoxLayout(self.main_widget)

        #drawing the three layers
        self.draw_config_layer()
        self.draw_input_layer()
        self.draw_output_layer()

        self.setCentralWidget(self.main_widget)

    def draw_input_layer(self):
        # input bar
        self.input_bar = QTextEdit()
        self.input_bar.setFixedSize(UICONSTANTS.IO_WIDTH,UICONSTANTS.IO_HEIGHT)
        self.input_bar.setAlignment(Qt.AlignCenter)

        #input layout
        self.input_layout = QHBoxLayout()
        self.input_layout.addWidget(self.input_bar)

        #input group box
        self.input_group = QGroupBox("Input")
        self.input_group.setLayout(self.input_layout)
        self.main_layout.addWidget(self.input_group)

    def draw_config_layer(self):
        # drop_down
        self.drop_down_menu = QComboBox()
        self.drop_down_menu.addItem("Ceaser Cipher", 1)
        self.drop_down_menu.addItem("Monoalphabetic Cipher", 2)
        self.drop_down_menu.addItem("Playfair Cipher", 3)
        self.drop_down_menu.addItem("Vigenère Cipher", 4)
        self.drop_down_menu.addItem("Vigenère auto (Plain) key", 5)
        self.drop_down_menu.addItem("Vigenère auto (Cipher) key", 6)

        #key_bar
        self.key_bar = QLineEdit()
        self.key_bar.setPlaceholderText("Enter a key (0 -> 25)")

        #encrypt button
        self.encrypt_button = QPushButton("🔒 Encrypt")

        #decrypt button
        self.decrypt_button = QPushButton("🔓 Decrypt")

        #bruteforce button
        self.bruteforce_button = QPushButton("Bruteforce")

        #middle layout
        self.operations_layout = QVBoxLayout()
        self.buttons_layout = QHBoxLayout()
        self.operations_layout.addWidget(self.drop_down_menu)
        self.operations_layout.addWidget(self.key_bar)
        self.buttons_layout.addWidget(self.encrypt_button)
        self.buttons_layout.addWidget(self.decrypt_button)
        self.buttons_layout.addWidget(self.bruteforce_button)
        self.operations_layout.addLayout(self.buttons_layout)

        # middle group box
        self.operations_group = QGroupBox("Operations")
        self.operations_group.setLayout(self.operations_layout)
        self.main_layout.addWidget(self.operations_group)

    def draw_output_layer(self):
        # output bar
        self.output_bar = QTextEdit()
        self.output_bar.setReadOnly(True)
        self.output_bar.setFixedSize(UICONSTANTS.IO_WIDTH,UICONSTANTS.IO_HEIGHT)

        #right layout
        self.right_layout = QVBoxLayout()
        self.right_layout.addWidget(self.output_bar)

        # right group box
        self.right_group = QGroupBox("Output")
        self.right_group.setLayout(self.right_layout)
        self.main_layout.addWidget(self.right_group)