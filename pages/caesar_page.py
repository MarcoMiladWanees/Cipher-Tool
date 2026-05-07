from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QSlider, QSpinBox, QPushButton

from pages.base_page import BasePage
from engines.caesar import *

class CaesarPage(BasePage):
    def __init__(self):
        title = "Caesar Cipher"
        description = "The ancient Roman cipher that shifts each letter by a fixed number of positions through the alphabet"
        super().__init__(cipher_name=title, cipher_description=description)
        self.build_numeric_key_widgets()
        self.bruteforce_button.clicked.connect(self.bruteforce)

    def add_extra_buttons(self):
        self.bruteforce_button = QPushButton("💥 Bruteforce")
        self.bruteforce_button.setObjectName("bruteforceButton")
        self.buttons_layout.addWidget(self.bruteforce_button)

    def encrypt(self):
        text = self.input_bar.toPlainText()
        key = self.key_box.value()
        if not self.error:
            self.output_bar.setPlainText(caesar_processor(text, key))

    def decrypt(self):
        text = self.input_bar.toPlainText()
        key = self.key_box.value()
        if not self.error:
            self.output_bar.setPlainText(caesar_processor(text, -key))

    def bruteforce(self):
        text = self.input_bar.toPlainText()
        if not self.error:
            output = ""
            for k in range(26):
                output += f"\n[{k}] {caesar_processor(text, k)}\n"
                output += "--------------------------------------"
            self.output_bar.setPlainText(output)

    def validate(self):
        pass