import random


a = 20
b = 20
c = 1
d = 43
M = [[random.randint(c, d) for i in range(a)] for j in range(b)]

while True:
    try:
        k = int(input('Введите i: '))
        break
    except ValueError:
        print('Неверный ввод')

print('изначальный массив:')
for i in range(a):
    for j in range(b):
        try:
            if M[i][j] % 10 == M[i][j]:
                en = '  '
            else:
                en = ' '
        except TypeError:
            en = '  '

        print(M[i][j], end=en)
        if M[i][j] > k:
            M[i][j] = '-'

    print()

print('новый массив: ')
for i in range(a):
    for j in range(b):

        try:
            if M[i][j] % 10 == M[i][j]:
                en = '  '
            else:
                en = ' '
        except TypeError:
            en = '  '

        print(M[i][j], end=en)
    print()
