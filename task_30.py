# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент,
# разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии:
# an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


def list_of_slice() -> list:
    value = list(map(int, input('Введите начальное значение списка, шаг, длинну через пробел: ').split()))
    return [item for item in range(value[0], value[0] + (value[2] * value[1]), value[1])]
    # new_list = [value[0]]
    # for i in range(1, value[2]):
    #     new_list.append(new_list[-1] + value[1])
    # return new_list


print(*list_of_slice())
