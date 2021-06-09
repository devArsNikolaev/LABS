try:
    x = int(input('Ведите число x: '))
    y = int(input('Ведите число y: '))
    if (x < 0) or (y < 0):
        raise Exception
    print('Ответ: ', (x - (y ** 0.5)) ** 0.5)
except ValueError:
    print('Это были не числа...')
except Exception:
    print('Вы ввели что-то отрицательное :с')
