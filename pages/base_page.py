from PyQt5.QtCore import QEventLoop, QTimer
from PyQt5.QtWidgets import (QLabel,
                             QPushButton, QWidget, QVBoxLayout, QLineEdit,
                             QHBoxLayout, QPlainTextEdit, QSpinBox, QGroupBox, QFrame, QApplication)
from utils.validators import validator_A_B

class BasePage(QWidget):
    def __init__(self, cipher_name, cipher_description):
        super().__init__()
        self.cipher_name = cipher_name
        self.cipher_description = cipher_description
        self.input_error = False
        self.key_error = False
        self.error = False
        self.initUI()
        self.setLayout(self.main_layout)

        #button signals
        self.copy_button.clicked.connect(self.copy)
        self.clear_button.clicked.connect(self.clear)
        self.swap_button.clicked.connect(self.swap)
        self.encrypt_button.clicked.connect(self.encrypt)
        self.decrypt_button.clicked.connect(self.decrypt)

    def initUI(self):
        self.main_layout = QVBoxLayout()
        self.main_layout.setSpacing(20)
        self.main_layout.setContentsMargins(65, 24, 24, 24)

        #the 4 big layouts
        self.build_header()
        self.build_parameters()
        self.build_io()
        self.build_buttons()

        #adding layputs to the main layout
        self.main_layout.addLayout(self.header_layout)
        self.main_layout.addSpacing(20)
        self.main_layout.addWidget(self.create_seperator())
        self.main_layout.addLayout(self.parameters_layout)
        self.main_layout.addWidget(self.create_seperator())
        self.main_layout.addSpacing(20)
        self.main_layout.addLayout(self.io_layout)
        self.main_layout.addSpacing(20)
        self.main_layout.addLayout(self.buttons_layout)

    def build_header(self):
        #defining the layout
        self.header_layout = QVBoxLayout()

        #defining the widgets
        self.title_label = QLabel(self.cipher_name)
        self.title_label.setObjectName("titleLabel")
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

        #input
        self.input_group = QGroupBox("Input")
        self.input_layout = QVBoxLayout()
        self.input_bar = QPlainTextEdit()
        self.input_bar.setPlaceholderText("Enter text here...")
        self.input_layout.addWidget(self.input_bar)
        self.input_group.setLayout(self.input_layout)

        #output
        self.output_group = QGroupBox("Output")
        self.output_layout = QVBoxLayout()
        self.output_bar = QPlainTextEdit()
        self.output_bar.setReadOnly(True)
        self.output_bar.setPlaceholderText("Result appears here")
        self.output_layout.addWidget(self.output_bar)
        self.output_group.setLayout(self.output_layout)

        #adding to the io layout
        self.io_layout.addWidget(self.input_group)
        self.io_layout.addWidget(self.output_group)

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
        self.key_label.setObjectName("paramLabel")

        # spinbox
        self.key_box = QSpinBox()
        self.key_box.setMinimum(0)
        self.key_box.setMaximum(25)
        self.key_box.setValue(0)

        # adding to the parameter layout
        self.parameters_layout.addWidget(self.key_label)
        self.parameters_layout.addWidget(self.key_box)

    def build_keyword_widgets(self):
        self.key_bar = QLineEdit()
        self.key_bar.setPlaceholderText("Enter a keyword")
        self.parameters_layout.addWidget(self.key_bar)

    def add_extra_buttons(self):
        pass

    def create_seperator(self):
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFixedHeight(1)
        line.setStyleSheet("background-color: #1F3447;")
        return line

    def copy(self):
        text = self.output_bar.toPlainText()
        clipboard = QApplication.clipboard()
        clipboard.setText(text)

        self.copy_button.setText("copied✔️")
        self.copy_button.setDisabled(True)
        loop = QEventLoop()
        QTimer.singleShot(5000, loop.quit)
        loop.exec_()
        self.copy_button.setDisabled(False)
        self.copy_button.setText("📋 Copy")
        return

    def clear(self):
        self.input_bar.clear()
        self.output_bar.clear()

    def swap(self):
        text = self.output_bar.toPlainText()
        self.input_bar.clear()
        self.input_bar.setPlainText(text)
        self.output_bar.clear()

    def encrypt(self):
        pass

    def decrypt(self):
        pass

    def update_widget_style(self, widget, is_urgent):
        widget.setProperty("urgent", is_urgent)
        widget.style().unpolish(widget)
        widget.style().polish(widget)
        widget.update()

    def update_ui(self):
        self.input_bar.textChanged.connect(self.validate)
        self.key_bar.textChanged.connect(self.validate)

    def validate(self):
        self.error = False

        self.input_error = validator_A_B(self.text)
        self.key_error = validator_A_B(self.key)

        self.update_widget_style(self.input_bar, self.input_error)
        self.update_widget_style(self.key_bar, self.key_error)

        if self.input_error or self.key_error:
            self.error = True

    @property
    def text(self):
        return self.input_bar.toPlainText().strip()

    @property
    def key(self):
        return self.key_bar.text().strip().replace(" ", "")
