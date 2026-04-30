def vernam_cipherer(msg, key):
    msg = msg.replace(" ", "")
    i = 0
    while len(key) < len(msg):
            key += key[i % len(key)]
            i += 1

    # msg_bin = "".join(format(ord(c), "08b") for c in msg)
    # key_bin = "".join(format(ord(c), "08b") for c in key_bin)
    cipher = ""
    for i in range(len(msg)):
        cipher += str(int(msg[i]) ^ int(key[i]))

    # cipher_ascii = ""
    # for i in range(0, len(msg_bin),8):
    #     byte = int(cipher[i:i+8], 2)
    #     cipher_ascii += chr(byte)
    return cipher
