from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QSlider, QSpinBox, QPushButton

from base_page import BasePage
from engines.caesar import *

class CaesarPage(BasePage):
    def __init__(self):
        title = "Caesar Cipher"
        description = "The ancient Roman cipher that shifts each letter by a fixed number of positions through the alphabet"
        super().__init__(cipher_name=title, cipher_description=description)
        self.build_numeric_key_widgets()

    def add_extra_buttons(self):
        self.bruteforce_button = QPushButton("💥 Bruteforce")
        self.bruteforce_button.setObjectName("bruteforceButton")
        self.buttons_layout.addWidget(self.bruteforce_button)
