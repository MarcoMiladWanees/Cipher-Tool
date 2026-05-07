import random
import secrets

from PyQt5.QtWidgets import QPushButton

from engines.vernam import vernam_cipherer
from pages.base_page import BasePage

class OneTimePadPage(BasePage):
    def __init__(self):
        title = "One Time Pad"
        description = "Achieves theoretically unbreakable encryption by combining the message with a truly random key used only once"
        super().__init__(cipher_name=title, cipher_description=description)

        self.build_keyword_widgets()
        self.update_ui()
        self.random_button.clicked.connect(self.random_key)

    def random_key(self):
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
        text = self.input_bar.toPlainText().strip().replace(" ", "")
        key = self.key_bar.text().strip().replace(" ", "")
        if not self.error:
            self.output_bar.setPlainText(vernam_cipherer(text, key))

    def decrypt(self):
        self.encrypt()

    def validate(self):
        self.error = False
        self.input_error = False
        self.key_error = False
        text = self.input_bar.toPlainText().strip().replace(" ", "")
        key = self.key_bar.text().strip().replace(" ", "")

        if not set(key).issubset({"0", "1"}):
            self.update_widget_style(self.key_bar, True)
            self.key_error = True

        if not set(text).issubset({"0", "1"}) or not text:
            self.update_widget_style(self.input_bar, True)
            self.input_error = True


        self.update_widget_style(self.input_bar, self.input_error)
        self.update_widget_style(self.key_bar, self.key_error)

        if self.input_error or self.key_error:
            self.error = True