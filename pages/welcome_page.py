from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QBrush, QColor, QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel


class WelcomePage(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        # K4 CIPHER TEXT
        self.k4_cipher_text = "OBKRUOXOGHULBSOLIFBBWFLRVQQPRNGKSSOTWTQSJQSSEKZZWATJKLUDIAWINFBNYPVTTMZFPKWGDKZXTJCDIGKUHUAUEKCAR"

        self.name_label = QLabel("K R Y P T O S")
        self.name_label.setObjectName("heroLabel")
        self.name_label.setAlignment(Qt.AlignCenter)

        self.subtitle1 = QLabel("between subtle shading and the absence of light\n lies the nuance of illusion")
        self.subtitle1.setObjectName("quoteLabel")
        self.subtitle1.setAlignment(Qt.AlignCenter)

        self.subtitle2 = QLabel('Select a method from the sidebar to begin')
        self.subtitle2.setObjectName("hintLabel")
        self.subtitle2.setAlignment(Qt.AlignCenter)


        self.main_layout.addStretch(1)
        self.main_layout.addWidget(self.name_label)
        self.main_layout.addSpacing(20)
        self.main_layout.addWidget(self.subtitle1)
        self.main_layout.addSpacing(20)
        self.main_layout.addWidget(self.subtitle2)
        self.main_layout.addStretch(1)

    def paintEvent(self, event):
        super().paintEvent(event)  # let Qt do its normal painting (children, etc.)

        painter = QPainter(self)
        painter.setOpacity(0.07)
        painter.setPen(QColor("#00D4FF"))
        painter.setFont(QFont("JetBrains Mono", 14))
        painter.drawText(self.rect(), Qt.AlignCenter |  Qt.TextWrapAnywhere, self.k4_cipher_text * 55)
        painter.end()  # release the painter
