# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

# TODO: your code here

import random
sum = 0
random_el = []
n = random.randint(10,1500)
for i in range (1,n):
    random_number = random.randint(-10,10)
    random_el.append( random_number)
for el in random_el:
    if el > 0:
        sum += el
print(sum)
