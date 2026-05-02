from pages.base_page import BasePage


class VigenereAutoPlainPage(BasePage):
    def __init__(self):
        title = "Vigenère Autokey — Plaintext"
        description = "Extends the keyword using the plaintext itself, creating a key that never repeats"
        super().__init__(cipher_name=title, cipher_description=description)

        self.build_keyword_widgets()