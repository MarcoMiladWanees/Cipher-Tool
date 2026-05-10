from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout

from engines.playfair import playfair_encryptor, playfair_decryptor, playfair_grid_maker
from pages.base_page import BasePage
from utils.validators import validator_playfair_decrypt


class PlayfairPage(BasePage):
    def __init__(self):
        title = "Playfair Cipher"
        description = "Encrypts letter pairs using a 5×5 matrix constructed from a keyword"
        super().__init__(cipher_name=title, cipher_description=description)

        self.build_keyword_widgets()
        self.update_ui()
        self.main_layout.setStretchFactor(self.parameters_layout, 1)
        self.main_layout.setStretchFactor(self.io_layout, 2)
        self.update_grid()

    def encrypt(self):
        if not self.error:
            self.output_bar.setPlainText(playfair_encryptor(self.text, self.key))

    def decrypt(self):
        if validator_playfair_decrypt(self.text):
            self.error = True
            self.update_widget_style(self.input_bar, True)
            self.output_bar.setPlainText("Error: Playfair ciphertext must have an even number of characters.")
        if not self.error:
            self.output_bar.setPlainText(playfair_decryptor(self.text, self.key))

    def build_parameters(self):
        self.parameters_layout = QHBoxLayout()
        self.key_layout = QVBoxLayout()
    def build_keyword_widgets(self):
        self.key_bar = QLineEdit()
        self.key_bar.setPlaceholderText("Enter a keyword")
        self.key_bar.setFixedWidth(280)
        grid_widget = self._build_grid_widget()

        self.key_layout.addWidget(self.key_bar)
        self.key_layout.addWidget(grid_widget)
        self.parameters_layout.addStretch(1)
        self.parameters_layout.addLayout(self.key_layout)
        self.parameters_layout.addStretch(1)

        self.key_bar.textChanged.connect(self.update_grid)

    def _build_grid_widget(self):
        self.container = QWidget()
        self.container.setObjectName("playfairGridContainer")
        self.container.setFixedWidth(280)
        grid_layout = QGridLayout()
        grid_layout.setContentsMargins(10, 10, 10, 10)
        grid_layout.setSpacing(8)
        grid_layout.setAlignment(Qt.AlignCenter)
        self.grid_labels = []

        for row in range(5):
            row_list = []
            for col in range(5):
                label = QLabel()
                label.setFixedSize(50, 50)
                label.setAlignment(Qt.AlignCenter)
                label.setObjectName("playfairCell")
                row_list.append(label)
                grid_layout.addWidget(label, row, col)
            self.grid_labels.append(row_list)

        self.container.setLayout(grid_layout)
        return self.container

    def update_grid(self):
        key_map, pos_map = playfair_grid_maker(self.key_bar.text())
        for r in range(5):
            for c in range(5):
                self.grid_labels[r][c].setText(key_map[r][c].upper())