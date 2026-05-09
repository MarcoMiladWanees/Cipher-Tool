from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSlider

from engines.rail_fence import rail_fence_encryptor, rail_fence_decryptor
from pages.base_page import BasePage
from utils.validators import validator_C


class RailFencePage(BasePage):
    def __init__(self):
        title = "Rail Fence Cipher"
        description = "Weaves the message in a zigzag pattern across multiple rails, then reads off each rail in sequence"
        super().__init__(cipher_name=title, cipher_description=description)
        self.build_numeric_key_widgets()
        self.update_ui()

    def build_numeric_key_widgets(self):
        super().build_numeric_key_widgets()

        #label
        self.key_label.setText("Depth:")

        # slider
        self.key_slider = QSlider(Qt.Horizontal)
        self.key_slider.setMinimum(0)
        self.key_slider.setMaximum(25)
        self.key_slider.setValue(0)

        # slider
        self.key_slider.setMinimum(2)
        self.key_slider.setMaximum(999)
        self.key_slider.setValue(2)

        #spinbox
        self.key_box.setMinimum(2)
        self.key_box.setMaximum(999)
        self.key_box.setValue(2)

        # linking the spinbox to the slider
        self.key_box.valueChanged.connect(self.key_slider.setValue)
        self.key_slider.valueChanged.connect(self.key_box.setValue)


        self.parameters_layout.addWidget(self.key_slider)

    def encrypt(self):
        if not self.input_error:
            self.output_bar.setPlainText(rail_fence_encryptor(self.text, self.key))

    def decrypt(self):
        if not self.input_error:
            self.output_bar.setPlainText(rail_fence_decryptor(self.text, self.key))

    def update_ui(self):
        self.input_bar.textChanged.connect(self.validate)

    def validate(self):
        self.input_error = validator_C(self.text)
        self.update_widget_style(self.input_bar, self.input_error)

    @property
    def key(self):
        return self.key_box.value()