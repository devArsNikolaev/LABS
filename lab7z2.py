inp = input('Введите строку из нескольких слов:\n').split()

saved = set()
for i in inp:
    if i in saved:
        print('yes')
    else:
        saved.add(i)
        print('no')
