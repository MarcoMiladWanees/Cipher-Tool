import random
import secrets

from PyQt5.QtWidgets import QPushButton

from engines.vernam import vernam_cipherer
from pages.base_page import BasePage
from pages.vernam_page import VernamPage
from utils.validators import validator_D


class OneTimePadPage(BasePage):
    def __init__(self):
        title = "One Time Pad"
        description = "Achieves theoretically unbreakable encryption by combining the message with a truly random key used only once"
        super().__init__(cipher_name=title, cipher_description=description)

        self.build_keyword_widgets()
        self.update_ui()
        self.random_button.clicked.connect(self.random_key)

    def random_key(self):
        self.key_bar.clear()
        text = self.input_bar.toPlainText()
        text = [char for char in text if char == "1" or char == '0']
        if not text:
            self.update_widget_style(self.input_bar, True)
            return
        key = [secrets.choice('01') for _ in range(len(text))]
        self.key_bar.setText("".join(key))

    def build_keyword_widgets(self):
        super().build_keyword_widgets()
        self.key_bar.setPlaceholderText("Enter binary key")
        self.random_button = QPushButton("🎲 Random")
        self.parameters_layout.addWidget(self.random_button)

    def encrypt(self):
        if not self.error:
            self.output_bar.setPlainText(vernam_cipherer(self.text, self.key))

    def decrypt(self):
        self.encrypt()

    def validate(self):
        self.error = False
        self.input_error = validator_D(self.text)
        self.key_error = validator_D(self.key)

        self.update_widget_style(self.input_bar, self.input_error)
        self.update_widget_style(self.key_bar, self.key_error)

        if self.input_error or self.key_error:
            self.error = True