'''
Задание 12.
Как известно, имя в языке Python может содержать только латинские символы, цифры
и знак подчеркивания "_". При этом, имя не может начинаться с цифры и не может быть
ключевым словом. Напишите программу, которая проверяет введенную строку, может ли
она быть именем в языке Python.
'''

text = input()
keywords = ('and as assert break class continue def del elif else except False finally for from global if import in is '
            'lambda None nonlocal not or pass raise return True try while with yield')
keywords = keywords.split()
alp = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
res = 0

if text.startswith(' ') or text[0].isdigit():
    res = 'Ваш логин ' + text + ' не соотвествует требованиям!'
else:
    res = 'Ваш логин ' + text + ' подходит!'

for i in range(len(keywords)):
    if keywords[i] in text:
        res = 'Ваш логин ' + text + ' не соотвествует требованиям!'

for i in range(len(text) - 1):
    if text[i].lower() in alp:
        res = 'Ваш логин ' + text + ' не соотвествует требованиям!'

print(res)
