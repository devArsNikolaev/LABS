count = int(input('Введите количество участниц: '))
people = dict()


for i in range(count):
    message = 'Введите данные ' + str(i+1) + ' участницы\n'
    inp = input(message).split()
    people.append(tuple(inp))


for i in people.keys():
    print(i)