from PyQt5.QtWidgets import QWidget, QLabel, QSlider, QSpinBox

from engines.rail_fence import rail_fence_encryptor, rail_fence_decryptor
from pages.base_page import BasePage


class RailFencePage(BasePage):
    def __init__(self):
        title = "Rail Fence Cipher"
        description = "Weaves the message in a zigzag pattern across multiple rails, then reads off each rail in sequence"
        super().__init__(cipher_name=title, cipher_description=description)
        self.build_numeric_key_widgets()

    def build_numeric_key_widgets(self):
        super().build_numeric_key_widgets()

        #label
        self.key_label.setText("Depth:")

        # slider
        self.key_slider.setMinimum(2)
        self.key_slider.setMaximum(999)
        self.key_slider.setValue(2)

        #spinbox
        self.key_box.setMinimum(2)
        self.key_box.setMaximum(999)
        self.key_box.setValue(2)

    def encrypt(self):
        text = self.input_bar.toPlainText()
        depth = self.key_box.value()
        self.output_bar.setPlainText(rail_fence_encryptor(text, depth))

    def decrypt(self):
        text = self.input_bar.toPlainText()
        depth = self.key_box.value()
        self.output_bar.setPlainText(rail_fence_decryptor(text, depth))


    def validate(self):
        pass