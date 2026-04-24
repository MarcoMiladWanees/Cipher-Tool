from PyQt5.QtCore import QObject, pyqtSignal
from Ceaser.Algorithm import *
from Monoalphabitic.Algorithm import *


class Worker(QObject):

    done_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def router(self, input, key, algorithm, mode):
        match mode:
            case 1:
                self.encrypt(input, key, algorithm)
            case 2:
                self.decrypt(input, key, algorithm)

    def encrypt(self, input, key, algorithm):
        match algorithm:
            case 1:
                self.done_signal.emit(ceaser_encrypt(input, int(key)))
            case 2:
                self.done_signal.emit(mono_encrypt(input, key))

    def decrypt(self, input, key, algorithm):
        match algorithm:
            case 1:
                self.done_signal.emit(ceaser_decrypt(input, int(key)))
            case 2:
                self.done_signal.emit(mono_decrypt(input, key))

