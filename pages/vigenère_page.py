from pages.base_page import BasePage


class VigenerePage(BasePage):
    def __init__(self):
        title = "Vigenère Cipher"
        description = "Applies a rotating series of shifts based on a repeating keyword to defeat frequency analysis"
        super().__init__(cipher_name=title, cipher_description=description)

        self.build_keyword_widgets()