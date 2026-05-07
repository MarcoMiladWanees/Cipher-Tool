from engines.vigenère_autokey_ciphertext import vigenere_auto_cipher_encryptor, vigenere_auto_cipher_decryptor
from pages.base_page import BasePage


class VigenereAutoCipherPage(BasePage):
    def __init__(self):
        title = "Vigenère Autokey — Ciphertext"
        description = "Extends the keyword using the ciphertext as it is produced, binding the key to the encrypted output"
        super().__init__(cipher_name=title, cipher_description=description)

        self.build_keyword_widgets()
        self.update_ui()

    def encrypt(self):
        text = self.input_bar.toPlainText()
        key = self.key_bar.text()
        if not self.error:
            self.output_bar.setPlainText(vigenere_auto_cipher_encryptor(text, key))

    def decrypt(self):
        text = self.input_bar.toPlainText()
        key = self.key_bar.text()
        if not self.error:
            self.output_bar.setPlainText(vigenere_auto_cipher_decryptor(text, key))