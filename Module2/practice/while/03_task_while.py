# По данному натуральному n выведите лесенку из n ступенек, i-я ступень состоит из чисел от 1 до i без пробелов.
# Формат входных данных: Вводится натуральное число n.
# Формат выходных данных: Выведите ответ на задачу.
# Пример:
# Для n = 4
# Нужно вывести:
# 1
# 12
# 123
# 1234

# TODO: your code here

number = int(input())   
count = 1
sum = 1
while count < number:
    if count == 1:  #сделано на кастылях)
        print(1)
    count += 1
    sum = (str(sum) + str(count))
    print(sum)
