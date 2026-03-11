import string


def encryption(key, message):
    key       = key.lower()
    values    = list(key.replace(" ", ""))
    values    = list(dict.fromkeys(values))
    remaining = [l for l in string.ascii_lowercase if l not in values]
    values    +=remaining
    keys      = [l for l in string.ascii_lowercase]
    table     = dict(zip(keys, values))
    encrypted_msg = ""
    for letter in message:
        if letter.isalpha():
            encrypted_msg += table[letter.lower()]
        else:
            encrypted_msg += letter
    return encrypted_msg.upper()
encryption("MMaarrccoo","marco" )

def decryption(key, encrypted_message):
    key       = key.lower()
    values    = list(key.replace(" ", ""))
    key       = key.lower()
    values    = list(key.replace(" ", ""))
    values    = list(dict.fromkeys(values))
    remaining = [l for l in string.ascii_lowercase if l not in values]
    values   += remaining
    keys      = [l for l in string.ascii_lowercase]
    table     = dict(zip(values, keys))
    msg = ""
    for letter in encrypted_message:
        if letter.isalpha():
            msg += table[letter.lower()]
        else:
            msg += letter
    return msg.lower()