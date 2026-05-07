from engines.row_transposition import row_transposition_encryptor, row_transposition_decryptor
from pages.base_page import BasePage

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
        text = self.input_bar.toPlainText().strip().replace(" ", "")
        key = self.key_bar.text().strip().replace(" ", "")
        if self.error:
            self.output_bar.setPlainText(row_transposition_encryptor(text, key))

    def decrypt(self):
        text = self.input_bar.toPlainText().strip().replace(" ", "")
        key = self.key_bar.text().strip().replace(" ", "")
        if self.error:
            self.output_bar.setPlainText(row_transposition_decryptor(text, key))

    def validate(self):
        self.error = False
        self.input_error = False
        self.key_error = False
        text = self.input_bar.toPlainText().strip().replace(" ", "")
        key = self.key_bar.text().strip().replace(" ", "")

        if not key or (not key.isalpha() and not key.isdigit()):
            self.key_error = True

        if not text:
            self.input_error = True

        self.update_widget_style(self.input_bar, self.input_error)
        self.update_widget_style(self.key_bar, self.key_error)

        if self.input_error or self.key_error:
            self.error = True