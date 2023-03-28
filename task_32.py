# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random

list1 = [random.randint(-10, 10) for _ in range(15)]
print(list1)

# def is_in_range(arr: list) -> list:
#     values = list(map(int, input('Задайте диапазон: ').split()))
#     return [arr.index(i) for i in arr if i >= values[0] and i <= values[1]]

values = list(map(int, input('Задайте диапазон: ').split()))


def is_in_range2(arr: list) -> list:
    dict1 = {}
    index_list = []
    for i in range(len(arr)):
        dict1[i] = arr[i]
    for k, v in dict1.items():
        if v >= values[0] and v <= values[1]:
            index_list.append(k)
    return index_list


print(is_in_range2(list1))
