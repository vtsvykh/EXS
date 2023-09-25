'''
Задание 7.
Дано предложение. Найти длину его самого короткого слова.
'''

text = input()
word = text.split()

short_word = min(word, key=len)

print(len(short_word))

'''
text = input()
word = text.split()
D = []

for i in range(len(word)):
    D.append(len(word[i]))

len = min(D)

print(len)
'''

