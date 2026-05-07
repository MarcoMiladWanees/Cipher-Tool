
def rail_fence_settings(columns, depth):
    #creating the fence
    fence = []
    for _ in range(depth):
        fence.append( ["" for _ in range(columns) ] )

    return fence

def rail_fence_filler(text, fence ,depth):
    # filling the fence
    rows = [i for i in range(depth)]
    column = 0

    for row in rows:
        if column < len(text):
            fence[row][column] = text[column]
            column += 1

    while column < len(text):
        for row in reversed(rows[: -1]):
            if column < len(text):
                fence[row][column] = text[column]
                column += 1
            else:
                break

        for row in rows[1:]:
            if column < len(text):
                fence[row][column] = text[column]
                column += 1
            else:
                break
    return fence

def rail_fence_encryptor(msg, depth):
    #setting things up
    fence = rail_fence_settings( len(msg) , depth )

    #filling the fence
    fence = rail_fence_filler(msg, fence, depth)

    #handling the cipher
    cipher = []
    for row in fence:
        for item in row:
            if item != "":
                cipher.append(item)

    return "".join(cipher)

def rail_fence_decryptor(cipher, depth):
    # setting things up
    fence = rail_fence_settings( len(cipher) , depth )

    # filling the fence
    filler = "".join( ["X" for _ in range( len(cipher) )] )
    fence = rail_fence_filler(filler, fence, depth)

    column = 0
    for row in fence:
        for i in range(len(row)):
            if row[i]:
                row[i] = cipher[column]
                column += 1

    #handling the message
    msg = []
    for i in range (len(cipher)):
        for row in fence:
            if row[i]:
                msg.append(row[i])

    return "".join(msg)