from pages.base_page import BasePage

class PlayfairPage(BasePage):
    def __init__(self):
        title = "Playfair Cipher"
        description = "Encrypts letter pairs using a 5×5 matrix constructed from a keyword"
        super().__init__(cipher_name=title, cipher_description=description)

        self.build_keyword_widgets()