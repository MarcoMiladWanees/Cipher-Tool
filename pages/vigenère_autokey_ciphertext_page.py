from pages.base_page import BasePage


class VigenereAutoCipherPage(BasePage):
    def __init__(self):
        title = "Vigenère Autokey — Ciphertext"
        description = "Extends the keyword using the ciphertext as it is produced, binding the key to the encrypted output"
        super().__init__(cipher_name=title, cipher_description=description)

        self.build_keyword_widgets()