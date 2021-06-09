class Employee:


    def __init__(self, name, job='программист'):
        self.job = job
        self.name = name

    def info(self):
        print(self.name, ', должность -', self.job)


Ivan = Employee('Иван')
Ivan.info()

Terentiy = Employee('Терентий', job='уборщик')
Terentiy.info()
