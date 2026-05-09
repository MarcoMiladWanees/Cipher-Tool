import re

#profiles are meant to have the common rules of ciphers
#some algos require their own special set of rules; hence their own extra validators
#all functions return False if there are no issues

#Profile A is for Caesar, Mono, Vigenere, Autokeys
#Profile B is for Playfair
#Profile C is for Row Trans and Rail fence
#profile D is for Vernam and OTP

def validator_A_B(text):
    if re.search(r"[a-zA-Z]", text): #make sure the message contains at least 1 english alphabetic character
        return False

    return True

def validator_C(text):
    return not bool(text and text.strip()) # make sure the message is not only white spaces

def validator_D(text):
    bits = text.strip().replace(" ", "")
    if bits and not set(bits).issubset({"0", "1"}):
        return True
    return False

def validator_playfair_decrypt(text):
    text = list(re.findall(r"[a-zA-Z]", text))
    if text and len(text) % 2 == 0: # make sure the cipher text is there and is of an even length
        return False
    return True

def validator_row_trans_key(key):
    error = False
    if not key: # make sure there's a key
        error = True

    if len(key) < 2: #make sure the key's length is more than 1
        error = True

    #make sure the key is either fully numeric or fully alphabetic
    if not re.fullmatch(r"[a-zA-Z]+", key) and not re.fullmatch(r"[0-9]+", key) :
        error = True

    #make sure the key has no duplicates
    if not len(list(key)) == len(set(key)):
        error = True

    return error

def validator_row_trans_decrypt(cipher, key):
    key = key.strip().replace(" ", "")
    cipher = cipher.strip()

    if key and cipher and (len(cipher) % len(key)) == 0:
        return False
    return True