'''
Задание 10.
Дано предложение. Выведите на экран те слова, которые отличны от первого слова,
в слове нет повторяющихся букв.
'''

text = input()
word = text.split()

for i in range(len(word)):
    if word[0] != word[i]:
        if len(set(word[i])) == len(word[i]):
            res = word[i]
            print(res, end=' ')
