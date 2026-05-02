from pages.base_page import BasePage

class MonoPage(BasePage):
    def __init__(self):
        title = "Monoalphabetic Cipher"
        description = "Substitutes each letter using a scrambled alphabet derived from a secret keyword"
        super().__init__(cipher_name=title, cipher_description=description)

        self.build_keyword_widgets()