# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

numb = int(input("Введите число: "))
pow = int(input("Введите степень: "))


def power(number, degree):
    if degree == 0:
        return 1
    return number * power(number, degree - 1)


numb_pow = power(numb, pow)
print(f'Число {numb} в степень {pow} = {numb_pow}')
