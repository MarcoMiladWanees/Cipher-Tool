from assets.letters_dic import letter_to_number
import math

def row_transposition_formatter(msg, key):
    key = key.replace(' ', '').lower()
    key = list(dict.fromkeys(key))
    msg = msg.replace(' ', '')
    msg = list(msg)
    for i in range(len(key)):
        if key[i].isalpha():
           key[i] = letter_to_number[key[i]]


    return msg, key

def row_transposition_mapper(text, key):

    rows = math.ceil(len(text) / len(key))
    key_map = []
    for _ in range(rows):
        key_map.append([" " for _ in range(len(key))])
    return key_map

def row_transposition_encryptor(msg, key):
    msg, key = row_transposition_formatter(msg, key)
    key_map = row_transposition_mapper(msg, key)

    #filling the key map
    for row in key_map:
        for i in range(len(key)):
            if msg:
                row[i] = msg[0]
                del msg[0]
            else:
                row[i] = "x"

    #adding the key row to the keymap
    key_map.insert(0,list(key))

    #extracting the cipher from the keymap
    key = sorted(key)
    cipher = ""
    column = 0
    while column < len(key):
        for row in range(1,len(key_map)):
            cipher += key_map[row][key_map[0].index(key[column])]
        column += 1

    return cipher.upper()

def row_transposition_decryptor(cipher, key):
    cipher, key = row_transposition_formatter(cipher, key)
    key_map = row_transposition_mapper(cipher, key)

    # adding the key row to the keymap
    key_map.insert(0, key)

    #filling the key map
    key = sorted(key)
    column = 0
    i = 0
    while column < len(key):
        for row in range(1, len(key_map)):
            key_map[row][key_map[0].index(key[column])] = cipher[i]
            i += 1
        column += 1

    #extracting the message from the key map
    msg = ""
    for row in range(1, len(key_map)):
        for i in range(len(key)):
            msg += key_map[row][i]
    return msg.lower()

