from cipher_algos.letters_dic import letter_to_number, number_to_letter
import math

def vigenere_formatter(text):
    text = text.lower()
    text = list(text.replace(" ", ""))
    return list(text)

def vigenere_translator(text):
    for i in range(len(text)):
        text[i] = letter_to_number.get(text[i],text[i])
    return text

def vigenere_key_generator(length,key):
    i = 0
    while len(key) < length:
        key.append(key[i % len(key)])
        i += 1

    return key

def vigenere_cipherer(msg, key):
    # calculating the cipher
    cipher = []
    for i in range(len(msg)):
            cipher.append((key[i] + msg[i]) % 26)

    cipher_text = [number_to_letter[n] if isinstance(n, int) else n for n in cipher]
    return "".join(cipher_text).upper()

def vigenere_decipherer(cipher, key):
    # calculating the msg
    msg = []
    for i in range(len(cipher)):
        msg.append((cipher[i] - key[i] + 26) % 26)

    plain_text = [number_to_letter[n] if isinstance(n, int) else n for n in msg]
    return "".join(plain_text)

def vigenere_encryptor(msg, key):
    #handling msg
    msg = vigenere_formatter(msg)
    msg = vigenere_translator(msg)
    #handling key
    key = vigenere_formatter(key)
    key = vigenere_translator(key)
    key = vigenere_key_generator(len(msg),key)

    return vigenere_cipherer(msg, key)

def vigenere_decryptor(cipher, key):
    #Handling cipher
    cipher = vigenere_formatter(cipher)
    cipher = vigenere_translator(cipher)
    # handling key
    key = vigenere_formatter(key)
    key = vigenere_translator(key)
    key = vigenere_key_generator(len(cipher), key)

    return vigenere_decipherer(cipher, key)

def vigenere_auto_plain_encryptor(msg, key):
    #HANDLING MSG
    msg = vigenere_formatter(msg)
    msg = vigenere_translator(msg)
    #HANDLING KEY
    key = vigenere_formatter(key)
    key = vigenere_translator(key)
    key.extend(msg)

    return vigenere_cipherer(msg, key)

def vigenere_auto_plain_decryptor(cipher, key):
    #HANDLING CIPHER
    cipher = vigenere_formatter(cipher)
    cipher = vigenere_translator(cipher)
    # handling key
    key = vigenere_formatter(key)
    key = vigenere_translator(key)

    msg = []
    for i in range(len(cipher)):
        msg.append((cipher[i] - key[i] + 26) % 26)
        key.append((cipher[i] - key[i] + 26) % 26)

    plain_text = [number_to_letter[n] if isinstance(n, int) else n for n in msg]
    return "".join(plain_text)

def vigenere_auto_cipher_encryptor(msg, key):
    # HANDLING MSG
    msg = vigenere_formatter(msg)
    msg = vigenere_translator(msg)
    # HANDLING KEY
    key = vigenere_formatter(key)
    key = vigenere_translator(key)

    cipher = []
    for i in range(len(msg)):
        cipher.append((key[i] + msg[i]) % 26)
        key.append((key[i] + msg[i]) % 26)

    cipher_text = [number_to_letter[n] if isinstance(n, int) else n for n in cipher]
    return "".join(cipher_text).upper()

def vigenere_auto_cipher_decryptor(cipher, key):
    # HANDLING CIPHER
    cipher = vigenere_formatter(cipher)
    cipher = vigenere_translator(cipher)
    # handling key
    key = vigenere_formatter(key)
    key = vigenere_translator(key)
    key.extend(cipher)

    return vigenere_decipherer(cipher, key)