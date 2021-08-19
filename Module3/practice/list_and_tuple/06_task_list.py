# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число

# TODO: your code here

first_number = int(input())
second_number = int(input())
new_list = []
for ran in range(first_number, second_number):
    if ran % 3 == 0:
        new_list.append(ran)
print(new_list)
