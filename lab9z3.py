def step(a, n):
    result = 1
    for i in range(n):
        result *= a
    return result


while True:
    try:
        A = int(input('Возвести число: '))
        N = int(input('В степень: '))
        break
    except ValueError:
        print('Неверный ввод')


print('Ответ:', step(A, N))
