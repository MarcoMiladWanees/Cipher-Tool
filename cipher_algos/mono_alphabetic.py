import string


def mono_encryptor(msg, key):
    key       = key.lower()
    values    = list(key.replace(" ", ""))
    values    = list(dict.fromkeys(values))
    remaining = [l for l in string.ascii_lowercase if l not in values]
    values    +=remaining
    keys      = [l for l in string.ascii_lowercase]
    table     = dict(zip(keys, values))
    encrypted_msg = ""
    for letter in msg:
        if letter.isalpha():
            encrypted_msg += table[letter.lower()]
        else:
            encrypted_msg += letter
    return encrypted_msg.upper()

def mono_decryptor(cipher, key):
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
    for letter in cipher:
        if letter.isalpha():
            msg += table[letter.lower()]
        else:
            msg += letter
    return msg.lower()