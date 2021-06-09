try:
    a = int(input('Введите число А: '))
    b = int(input('Введите число В: '))
    c = int(input('Введите число C: '))
    print( 'ответ:',abs( (-5*a**3 + b/5)**2 - c%3 ) * 7)
except ValueError:
    print('Введены неверные значения')