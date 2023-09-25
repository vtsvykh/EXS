'''
Задание 8.
Дано предложение. Напечатать все его слова в порядке неубывания их длин.
'''

text = input()
word = text.split()
word = sorted(word, reverse=False, key=len)

print(*word)
