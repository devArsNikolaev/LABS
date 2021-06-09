try:
    a = int(input('Введите цену в рублях: '))
    b = int(input('Введите цену в копейках: '))
    c = int(input('Введите сумму в рублях: '))
    d = int(input('Введите сумму в копейках: '))
    if b > 99:
        a += b // 100
        b = b % 100
    if d > 99:
        c += d // 100
        d = d % 100

    price = a * 100 + b
    inp = c * 100 + d
    ref = inp - price
    if ref < 0:
        raise Exception
    print('Сдача составит', ref // 100, 'рублей', ref % 100, 'копеек')
except ValueError:
    print('Вы ввели что-то не то...')
except Exception:
    print('У Вас недостаточно денег')
