"Rome is the greatest empire"
# msg = str(input("Enter a msg: "))
# key = int(input("Enter a key: "))

def ceaser_encrypt(msg, key):
    msg = msg.lower()
    cipher = ""
    for char in msg:
        if char.isalpha():
            encrypted_letter = ((ord(char) - 97) + key ) % 26
            cipher += chr(encrypted_letter + 97)
        else:
            cipher += char
    return cipher.upper()

def ceaser_decrypt(cipher, key):
    cipher = cipher.lower()
    msg = ""
    for char in cipher:
        if char.isalpha():
            letter  =  ((ord(char) -97) - key ) % 26
            msg +=  chr(letter + 97)
        else:
            msg += char
    return msg.lower()
