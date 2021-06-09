import random


ran = random.randint(1, 5)
for i in range(3):
    print('Раунд', i+1)
    try:
        inp = int(input('Попробуйте угадать число от 1 до 5: \n'))
        if inp == ran:
            print('Вы угадали. Компьютер загадал', ran)
            break
        else:
            print('Вы не угдали.')
            if inp > ran:
                print('Число компьютера меньше вашего')
            else:
                print('Число компьютера больше вашего')
    except ValueError:
        print('Это было не число...\n Тем не менее, компьютер загадал', ran)
        break
else:
    print('Компьютер загадал', ran)
