# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
# 1 2 3 4 5
# 6
# -> 5
import random

length_list = int(input("Введите количество элементов в массиве: "))
number_list = [random.randint(1, 10) for _ in range(length_list)]
x_number = int(input("Введите число X: "))
print(length_list)
print(*number_list)
print(x_number)
print('-> ', end='')

if x_number in number_list:
    index = number_list.index(x_number)
    if 0 < index < len(number_list) - 1:
        section = number_list[index - 1:index + 2]
        section.pop(1)
        if abs(section[0] - x_number) < abs(section[1] - x_number):
            print(section[0])
        else:
            print(section[1])
    elif index == len(number_list) - 1:
        print(number_list[-2])
    else:
        print(number_list[1])
else:
    print(number_list[-1])

