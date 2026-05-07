from engines.vigenère_autokey_plaintext import vigenere_auto_plain_encryptor, vigenere_auto_plain_decryptor
from pages.base_page import BasePage


class VigenereAutoPlainPage(BasePage):
    def __init__(self):
        title = "Vigenère Autokey — Plaintext"
        description = "Extends the keyword using the plaintext itself, creating a key that never repeats"
        super().__init__(cipher_name=title, cipher_description=description)

        self.build_keyword_widgets()
        self.update_ui()

    def encrypt(self):
        text = self.input_bar.toPlainText()
        key = self.key_bar.text()
        if not self.error:
            self.output_bar.setPlainText(vigenere_auto_plain_encryptor(text, key))

    def decrypt(self):
        text = self.input_bar.toPlainText()
        key = self.key_bar.text()
        if not self.error:
            self.output_bar.setPlainText(vigenere_auto_plain_decryptor(text, key))

