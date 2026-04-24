from PyQt5.QtCore import QObject
from Ceaser.Algorithm import *
from Monoalphabitic.Algorithm import *


class Worker(QObject):
    def __init__(self):
        super().__init__()
        self.input = None
        self.key = None

    def Ceaser_Encrypt(self):
        return ceaser_encrypt(self.input, int(self.key))

    def Ceaser_Decrypt(self):
        return ceaser_decrypt(self.input, int(self.key))

    def Mono_Encrypt(self):
        return mono_encrypt(self.input, self.key)

    def Mono_Decrypt(self):
        return mono_decrypt(self.input, self.key)

