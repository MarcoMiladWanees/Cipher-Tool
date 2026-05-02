from pages.base_page import BasePage

class OneTimePadPage(BasePage):
    def __init__(self):
        title = "One Time Pad"
        description = "Achieves theoretically unbreakable encryption by combining the message with a truly random key used only once"
        super().__init__(cipher_name=title, cipher_description=description)

        self.build_keyword_widgets()

    def build_keyword_widgets(self):
        super().build_keyword_widgets()
        self.key_bar.setPlaceholderText("Enter binary key")