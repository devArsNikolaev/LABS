import random


class Person:

    moods = ['ужасно', 'плохо', 'нормально', 'хорошо', 'прекрасно', 'никак']

    def __init__(self, name, surname, age, mood=random.randint(1, 5)):
        self.name = name
        self.surname = surname
        self.age = age
        self.mood = mood

    def do_better(self):
        if self.mood+1 <= 5:
            self.mood += 1

    def do_worse(self):
        if self.mood - 1 >= 1:
            self.mood -= 1

    def grow(self, years):
        self.age += years
        if (self.age >= 122) or (self.age < 0 ):
            self.die()

    def state(self):
        print(self.name, self.surname, self.age)
        print('настроение:', Person.moods[self.mood-1])

    def born_year(self, this_year):
        return this_year-self.age

    def die(self):
        self.age = 'умер'
        self.mood = 6


Artem = Person('Артём', 'Куклевский', 16)
Artem.state()

while True:
    choose = input('сделать счастливее - 1, сделать несчастнее - 2, стать старше на год - 3, убить - 4, выход - 5\n')
    if choose == '1':
        Artem.do_better()
        Artem.state()
    elif choose == '2':
        Artem.do_worse()
        Artem.state()
    elif choose == '3':
        Artem.grow(1)
        i = random.randint(1, 5)
        Artem.mood = i

        d = random.randint(1, 100)
        if d == 1:
            Artem.die()
            Artem.state()
            break

        Artem.state()
    elif choose == '4':
        Artem.die()
        Artem.state()
        break
    elif choose == '4':
        break
