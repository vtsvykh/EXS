'''
Задание 7.
Дано предложение. Найти длину его самого короткого слова.
'''

text = input()
word = text.split()
D = []

for i in range(len(word)):
    D.append(len(word[i]))

len = min(D)

print(len)

'''
text = input()
word = text.split()
d = 
shortest_word = min(word)
print(shortest_word)
'''