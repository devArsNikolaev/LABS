import random

def show_results(values):
    cubeprints = [['     ', '     ', '     '],
                  ['     ', '  *  ', '     '],
                  ['*    ', '     ', '    *'],
                  ['*    ', '  *  ', '    *'],
                  ['*   *', '     ', '*   *'],
                  ['*   *', '  *  ', '*   *'],
                  ['* * *', '     ', '* * *']]

    for i in range(3):
        for j in range(len(values)):
            print(cubeprints[values[j]][i], end='     ')
        print()

def play(cubes, rounds):
    for i in range(rounds):
        print('Раунд', i+1)

        pl1_results = [random.randint(1,6) for k in range(cubes)]
        pl2_results = [random.randint(1, 6) for k in range(cubes)]


        pl1_sum = 0
        pl2_sum = 0
        for t in range(cubes):
            pl1_sum += pl1_results[t]
            pl2_sum += pl2_results[t]

        print('Результаты игрока 1:', 'сумма:', pl1_sum)
        show_results(pl1_results)

        print('Результаты игрока 2:', 'сумма:', pl2_sum)
        show_results(pl2_results)

        if pl1_sum > pl2_sum:
            print('ПОБЕДИЛ ИГРОК 1')
        elif pl1_sum < pl2_sum:
            print('ПОБЕДИЛ ИГРОК 2')
        else:
            print('НИЧЬЯ')


while True:
    try:
        inp_cubes = int(input('Введите количество кубов: '))
        inp_rounds = int(input('Введите количество раундов: '))
        break
    except ValueError:
        print('Неверный ввод')

play(inp_cubes, inp_rounds)
