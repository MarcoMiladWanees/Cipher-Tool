import math

def row_transposition_formatter(msg, key):
    msg = list(msg)
    key = list(key.lower().replace(" ", ""))
    return msg, key

def row_transposition_mapper(rows, columns):
    return [["" for _ in range(columns)] for _ in range(rows)]

def row_transposition_column_order(key):
    return sorted(range(len(key)), key=lambda i: key[i])

def row_transposition_encryptor(msg, key):
    msg, key = row_transposition_formatter(msg, key)

    rows = math.ceil(len(msg) / len(key))
    columns = len(key)

    # padding
    while len(msg) < (rows * columns):
        msg.append("x")

    key_map = row_transposition_mapper(rows, columns)

    # fill row-wise
    index = 0
    for row in range(rows):
        for column in range(columns):
            key_map[row][column] = msg[index]
            index += 1

    # read columns in sorted-key order
    cipher = []
    order = row_transposition_column_order(key)

    for column in order:
        for row in range(rows):
            cipher.append(key_map[row][column])

    return "".join(cipher)

def row_transposition_decryptor(cipher, key):
    cipher, key = row_transposition_formatter(cipher, key)

    columns = len(key)

    # ciphertext length must perfectly fill rectangle
    if len(cipher) % columns != 0:
        raise ValueError(
            "Ciphertext length must be divisible by key length."
        )

    rows = len(cipher) // columns

    key_map = row_transposition_mapper(rows, columns)

    # fill columns in sorted-key order
    order = row_transposition_column_order(key)

    index = 0
    for column in order:
        for row in range(rows):
            key_map[row][column] = cipher[index]
            index += 1

    # read row-wise
    msg = []
    for row in range(rows):
        for column in range(columns):
            msg.append(key_map[row][column])

    return "".join(msg)