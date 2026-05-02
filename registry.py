from pages.caesar_page import CaesarPage
from pages.mono_page import MonoPage
from pages.playfair_page import PlayfairPage
from pages.rail_fence_page import RailFencePage
from pages.row_transposition_page import RowTransPage
from pages.vernam_page import VernamPage
from pages.one_time_pad_page import OneTimePadPage
from pages.vigenère_autokey_ciphertext_page import VigenereAutoCipherPage
from pages.vigenère_autokey_plaintext_page import VigenereAutoPlainPage
from pages.vigenère_page import VigenerePage

CLASSICAL_REGISTRY = {
    "Substitution Ciphers": [
        ("Caesar Cipher", "caesar", CaesarPage),
        ("Monoalphabetic", "mono", MonoPage),
        ("Playfair", "playfair", PlayfairPage),
        ("Vigenère Cipher", "vigenere", VigenerePage),
        ("Vigenère Autokey — Plaintext", "vigenere_auto_p", VigenereAutoPlainPage),
        ("Vigenère Autokey — Ciphertext", "vigenere_auto_c", VigenereAutoCipherPage),
    ],
    "Transposition Ciphers": [
        ("Rail Fence", "railfence", RailFencePage),
        ("Row Transposition", "rowtrans", RowTransPage),
    ],
    "Stream Ciphers": [
        ("Vernam", "vernam", VernamPage),
        ("One Time Pad", "otp", OneTimePadPage),
    ]
}