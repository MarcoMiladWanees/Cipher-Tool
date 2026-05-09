from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QSlider, QSpinBox, QPushButton

from pages.base_page import BasePage
from engines.caesar import *
from utils.validators import validator_A_B


class CaesarPage(BasePage):
    def __init__(self):
        title = "Caesar Cipher"
        description = "The ancient Roman cipher that shifts each letter by a fixed number of positions through the alphabet"
        super().__init__(cipher_name=title, cipher_description=description)
        self.build_numeric_key_widgets()
        self.bruteforce_button.clicked.connect(self.bruteforce)
        self.key_box.valueChanged.connect(self.update_label)
        self.update_ui()

    def add_extra_buttons(self):
        self.bruteforce_button = QPushButton("💥 Bruteforce")
        self.bruteforce_button.setObjectName("bruteforceButton")
        self.buttons_layout.addWidget(self.bruteforce_button)

    def build_numeric_key_widgets(self):
        self.parameters_layout.addStretch(1)

        super().build_numeric_key_widgets()
        self.shift_value_label = QLabel(f"A → {chr(self.key + 65)}")
        self.shift_value_label.setObjectName("paramLabel")
        self.parameters_layout.addWidget(self.shift_value_label)
        self.parameters_layout.addStretch(1)

    def update_label(self):
        self.shift_value_label.setText(f"A → {chr(self.key + 65)}")
    def encrypt(self):
        if not self.input_error:
            self.output_bar.setPlainText(caesar_processor(self.text, self.key))

    def decrypt(self):
        if not self.input_error:
            self.output_bar.setPlainText(caesar_processor(self.text, -(self.key)))

    def bruteforce(self):
        if not self.error:
            output = ""
            for k in range(26):
                output += f"\n[{k}] {caesar_processor(self.text, k)}\n"
                output += "--------------------------------------"
            self.output_bar.setPlainText(output)

    def update_ui(self):
        self.input_bar.textChanged.connect(self.validate)

    def validate(self):
        self.input_error = validator_A_B(self.text)
        self.update_widget_style(self.input_bar, self.input_error)


    @property
    def key(self):
        return self.key_box.value()