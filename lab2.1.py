import random
ran = random.randint(1, 5)
try:
    inp = int(input('Попробуйте угадать число \n'))
    if inp == ran:
        print('Вы угадали. Компьютер загадал', ran)
    else:
        print('Вы не угдали. Компьютер загадал', ran)
        if inp > ran:
            print('Число компьютера меньше вашего')
        else:
            print('Число компьютера больше вашего')
except ValueError:
    print('Это было не число...\n Тем не менее, компьютер загадал', ran)
