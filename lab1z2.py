import math
x = int(input('Введите х: '))
a = float(input('Введите a: '))
b = float(input('Введите b: '))
print( format(((x**2 + b )**(1 / 5 )-( b**2 * math.sin( x + a )**3 ) / x),'0.4f') )
