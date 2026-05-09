from engines.row_transposition import row_transposition_encryptor, row_transposition_decryptor
from pages.base_page import BasePage
from utils.validators import validator_C, validator_row_trans_key, validator_row_trans_decrypt


class RowTransPage(BasePage):
    def __init__(self):
        title = "Row Transposition Cipher"
        description = "Arranges the message into a grid of rows and reorders the columns based on a numeric key"
        super().__init__(cipher_name=title, cipher_description=description)
        self.build_keyword_widgets()
        self.update_ui()

    def build_keyword_widgets(self):
        super().build_keyword_widgets()
        self.key_bar.setPlaceholderText("e.g., 3142 or ZEBRA")

    def encrypt(self):
        if not self.error:
            self.output_bar.setPlainText(row_transposition_encryptor(self.text, self.key))

    def decrypt(self):
        if validator_row_trans_decrypt(self.text, self.key):
            self.update_widget_style(self.input_bar, True)
            self.output_bar.setPlainText("Error: Input length must be a multiple of the key length ")
            self.error = True
        if not self.error:
            self.output_bar.setPlainText(row_transposition_decryptor(self.text, self.key))

    def validate(self):
        self.error = False
        self.input_error = validator_C(self.text)
        self.key_error = validator_row_trans_key(self.key)

        self.update_widget_style(self.input_bar, self.input_error)
        self.update_widget_style(self.key_bar, self.key_error)

        if self.input_error or self.key_error:
            self.error = True