'''
Задание 9.
Дано предложение. В нем только два слова одинаковые. Найти эти слова.
'''

text = input()
word = text.split()

for i in word:
    if word.count(i) == 2:
        word = i

print(word)
