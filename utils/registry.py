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

CLASSICAL_REGISTRY = [
        ("Caesar", "caesar", CaesarPage),
        ("Monoalphabetic", "mono", MonoPage),
        ("Playfair", "playfair", PlayfairPage),
        ("Vigenère", "vigenere", VigenerePage),
        ("Vigenère Autokey (PT)", "vigenere_auto_p", VigenereAutoPlainPage),
        ("Vigenère Autokey (CT)", "vigenere_auto_c", VigenereAutoCipherPage),
        ("Rail Fence", "railfence", RailFencePage),
        ("Row Transposition", "rowtrans", RowTransPage),
        ("Vernam", "vernam", VernamPage),
        ("One Time Pad", "otp", OneTimePadPage),
]
PAGES_DIC = {}