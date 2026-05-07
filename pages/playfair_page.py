from engines.playfair import playfair_encryptor, playfair_decryptor
from pages.base_page import BasePage

class PlayfairPage(BasePage):
    def __init__(self):
        title = "Playfair Cipher"
        description = "Encrypts letter pairs using a 5×5 matrix constructed from a keyword"
        super().__init__(cipher_name=title, cipher_description=description)

        self.build_keyword_widgets()
        self.update_ui()

    def encrypt(self):
        text = self.input_bar.toPlainText().strip().replace(" ", "")
        key = self.key_bar.text().strip().replace(" ", "")
        if not self.error:
            self.output_bar.setPlainText(playfair_encryptor(text, key))

    def decrypt(self):
        text = self.input_bar.toPlainText().strip().replace(" ", "")
        key = self.key_bar.text().strip().replace(" ", "")
        if not self.error:
            self.output_bar.setPlainText(playfair_decryptor(text, key))