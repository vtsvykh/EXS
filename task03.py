'''
Задание 3.
Дан текст. Определить, сколько различных букв в нем.
'''

text = input()
s = ''

for i in text:
    if i not in s:
        s += i

print(len(s))
