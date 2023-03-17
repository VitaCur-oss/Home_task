
# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
# 1 2 3 4 5
# 3
# -> 1
import random
length_list = int(input("Введите количество элементов в массиве: "))
number_list = [random.randint(1, 5) for _ in range(length_list)]
x_number = int(input("Введите число X: "))
print(length_list)
print(number_list)
print(x_number)
print(f' -> {number_list.count(x_number)}')
