class Specialist:

    def __init__(self, name, surname, qualification=1):
        self.name = name
        self.surname = surname
        self.qualification = qualification

    def info(self):
        inf = self.name + ' ' + self.surname + ', квалификация - ' + str(self.qualification)
        return inf

    def __del__(self):
        print('До свидания, мистер', self.surname)


S1 = Specialist('Иван', 'Голунов')
S2 = Specialist('Иван', 'Дорн', qualification=2)
S3 = Specialist('Иван', 'Рябой', qualification=3)

print(S1.info())
print(S2.info())
print(S3.info())

print()

