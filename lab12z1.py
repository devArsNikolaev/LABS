import random


class MyClass:

    def __init__(self, x):
        self.x = x

    def print_x(self):
        print('число х равно', self.x)


M = MyClass(random.randint(1, 10))

M.print_x()
