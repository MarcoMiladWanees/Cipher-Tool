from engines.vernam import vernam_cipherer
from pages.base_page import BasePage
from utils.validators import validator_D


class VernamPage(BasePage):
    def __init__(self):
        title = "Vernam Cipher"
        description = "Combines each bit of the message with a corresponding bit of the key using the XOR operation"
        super().__init__(cipher_name=title, cipher_description=description)

        self.build_keyword_widgets()
        self.update_ui()

    def build_keyword_widgets(self):
        super().build_keyword_widgets()
        self.key_bar.setPlaceholderText("Enter binary key")

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

