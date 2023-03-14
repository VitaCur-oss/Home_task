# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
import math

sum_of_number = int(input("Введите сумму чисел: "))
multiplication_of_number = int(input("Введите произведение чисел: "))

discriminant = (sum_of_number ** 2) - (4 * multiplication_of_number)
if discriminant >= 0:
    number1 = (sum_of_number + math.sqrt(discriminant)) / 2
    number2 = (sum_of_number - number1)
    print(f'Петя загадал числа {int(number1)} и {int(number2)}')
else:
    print('Петя не правильно посчитал сумму и произведение чисел')




