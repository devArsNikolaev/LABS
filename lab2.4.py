try:
    year = int(input('Введите год: '))
    if (year % 4 == 0) and (year % 400 == 0) or (year % 100 != 0):
        print('Год високосный')
    else:
        print('Год не високосный')
except ValueError:
    print('вы ввели неверный год')
