import string
import random


def cetak(num):
    data = []
    while len(data) < num:
        rand = random_string(32)
        if rand not in data:
            data.append(rand)
            print(rand)


def random_string(length: int):
    chars = "abcdefghijklmnopqrstufwxyzABCDEFGHIJKLMNOPQRSTUFWXYZ1234567890"
    return "".join(random.choice(chars) for x in range(length))


cetak(2)
