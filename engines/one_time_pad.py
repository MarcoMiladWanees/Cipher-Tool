import random

def one_time_pad(msg, key = ""):
    msg = msg.replace(" ", "")
    if not key:
        key = [str(random.randint(0, 1)) for _ in range(len(msg))]
    else:
        i = 0
        while len(key) < len(msg):
            key += key[i % len(key)]
            i += 1

    cipher = ""
    for i in range(len(msg)):
        cipher += str(int(msg[i]) ^ int(key[i]))

    return f"output: {cipher} | Key = {"".join(key)}"
