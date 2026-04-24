from PyQt5.QtCore import QObject, pyqtSignal
from Ceaser.Algorithm import *
from Monoalphabitic.Algorithm import *


class Worker(QObject):

    done_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def router(self, input_text, key, algorithm, mode):
        match mode:
            case 1:
                self.encrypt(input_text, key, algorithm)
            case 2:
                self.decrypt(input_text, key, algorithm)
            case 3:
                self.bruteforce(input_text, algorithm)

    def encrypt(self, input_text, key, algorithm):
        match algorithm:
            case 1:
                self.done_signal.emit(ceaser_encrypt(input_text, int(key)))
            case 2:
                self.done_signal.emit(mono_encrypt(input_text, key))

    def bruteforce(self, input_text, algorithm):
        output = ""
        match algorithm:
            case 1:
                for k in range(26):
                    output += f"\n[{k}] {ceaser_decrypt(input_text, k)}\n"
                    output += "--------------------------------------"
        self.done_signal.emit(output)

    def decrypt(self, input_text, key, algorithm):
        match algorithm:
            case 1:
                self.done_signal.emit(ceaser_decrypt(input_text, int(key)))
            case 2:
                self.done_signal.emit(mono_decrypt(input_text, key))

