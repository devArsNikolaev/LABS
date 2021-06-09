import random


def knb_result(pl, ai):
    if pl == ai:  # ничья
        return 0
    if pl == 1:  # камень
        if ai == 3:
            return 2  # камень - бумага -> проигрыш
        elif ai == 2:
            return 1  # камень - ножницы -> выигрыш
    elif pl == 2:  # ножницы
        if ai == 1:
            return 2  # ножницы - камень -> проигрыш
        elif ai == 3:
            return 1  # ножницы - бумага -> выигрыш
    elif pl == 3:  # бумага
        if ai == 1:
            return 1  # бумага - камень -> выигрыш
        elif ai == 2:
            return 2  # бумага - ножницы -> проигрыш


def code(inp_str):
    if (inp_str == "камень") or (inp_str == '1'):
        return 1
    elif (inp_str == "ножницы") or (inp_str == '2'):
        return 2
    elif (inp_str == "бумага") or (inp_str == '3'):
        return 3
    elif inp_str == "выход":
        return 4
    else:
        return 0


def decode(inp_int):
    if inp_int == 1:
        return "камень"
    elif inp_int == 2:
        return "ножницы"
    elif inp_int == 3:
        return "бумагу"


cash = 100
computer_wins = 0
player_wins = 0
while True:
    bet = 0
    if cash <= 0:
        print('К сожалению, вы проиграли :с')
        print('Вы выиграли', player_wins, 'игр(ы)')
        print('Компьютер выиграл', computer_wins, 'игр(ы)')
        break
    elif cash >= 1000:
        print('Вы выиграли! с:')
        print('Вы выиграли', player_wins, 'игр(ы)')
        print('Компьютер выиграл', computer_wins, 'игр(ы)')
        break
    ai_choose = random.randint(1, 3)
    pl_choose = input("Выберите: камень, ножницы или бумага?\n")
    pl_choose = code(pl_choose)
    res = knb_result(pl_choose, ai_choose)
    if pl_choose != 4:
        while True:
            bet = 0
            try:
                print('выберите ставку. У вас осталось:', cash)
                bet = int(input())
                if bet <= cash:
                    break
                else:
                    print('Неверный ввод')
            except ValueError:
                print('Неверный ввод')

    if res == 1:
        print('Вы выиграли', bet)
        print('компьютер поставил', decode(ai_choose))
        cash += bet
        player_wins += 1
        print('У вас осталось', cash)
    elif res == 2:
        print('Вы проиграли', bet)
        print('компьютер поставил', decode(ai_choose))
        cash -= bet
        computer_wins += 1
        print('У вас осталось', cash)
    elif res == 0:
        print('ничья. У вас осталось', cash)
    elif pl_choose == 4:
        break
    else:
        print('Ошибка ввода')
