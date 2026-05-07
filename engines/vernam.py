def vernam_cipherer(msg, key):
    key = [char for char in key if  char == "1" or char == '0']
    msg = [char for char in msg if  char == "1" or char == '0']

    cipher = []
    for i in range(len(msg)):
        cipher.append(str( int(msg[i]) ^ int(key[i % len(key)]) ))

    return "".join(cipher)