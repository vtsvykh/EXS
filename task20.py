'''
Задание 20.
Дано натуральное число не превосходящее 900 000 000. Напишите программу, которая
выводит на экран это число русскими словами.
'''

num = int(input())
s_units = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', '']
s = ['одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать', '']
s_tens = ['десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто', '']
s_hundreds = ['сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот', '']
s_thousands = ['тысяча', 'тысячи', 'тысяч']
s_1 = ['две']


if num == 0:
    print('ноль')

if 1 <= num < 10:
    print(s_units[num - 1])

if 10 < num < 20:
    units = num % 10
    print(s[units - 1])

if 20 <= num < 100 or num == 10:
    tens = num // 10
    units = num % 10
    print(s_tens[tens - 1], s_units[units - 1])

if 100 <= num < 1000:
    v = num % 100
    if 11 <= v <= 19:
        hundreds = num // 100
        a = num % 10
        print(s_hundreds[hundreds - 1], s[a - 1])
    else:
        hundreds = num // 100
        tens = num % 100 // 10
        units = num % 10
        print(s_hundreds[hundreds - 1], s_tens[tens - 1], s_units[units - 1])

if 1000 <= num < 10000:
    v = num % 100
    if 1000 <= num <= 1999:
        if 11 <= v <= 19:
            thousands = num // 1000
            hundreds = num % 1000 // 100
            a = num % 10
            print(s_thousands[0], s_hundreds[hundreds - 1], s[a - 1])
        else:
            thousands = num // 1000
            hundreds = num % 1000 // 100
            tens = num % 100 // 10
            units = num % 10
            print(s_thousands[0], s_hundreds[hundreds - 1], s_tens[tens - 1], s_units[units - 1])
    if 2000 <= num <= 2999:
        v = num % 100
        if 11 <= v <= 19:
            thousands = num // 1000
            hundreds = num % 1000 // 100
            a = num % 10
            print(s_1[0], s_thousands[1], s_hundreds[hundreds - 1], s[a - 1])
        else:
            thousands = num // 1000
            hundreds = num % 1000 // 100
            tens = num % 100 // 10
            units = num % 10
            print(s_1[0], s_thousands[1], s_hundreds[hundreds - 1], s_tens[tens - 1], s_units[units - 1])
    if 3000 <= num <= 4999:
        v = num % 100
        if 11 <= v <= 19:
            thousands = num // 1000
            hundreds = num % 1000 // 100
            a = num % 10
            print(s_units[thousands - 1], s_thousands[1], s_hundreds[hundreds - 1], s[a - 1])
        else:
            thousands = num // 1000
            hundreds = num % 1000 // 100
            tens = num % 100 // 10
            units = num % 10
            print(s_units[thousands - 1], s_thousands[1], s_hundreds[hundreds - 1], s_tens[tens - 1], s_units[units - 1])
    if 5000 <= num <= 9999:
        v = num % 100
        if 11 <= v <= 19:
            thousands = num // 1000
            hundreds = num % 1000 // 100
            a = num % 10
            print(s_units[thousands - 1], s_thousands[2], s_hundreds[hundreds - 1], s[a - 1])
        else:
            thousands = num // 1000
            hundreds = num % 1000 // 100
            tens = num % 100 // 10
            units = num % 10
            print(s_units[thousands - 1], s_thousands[2], s_hundreds[hundreds - 1], s_tens[tens - 1], s_units[units - 1])

'''
if 10000 <= num <= 99999:
    if 11 <= num // 1000 <= 19:
        if 11 <= num % 100 <= 19:
            v = num // 1000 % 10
            hundreds = num % 1000 // 100
            tens = num % 100 // 10
            a = num % 10
            print(s[v - 1], s_thousands[2], s_hundreds[hundreds - 1], s[a - 1])
        else:
            hundreds = num % 1000 // 100
            tens = num // 10000
            a = num // 1000 % 10
'''

