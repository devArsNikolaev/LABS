string = input('Введите строку')

a1 = input('введите первый символ')
a2 = input('введите второй символ')

if (a1 in string) and (a2 in string):
    for i in range(len(string)):
        if string[i] == a1:
            b1 = i
    for i in range(len(string)):
        if string[i] == a2:
            b2 = i
    answer = string[:b1+1]+string[b2:]
    print(answer)