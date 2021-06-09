import math

try:
    a = int(input('введите левую границу отрезка: '))
    b = int(input('введите правую границу отрезка: '))
    h = int(input('введите шаг: '))
    if a >= b:
        correct_input = False
    elif h > b-a:
        correct_input = False
    else:
        correct_input = True

except ValueError:
    correct_input = False

if correct_input:
    print('x  ','y')
    for i in range (a, b+1, h):
        print(str(i).format('4d'), format(i**2 - math.sin(i),'3.2f'))