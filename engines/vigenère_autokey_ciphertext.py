from engines.vigenere import vigenere_key_formatter


def vigenere_auto_cipher_encryptor(msg, key):
   key = vigenere_key_formatter(key)

   cipher = []
   i = 0
   for char in msg:
       if 'a' <= char.lower() <= 'z':
           if char.islower():
               base = ord("a")
           elif char.isupper():
               base = ord("A")

           pos = (ord(char) - base)
           char_in_numbers = (pos + key[i % len(key)]) % 26
           key.append(char_in_numbers)
           cipher.append(chr(char_in_numbers + base))
           i += 1
       else:
           cipher.append(char)

   return "".join(cipher)


def vigenere_auto_cipher_decryptor(cipher, key):
    key = vigenere_key_formatter(key)

    plain = []
    i = 0
    for char in cipher:
        if 'a' <= char.lower() <= 'z':
            if char.islower():
                base = ord("a")
            elif char.isupper():
                base = ord("A")

            pos = (ord(char) - base)
            key.append(pos)
            char_in_numbers = ((pos - key[i % len(key)]) + 26) % 26
            plain.append(chr(char_in_numbers + base))
            i += 1
        else:
            plain.append(char)

    return "".join(plain)