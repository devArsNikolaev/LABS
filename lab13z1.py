class MyClass:
    def __init__(self, intvar, stringvar):
        self.intvar = intvar
        self.stringvar = stringvar

    def __add__(self, arg):
        if type(arg) == int:
            self.intvar += arg
        elif type(arg) == str:
            self.stringvar += arg

    def __sub__(self, arg):
        if type(arg) == int:
            self.intvar -= arg

    def __mul__(self, arg):
        if type(arg) == int:
            self.intvar *= arg


A = MyClass(7, 'apple')
A + 5
A * 6
A + 'crocodile'

print(A.intvar)
print(A.stringvar)
