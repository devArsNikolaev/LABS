N = int(input('Введите количество слов: '))
words = dict()
for i in range(N):
    eng = input('Введите слово на английском:')
    rus = input('Введите перевод этого слова на русском: ')
    rus = rus.split()
    words[eng] = rus

M = int(input('сколько слов нужно найти? '))
for i in range(M):
    find = input('Введите слово на русском: ')
    for i in words.keys():
        for j in words[i]:
            if find == j:
                print(i)