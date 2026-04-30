import random

def one_time_pad(msg, key = ""):
    if not key:
        key = [str(random.randint(0, 1)) for _ in range(len(msg))]

    cipher = ""
    for i in range(len(msg)):
        cipher += str(int(msg[i]) ^ int(key[i]))

    return f"output: {cipher} | Key = {"".join(key)}"
