'''
Задание 2.
Дан текст. Необходимо определить максимальное количество последовательных одинаковых символов в нём.
'''

text = input()
cnt = 1
max_cnt = 1

for i in range(len(text) - 1):
    if text[i] == text[i + 1]:
        cnt += 1
    else:
        if cnt > max_cnt:
            max_cnt = cnt
        cnt = 1

if cnt > max_cnt:
    max_cnt = cnt
else:
    max_cnt = max_cnt

print(max_cnt)
