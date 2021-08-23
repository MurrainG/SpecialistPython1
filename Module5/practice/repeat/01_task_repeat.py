import random


def gen_list(size, of, to):
    new_list = []
    for _ in range(size):
        number = random.randint(of, to)
        new_list.append(number)
    return new_list


print(gen_list(123, -1293120, 1276351))

