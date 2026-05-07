from engines.mono_alphabetic import mono_encryptor, mono_decryptor
from pages.base_page import BasePage

class MonoPage(BasePage):
    def __init__(self):
        title = "Monoalphabetic Cipher"
        description = "Substitutes each letter using a scrambled alphabet derived from a secret keyword"
        super().__init__(cipher_name=title, cipher_description=description)

        self.build_keyword_widgets()
        self.update_ui()

    def encrypt(self):
        text = self.input_bar.toPlainText()
        key = self.key_bar.text()
        if not self.error:
            self.output_bar.setPlainText(mono_encryptor(text, key))

    def decrypt(self):
        text = self.input_bar.toPlainText()
        key = self.key_bar.text()
        if not self.error:
            self.output_bar.setPlainText(mono_decryptor(text, key))