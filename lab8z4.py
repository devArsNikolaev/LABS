school = {'1а':25, '1б':24, '1в':23, '2а':26}

print(school)
while True:
    choose = input('1 - изменить кол-во учащихся в классе \n 2 - новый класс\n 3 - удалить класс\n 4 - выход: \n')
    if choose == '1':
        while True:
            class_name = input('Введите класс: ')

            if class_name in school.keys():
                break
            else:
                print('неверный ввод')

        while True:
            try:
                class_new_value = int(input('Введите новое количество учащихся: '))
                school[class_name] = class_new_value
                break
            except ValueError:
                print('неверный ввод')

    elif choose == '2':
        new_class_name = input('введите имя класса: ')

        while True:
            try:
                new_class_value = int(input('Введите количество учащихся: '))
                break
            except ValueError:
                print('неверный ввод')

        school[new_class_name] = new_class_value

    elif choose == '3':
        while True:
            del_class_name = input('введите имя класса: ')
            if del_class_name in school.keys():
                school.pop(del_class_name)
                break
            else:
                print('неверный ввод')
    elif choose == '4':
        break
    else:
        print('неверный ввод')

    print(school)