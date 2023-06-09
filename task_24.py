# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке,
# причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора
# на них выросло различное число ягод – на i-ом кусте выросло ai ягод. В этом фермерском хозяйстве
# внедрена система автоматического сбора черники. Эта система состоит из  управляющего модуля и нескольких
# собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним. Напишите программу для нахождения максимального
# числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки
import random

set_fruits = list(set(random.randint(1, 10) for _ in range(10)))
print(set_fruits)
list_max = []

for i in range(0, len(set_fruits)):
    if i != len(set_fruits) - 1:
        list_max.append(set_fruits[i] + set_fruits[i + 1] + set_fruits[i - 1])
    else:
        list_max.append(set_fruits[i] + set_fruits[0] + set_fruits[i - 1])

print(list_max)
print(max(list_max))
