import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QPushButton, QCheckBox, QWidget, QVBoxLayout, QRadioButton, QButtonGroup, QLineEdit,
                             QHBoxLayout, QComboBox, QGroupBox, QTextEdit, QPlainTextEdit, QSlider, QSpinBox)
from   PyQt5.QtGui     import QIcon, QFont
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from   PyQt5.QtGui     import QPixmap

from constants import UICONSTANTS, resource_path

class BasePage(QWidget):
    def __init__(self, cipher_name, cipher_description):
        super().__init__()
        self.cipher_name = cipher_name
        self.cipher_description = cipher_description

        self.initUI()

        self.setLayout(self.main_layout)

    def initUI(self):
        #main layout
        self.main_layout = QVBoxLayout()

        #the 4 big layouts
        self.build_header()
        self.build_parameters()
        self.build_io()
        self.build_buttons()

        #adding layputs to the main layout
        self.main_layout.addLayout(self.header_layout)
        self.main_layout.addLayout(self.parameters_layout)
        self.main_layout.addLayout(self.io_layout)
        self.main_layout.addLayout(self.buttons_layout)

    def build_header(self):
        #defining the layout
        self.header_layout = QVBoxLayout()

        #defining the widgets
        self.title_label = QLabel(self.cipher_name)
        self.title_label.setObjectName("title_label")
        self.description_label = QLabel(self.cipher_description)
        self.description_label.setObjectName("subtitleLabel")

        #adding stuff to the layout
        self.header_layout.addWidget(self.title_label)
        self.header_layout.addWidget(self.description_label)

    def build_parameters(self):
        #defining the parameters layout
        self.parameters_layout = QHBoxLayout()

    def build_io(self):
        #defining the io layout
        self.io_layout = QHBoxLayout()

        #defining widgets
        self.input_bar = QPlainTextEdit()
        self.output_bar = QPlainTextEdit()
        self.output_bar.setReadOnly(True)

        #adding to the io layout
        self.io_layout.addWidget(self.input_bar)
        self.io_layout.addWidget(self.output_bar)

    def build_buttons(self):
        self.buttons_layout = QHBoxLayout()

        # encrypt button
        self.encrypt_button = QPushButton("🔒 Encrypt")
        self.encrypt_button.setObjectName("encryptButton")

        # decrypt button
        self.decrypt_button = QPushButton("🔓 Decrypt")
        self.decrypt_button.setObjectName("decryptButton")

        # swap button
        self.swap_button = QPushButton("⇄ Swap")

        #copy button
        self.copy_button = QPushButton("📋 Copy")
        self.copy_button.setObjectName("copyButton")

        #clear button
        self.clear_button = QPushButton("🗑 Clear")
        self.clear_button.setObjectName("clearButton")

        #adding the buttons to the layout
        self.buttons_layout.addWidget(self.encrypt_button)
        self.buttons_layout.addWidget(self.decrypt_button)
        self.add_extra_buttons()
        self.buttons_layout.addStretch()
        self.buttons_layout.addWidget(self.swap_button)
        self.buttons_layout.addWidget(self.copy_button)
        self.buttons_layout.addWidget(self.clear_button)

    def build_numeric_key_widgets(self):
        # defining the widgets

        # label
        self.key_label = QLabel("Shift:")

        # slider
        self.key_slider = QSlider(Qt.Horizontal)
        self.key_slider.setMinimum(0)
        self.key_slider.setMaximum(25)
        self.key_slider.setValue(0)

        # spinbox
        self.key_box = QSpinBox()
        self.key_box.setMinimum(0)
        self.key_box.setMaximum(25)
        self.key_box.setValue(0)

        # linking the spinbox to the slider
        self.key_box.valueChanged.connect(self.key_slider.setValue)
        self.key_slider.valueChanged.connect(self.key_box.setValue)

        # adding to the parameter layout
        self.parameters_layout.addWidget(self.key_label)
        self.parameters_layout.addWidget(self.key_slider)
        self.parameters_layout.addWidget(self.key_box)

    def build_keyword_widgets(self):
        self.key_bar = QLineEdit()
        self.key_bar.setPlaceholderText("Enter a keyword")
        self.parameters_layout.addWidget(self.key_bar)

    def add_extra_buttons(self):
        pass

