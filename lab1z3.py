import random
a = random.randint(100000, 999999)
print('Случайное число равно', a)
s = 0
for i in range(len(str(a))):
    s += int(str(a)[i])
print('Сумма цифр равна', s)
