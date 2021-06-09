def collatz(inp):
    if inp % 2 == 0:
        return inp // 2
    else:
        return 3*inp + 1


while True:
    try:
        N = int(input('Введите число: '))
        break
    except ValueError:
        print('Неверный ввод')

result = N
while result != 1:
    result = collatz(result)
    print(result, end=' ')

