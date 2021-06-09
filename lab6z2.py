import random


cols = int(input('Введите количество столбцов'))
rows = int(input('Введите количество строк'))

matrix = [[random.randint(0, 10) for i in range(cols)] for j in range(rows)]
print('Старая матрица')

for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], ' ', end='')
    print()


print('Новая матрица')
matrix1 = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        print(matrix1[i][j], ' ', end='')
    print()
