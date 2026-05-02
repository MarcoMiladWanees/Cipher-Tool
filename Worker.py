from PyQt5.QtCore import QObject, pyqtSignal
from engines.caesar import *
from engines.mono_alphabetic import *
from engines.playfair import playfair_encryptor, playfair_decryptor
from engines.vigenere import *
from engines.vernam import *
from engines.one_time_pad import *
from engines.rail_fence import *
from engines.row_transposition import *

class Worker(QObject):

    def encrypt(self, input_text, key, algorithm):
        match algorithm:
            case 1:
                self.done_signal.emit(ceaser_encryptor(input_text, int(key)))
            case 2:
                self.done_signal.emit(mono_encryptor(input_text, key))
            case 3:
                self.done_signal.emit(playfair_encryptor(input_text, key))
            case 4:
                self.done_signal.emit(vigenere_encryptor(input_text, key))
            case 5:
                self.done_signal.emit(vigenere_auto_plain_encryptor(input_text, key))
            case 6:
                self.done_signal.emit(vigenere_auto_cipher_encryptor(input_text, key))
            case 7:
                self.done_signal.emit(vernam_cipherer(input_text, key))
            case 8:
                self.done_signal.emit(one_time_pad(input_text, key))
            case 9:
                self.done_signal.emit(rail_fence_encryptor(input_text, key))
            case 10:
                self.done_signal.emit(row_transposition_encryptor(input_text, key))

    def decrypt(self, input_text, key, algorithm):
        match algorithm:
            case 1:
                self.done_signal.emit(ceaser_decryptor(input_text, int(key)))
            case 2:
                self.done_signal.emit(mono_decryptor(input_text, key))
            case 3:
                self.done_signal.emit(playfair_decryptor(input_text, key))
            case 4:
                self.done_signal.emit(vigenere_decryptor(input_text, key))
            case 5:
                self.done_signal.emit(vigenere_auto_plain_decryptor(input_text, key))
            case 6:
                self.done_signal.emit(vigenere_auto_cipher_decryptor(input_text, key))
            case 7:
                self.done_signal.emit(vernam_cipherer(input_text, key))
            case 8:
                self.done_signal.emit(one_time_pad(input_text, key))
            case 9:
                self.done_signal.emit(rail_fence_decryptor(input_text, key))
            case 10:
                self.done_signal.emit(row_transposition_decryptor(input_text, key))

    def bruteforce(self, input_text, algorithm):
        output = ""
        match algorithm:
            case 1:
                for k in range(26):
                    output += f"\n[{k}] {ceaser_decryptor(input_text, k)}\n"
                    output += "--------------------------------------"
