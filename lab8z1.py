year = {'январь':'01', 'февраль':'02', 'март':'03', 'апрель':'04', 'май':'05', 'июнь':'06', 'июль':'07', 'август':'08', 'сентябрь':'09', 'октябрь':'10', 'ноябрь':'11', 'декабрь':'12'}

while True:
    inp = input('Введите месяц и число: ')
    inp = inp.split()
    inp[1] = int(inp[1])
    if not(inp[0] in year.keys())or not(inp[1]>0 and inp[1]<32):
        print('Неверный ввод')
    else:
        break

month = inp[0]
month = month.lower()
day = inp[1]
print(year[month], '.', day, sep='')