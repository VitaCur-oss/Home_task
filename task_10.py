# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток,
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.

from random import randint

count_coins = int(input('Введите количество монеток: '))
eagle_of_coin = 0
tail_of_coin = 0
coins = 0

for i in range(count_coins):
    coins = randint(0, 1)
    print(coins, end=' ')
    if coins == 0:
        eagle_of_coin += 1
    else:
        tail_of_coin += 1
if eagle_of_coin < tail_of_coin:
    print(sep='')
    print(f'Min coins to turn = eagle_of_coin({eagle_of_coin})')
elif tail_of_coin == eagle_of_coin:
    print(sep='')
    print('You can turn any coin')
else:
    print(sep='')
    print(f'Min coins to turn = tail_of_coin({tail_of_coin})')
