import string

def construct_key_map(key):
    key_map = []
    key = key.lower()
    for i in range(5):
        key_map.append([0, 0, 0, 0, 0])
    key = key.replace(' ', '')
    key = key.replace('j', '')
    key = list(key)
    key = list(dict.fromkeys(key))
    remaining_letters = [l for l in string.ascii_lowercase if l not in key]
    remaining_letters.remove('j')
    for i in range(5):
        for j in range(5):
            if key:
                key_map[i][j] = (key[0])
                del key[0]
            else:
                break
    for i in range(5):
        for j in range(5):
            if key_map[i][j] == 0:
                key_map[i][j] = remaining_letters[0]
                del remaining_letters[0]
            else:
                continue

    return key_map

def playfair_formater(msg, key):
    key_map = construct_key_map(key)

    msg = msg.lower()
    msg = msg.replace(' ', '')
    msg = msg.replace('j', 'i')
    msg = [letter for letter in msg if letter.isalpha()]

    i = 0
    while i < (len(msg) - 1):
        if msg[i] == msg[i + 1]:
            msg.insert(i + 1, 'x')
        i += 2

    if len(msg) % 2 != 0:
        msg.append('x')

    cipher = msg.copy()
    indexes = []

    for i in range(len(msg)):
        for j in range(5):
            if msg[i] in key_map[j]:
                indexes.append([j, key_map[j].index(msg[i])])

    return cipher, indexes, key_map

def playfair_encryptor(msg, key):

    cipher,indexes, key_map = playfair_formater(msg, key)

    for i in range(0,len(indexes)-1,2):
        row_a = indexes[i][0]
        column_a = indexes[i][1]
        row_b = indexes[i + 1][0]
        column_b = indexes[i + 1][1]
        if row_a == row_b:
            if column_a == 4:
                cipher[i] = key_map[row_a][0]
            else:
                cipher[i] = key_map[row_a][column_a + 1]
            if column_b == 4:
                cipher[i+1] = key_map[row_b][0]
            else:
                cipher[i+1] = key_map[row_b][column_b + 1]
        elif column_a == column_b:
            if row_a == 4:
                cipher[i] = key_map[0][column_a]
            else:
                cipher[i] = key_map[row_a + 1][column_a]
            if row_b == 4:
                cipher[i+1] = key_map[0][column_b]
            else:
                cipher[i+1] = key_map[row_b + 1][column_b]
        else:
            cipher[i] = key_map[row_a][column_b]
            cipher[i+1] = key_map[row_b][column_a]

    return "".join(cipher).upper()

def playfair_decryptor(cipher, key):

    text, indexes, key_map = playfair_formater(cipher, key)

    for i in range(0, len(indexes) - 1, 2):
        row_a = indexes[i][0]
        column_a = indexes[i][1]
        row_b = indexes[i + 1][0]
        column_b = indexes[i + 1][1]

        if row_a == row_b:
            if column_a == 0:
                text[i] = key_map[row_a][4]
            else:
                text[i] = key_map[row_a][column_a - 1]
            if column_b == 0:
                text[i + 1] = key_map[row_b][4]
            else:
                text[i + 1] = key_map[row_b][column_b - 1]
        elif column_a == column_b:
            if row_a == 0:
                text[i] = key_map[4][column_a]
            else:
                text[i] = key_map[row_a - 1][column_a]
            if row_b == 0:
                text[i + 1] = key_map[4][column_b]
            else:
                text[i + 1] = key_map[row_b - 1][column_b]
        else:
            text[i] = key_map[row_a][column_b]
            text[i + 1] = key_map[row_b][column_a]

    return "".join(text).lower()
