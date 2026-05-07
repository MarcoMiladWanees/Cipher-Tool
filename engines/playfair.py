import string

def playfair_grid_maker(key):
    key = key.lower().strip().replace(' ', '').replace('j', 'i') # replace Js with Is
    key = [char for char in key if "a" <= char <= "z"] # filter non ascii letters
    key = list(dict.fromkeys(key)) #remove duplicates

    remaining_letters = [l for l in string.ascii_lowercase if l not in key] #create a list with the remaining letters
    remaining_letters.remove('j') # remove j from the remaining letters list

    key.extend(remaining_letters) # add the remaining letters to the key

    key_map = [[],[],[],[],[]] # create the grid
    pos_map = {} # create a dic to store character position in the grid (row, column)

    #add the letters to the grid and their positions to the pos dic
    column = 0
    row = 0
    for letter in key:
        if column > 4:
            row += 1
            column = 0
        key_map[row].append(letter)
        pos_map[letter] = (row,column)
        column += 1

    return key_map, pos_map

def playfair_plaintext_formatter(msg):
    msg = msg.lower().replace('j', 'i')
    msg = [char for char in msg if "a" <= char <= "z"]

    #add a filler char between repeated letters
    index = 0
    while index < (len(msg) - 1):
        if msg[index] == 'x':
            if msg[index] == msg[index + 1]:
                msg.insert(index + 1, 'q')
            index += 2

        else :
            if msg[index] == msg[index + 1]:
                msg.insert(index + 1, 'x')
            index += 2

    #add a filler char at the end if the msg len isn't even
    if len(msg) % 2 != 0:
        if msg[-1] == 'x':
            msg.append('q')
        else:
            msg.append('x')

    digraphs = []
    for i in range (0, len(msg) - 1, 2):
        digraphs.append( (msg[i], msg[i + 1]) )

    return digraphs

def playfair_ciphertext_parser(cipher):
    cipher = cipher.lower().replace('j', 'i')
    cipher = [char for char in cipher if "a" <= char <= "z"]
    digraphs = []

    for i in range(0, len(cipher) - 1, 2):
        digraphs.append((cipher[i], cipher[i + 1]))

    return digraphs

def playfair_encryptor(msg, key):
    key_map, pos_map = playfair_grid_maker(key)
    digraphs = playfair_plaintext_formatter(msg)
    cipher = []

    for di in digraphs:
        row_a , column_a = pos_map[di[0]]
        row_b, column_b = pos_map[di[1]]

        if row_a == row_b: # if the two letters are in the same row
            cipher.append(key_map[row_a][(column_a + 1) % 5])
            cipher.append(key_map[row_b][(column_b + 1) % 5])

        elif column_a == column_b: # if the two letters are in the same column
            cipher.append(key_map[(row_a + 1) % 5][column_a])
            cipher.append(key_map[(row_b + 1) % 5][column_b])

        else: #rectangle shift rule
            cipher.append(key_map[row_a][column_b])
            cipher.append(key_map[row_b][column_a])

    return "".join(cipher).upper()

def playfair_decryptor(cipher, key):
    key_map, pos_map = playfair_grid_maker(key)
    digraphs = playfair_ciphertext_parser(cipher)
    plain = []

    for di in digraphs:
        row_a, column_a = pos_map[di[0]]
        row_b, column_b = pos_map[di[1]]

        if row_a == row_b:  # if the two letters are in the same row
            plain.append(key_map[row_a][(column_a - 1) % 5])
            plain.append(key_map[row_b][(column_b - 1) % 5])

        elif column_a == column_b:  # if the two letters are in the same column
            plain.append(key_map[(row_a - 1) % 5][column_a])
            plain.append(key_map[(row_b - 1) % 5][column_b])

        else:  # rectangle shift rule
            plain.append(key_map[row_a][column_b])
            plain.append(key_map[row_b][column_a])

    return "".join(plain).lower()