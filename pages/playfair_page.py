from engines.playfair import playfair_encryptor, playfair_decryptor
from pages.base_page import BasePage
from utils.validators import validator_playfair_decrypt


class PlayfairPage(BasePage):
    def __init__(self):
        title = "Playfair Cipher"
        description = "Encrypts letter pairs using a 5×5 matrix constructed from a keyword"
        super().__init__(cipher_name=title, cipher_description=description)

        self.build_keyword_widgets()
        self.update_ui()

    def encrypt(self):
        if not self.error:
            self.output_bar.setPlainText(playfair_encryptor(self.text, self.key))

    def decrypt(self):
        if validator_playfair_decrypt(self.text):
            self.error = True
            self.update_widget_style(self.input_bar, True)
            self.output_bar.setPlainText("Error: Playfair ciphertext must have an even number of characters.")
        if not self.error:
            self.output_bar.setPlainText(playfair_decryptor(self.text, self.key))
