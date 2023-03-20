# *Задача 20: * В настольной игре Скраб л (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские,
# либо только русские буквы.
# *Пример:*
# ноутбук
# 12
letters = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']
letters_2 = ['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У']
letters_3 = ['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я']
letters_4 = ['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы']
letters_5 = ['K', 'Ж', 'З', 'Х', 'Ц', 'Ч']
letters_6 = ['J', 'X', 'Ш', 'Э', 'Ю']
letters_7 = ['Q', 'Z', 'Ф', 'Щ', 'Ъ']

alfabet_dict = {}

alfabet_dict = dict.fromkeys(letters, 1)
alfabet_dict.update(dict.fromkeys(letters_2, 2))
alfabet_dict.update(dict.fromkeys(letters_3, 3))
alfabet_dict.update(dict.fromkeys(letters_4, 4))
alfabet_dict.update(dict.fromkeys(letters_5, 5))
alfabet_dict.update(dict.fromkeys(letters_6, 8))
alfabet_dict.update(dict.fromkeys(letters_7, 10))
# print(alfabet_dict)
word = input('Введите слово: ')
points = 0
for i in word:
    if i.upper() in alfabet_dict.keys():
        points = points + alfabet_dict[i.upper()]
print(word)
print(points)
