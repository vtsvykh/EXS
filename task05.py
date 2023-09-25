'''
Задание 5.
Даны три строки. Выведите на экран только те символы, которые есть лишь в одной из этих трёх строк.
'''
str_1 = input()
str_2 = input()
str_3 = input()

set_1 = set(str_1)
set_2 = set(str_2)
set_3 = set(str_3)

result = set_1 ^ set_2 ^ set_3

print(result)
