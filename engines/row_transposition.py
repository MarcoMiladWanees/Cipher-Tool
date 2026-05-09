import math


def row_transposition_formatter(msg, key):
    # Standardize msg and key to lists without destructive filtering
    # Removed .lower() and .replace() to support numeric/raw keys
    return list(msg), list(key)


def row_transposition_mapper(rows, columns):
    return [["" for _ in range(columns)] for _ in range(rows)]


def row_transposition_column_order(key):
    # Rank-based mapping: handles '9,1,5', 'BAC', or any unique sequence
    # Returns the original indices in the order of their sorted values
    return sorted(range(len(key)), key=lambda i: key[i])


def row_transposition_encryptor(msg, key):
    msg, key = row_transposition_formatter(msg, key)

    columns = len(key)
    rows = math.ceil(len(msg) / columns)

    # Padding with 'x' to fill the rectangle
    while len(msg) < (rows * columns):
        msg.append("x")

    key_map = row_transposition_mapper(rows, columns)

    # Fill the grid row-wise
    index = 0
    for r in range(rows):
        for c in range(columns):
            key_map[r][c] = msg[index]
            index += 1

    # Read columns based on key rank order
    cipher = []
    order = row_transposition_column_order(key)

    for col_idx in order:
        for r in range(rows):
            cipher.append(key_map[r][col_idx])

    return "".join(cipher)


def row_transposition_decryptor(cipher, key):
    cipher, key = row_transposition_formatter(cipher, key)

    columns = len(key)
    # Validation check: length must be compatible with grid
    if len(cipher) % columns != 0:
        raise ValueError("Ciphertext length must be divisible by key length.")

    rows = len(cipher) // columns
    key_map = row_transposition_mapper(rows, columns)

    # Determine the order columns were read during encryption
    order = row_transposition_column_order(key)

    # Fill columns in sorted-key order
    index = 0
    for col_idx in order:
        for r in range(rows):
            key_map[r][col_idx] = cipher[index]
            index += 1

    # Read row-wise to recover the message
    msg = []
    for r in range(rows):
        for c in range(columns):
            msg.append(key_map[r][c])

    return "".join(msg)