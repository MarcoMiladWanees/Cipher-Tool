from pages.base_page import BasePage

class VernamPage(BasePage):
    def __init__(self):
        title = "Vernam Cipher"
        description = "Combines each bit of the message with a corresponding bit of the key using the XOR operation"
        super().__init__(cipher_name=title, cipher_description=description)

        self.build_keyword_widgets()

    def build_keyword_widgets(self):
        super().build_keyword_widgets()
        self.key_bar.setPlaceholderText("Enter binary key")