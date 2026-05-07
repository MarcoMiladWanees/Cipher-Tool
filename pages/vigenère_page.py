from engines.vigenere import vigenere_encryptor, vigenere_decryptor
from pages.base_page import BasePage


class VigenerePage(BasePage):
    def __init__(self):
        title = "Vigenère Cipher"
        description = "Applies a rotating series of shifts based on a repeating keyword to defeat frequency analysis"
        super().__init__(cipher_name=title, cipher_description=description)

        self.build_keyword_widgets()
        self.update_ui()

    def encrypt(self):
        text = self.input_bar.toPlainText()
        key = self.key_bar.text()
        if not self.error:
            self.output_bar.setPlainText(vigenere_encryptor(text, key))

    def decrypt(self):
        text = self.input_bar.toPlainText()
        key = self.key_bar.text()
        if not self.error:
            self.output_bar.setPlainText(vigenere_decryptor(text, key))

