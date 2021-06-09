import random


class Player:
    def __init__(self, hp, damage):
        self.hp = hp
        self.damage = damage

    def deal_damage(self):
        return random.randint(self.damage[0], self.damage[1])

    def hit(self, incoming_damage):
        if self.hp - incoming_damage > 0:
            print('Дракон бьёт игрока')
            self.hp -= incoming_damage
        else:
            print('игрок мёртв')
            self.hp = 0


class Dragon:
    def __init__(self, hp, level, num, dmg=[3, 1000]):
        self.hp = hp
        self. level = level
        self. num = num
        self.dmg = dmg

    def deal_damage(self):
        return random.randint(self.dmg[0], self.dmg[1])

    def hit(self, incoming_damage):
        if self.hp-incoming_damage > 0:
            print('Игрок бьёт дракона', self.num, 'с уровня', self.level)
            self.hp -= incoming_damage
        else:
            print('Дракон', self.num, 'с уровня', self.level, 'мёртв')
            self.hp = 0


def states(Dr, P):
    print('Игрок -', P.hp, 'X Дракон -', Dr.hp)


def brawl(Dr, P):
    while (Dr.hp > 0) and (P.hp > 0):
        Dr.hit(P.deal_damage())
        P.hit(D.deal_damage())
        states(D, hero)
    if hero.hp > 0:
        return 'success'


n = input('Количество уровней:')
n = int(n)
hero = Player(100, [10, 50])
slain = 0

for i in range(1, n+1):
    for j in range(1, i+1):
        D = Dragon(50, i, j)
        result = brawl(D, hero)
        if result == 'success':
            slain += 1
        else:
            break

print('Вы победили', slain, 'драконов')
