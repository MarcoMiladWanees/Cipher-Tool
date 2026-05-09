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
        if not self.error:
            self.output_bar.setPlainText(vigenere_auto_cipher_encryptor(self.text, self.key))

    def decrypt(self):
        if not self.error:
            self.output_bar.setPlainText(vigenere_auto_cipher_decryptor(self.text, self.key))