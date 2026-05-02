from pages.base_page import BasePage

class RowTransPage(BasePage):
    def __init__(self):
        title = "Row Transposition Cipher"
        description = "Arranges the message into a grid of rows and reorders the columns based on a numeric key"
        super().__init__(cipher_name=title, cipher_description=description)
        self.build_keyword_widgets()

    def build_keyword_widgets(self):
        super().build_keyword_widgets()
        self.key_bar.setPlaceholderText("e.g., 3142 or ZEBRA")