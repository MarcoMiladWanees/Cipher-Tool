import string
def mono_key_formatter(key):
    key = key.lower()
    key = [char for char in key if "a" <= char <= "z"] # filter non ascii letters
    key = list(dict.fromkeys(key))
    remaining = [l for l in string.ascii_lowercase if l not in key]
    key.extend(remaining)
    return key

def mono_encryptor(msg, key):
    key = mono_key_formatter(key)
    table = dict(zip(string.ascii_lowercase, key))
    encrypted_msg = ""

    for char in msg:
        if 'a' <= char.lower() <= 'z':
            if char.isupper():
                encrypted_msg += table[char.lower()].upper()
            else:
                encrypted_msg += table[char.lower()].lower()
        else:
            encrypted_msg += char

    return encrypted_msg

def mono_decryptor(cipher, key):
    key = mono_key_formatter(key)
    table = dict(zip(key, string.ascii_lowercase))
    msg = ""

    for char in cipher:
        if 'a' <= char.lower() <= 'z':
            if char.isupper():
                msg += table[char.lower()].upper()
            else:
                msg += table[char.lower()].lower()

        else:
            msg += char

    return msg