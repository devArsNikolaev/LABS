class PhoneNumber:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def info(self):
        print(self.name, '-', self.number)

    def getname(self):
        return self.name

    def getnum(self):
        return self.number


class Person(PhoneNumber):
    def __init__(self, name, number, address):
        self.name = name
        self.number = number
        self.address = address

    def info(self):
        print(self.name, '-', self.number, '\n  Адрес:', self.address)


class Company(PhoneNumber):
    def __init__(self, name, number, organization, address):
        self.name = name
        self.number = number
        self.organization = organization
        self.address = address

    def info(self):
        print(self.name, '-', self.number, 'компания:', self.organization, 'по адресу', self.address)


class Friend(PhoneNumber):
    def __init__(self, name, number, address, date):
        self.name = name
        self.number = number
        self.address = address
        self.date = date

    def info(self):
        print(self.name, '-', self.number, 'Адрес:', self.address)


def create(M):
    choose = input('Выберите тип контакта:\n 1 - Знакомый\n 2 - Организация\n 3 - Друг\n').lower()
    k = 0
    if choose in ('знакомый', '1'):
        nam = input('Введите имя: ')
        num = input('Введите номер: ')
        adr = input('Введите адрес: ')
        k = Person(nam, num, adr)

    elif choose in ('организация', '2'):
        nam = input('Введите имя сотрудника: ')
        num = input('Введите номер: ')
        org = input('Введите название организации: ')
        adr = input('введите адрес компании: ')
        k = Company(nam, num, org, adr)

    elif choose in ('друг', '3'):
        nam = input('Введите имя: ')
        num = input('Введите номер: ')
        adr = input('Введите адрес: ')
        brn = input('Введите дату рождения: ')
        k = Friend(nam, num, adr, brn)

    M.append(k)
    print('Контакт успешно создан!')


def show(M):
    for contact in M:
        print(contact.getname(), '///', contact.getnum())


contact_list = []
n = int(input('Количество записей: '))
for i in range(n):
    create(contact_list)
show(contact_list)

n = int(input('вывести данные о контакте номер: ')) - 1
contact_list[n].info()
