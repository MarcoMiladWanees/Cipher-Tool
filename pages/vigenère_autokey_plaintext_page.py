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
        if not self.error:
            self.output_bar.setPlainText(vigenere_auto_plain_encryptor(self.text, self.key))

    def decrypt(self):
        if not self.error:
            self.output_bar.setPlainText(vigenere_auto_plain_decryptor(self.text, self.key))

