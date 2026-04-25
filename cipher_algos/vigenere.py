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
    key_map = vigenere_formatter(key)
    key_map2 = key_map.copy()
    key = []
    len_key = math.ceil(length / len(key_map))

    # generating key
    for _ in range(len_key):
        key_map2 = key_map.copy()
        while key_map2:
            key.append(key_map2[0])
            del key_map2[0]

    #translating key
    key = vigenere_translator(key)

    return key

def vigenere_encryptor(msg, key):
    #formatting msg
    msg = vigenere_formatter(msg)
    #translating msg
    msg = vigenere_translator(msg)
    #handling key
    key = vigenere_key_generator(len(msg),key)

    #calculating the cipher
    cipher = []
    for i in range(len(msg)):
        if isinstance(msg[i], int):
            cipher.append((key[i] + msg[i]) % 26)
        else:
            cipher.append(msg[i])

    cipher_text = [number_to_letter[n] if isinstance(n, int) else n for n in cipher]
    return "".join(cipher_text).upper()

def vigenere_decryptor(cipher, key):
    # formatting cipher
    cipher = vigenere_formatter(cipher)
    # translating msg
    cipher = vigenere_translator(cipher)
    # handling key
    key = vigenere_key_generator(len(cipher), key)

    # calculating the msg
    msg = []
    for i in range(len(cipher)):
        if isinstance(cipher[i], int):
            msg.append((cipher[i] - key[i] +26) % 26)
        else:
            msg.append(cipher[i])

    plain_text = [number_to_letter[n] if isinstance(n, int) else n for n in msg]
    return "".join(plain_text)



