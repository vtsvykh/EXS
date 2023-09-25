'''
Задание 6.
Дано предложение. Напечатать его в обратном порядке слов.
'''

text = input()
word = text.split()

reversed_text = word[::-1]

print(*reversed_text)
