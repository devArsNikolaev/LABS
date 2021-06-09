buf1 = 1
buf2 = 1
out = 0
while True:
    try:
        n = int(input('Введите число: '))
        break
    except ValueError:
        print('Вы ввели неправильное число. Попробуйе ещё раз')
print(buf1, buf2,'',end = '')
while out < n:
    if out !=0:
        print(out, '', end = '')
    out = buf1 + buf2
    buf1, buf2 = buf2, out
