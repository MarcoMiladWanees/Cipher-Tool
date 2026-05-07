def caesar_processor(msg, shift):
    cipher = ""
    for char in msg:
        if "a" <= char.lower() <= "z":

            if char.islower():
                base = ord("a")
            elif char.isupper():
                base = ord("A")

            pos = (ord(char) - base)
            encrypted_letter = (pos + shift + 26) % 26
            cipher += chr(encrypted_letter + base)
        else:
            cipher += char
    return cipher