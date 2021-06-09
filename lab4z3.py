s = (input('Введите строку: ')).lower()
check = 0
for i in range(len(s)//2):
    if s[i] != s[-1*(i+1)]:
        print('это не палиндром')
        check = 1
        break
if check != 1:
    print('это палиндром')