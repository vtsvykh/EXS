'''
Задание 1.
Дан текст. Необходимо определить максимальное количество последовательных пробельных символов  в нём.
'''

text = input()
cnt = 0
max_cnt = 0

for i in text:
    if i == ' ':
        cnt += 1
    else:
        if cnt > max_cnt:
            max_cnt = cnt
            cnt = 0
        else:
            max_cnt = max_cnt

if cnt > max_cnt:
    max_cnt = cnt
else:
    max_cnt = max_cnt

print(max_cnt)
