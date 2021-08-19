# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here


import random
sum = 0
for i in range (1,201):
    random_number = random.randint(-100,101)
    if random_number * -1 < 0 and random_number % 2 == 0:
        sum += random_number
print(sum)
