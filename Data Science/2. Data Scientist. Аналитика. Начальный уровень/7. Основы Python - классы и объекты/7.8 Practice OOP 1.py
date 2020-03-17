import random

from termcolor import cprint


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 20
        self.food = 10
        self.money = 0

    def __str__(self):
        return 'I\'m {}, fulness {}, food {}, money {}'.format(self.name, self.fullness, self.food, self.money)

    def eat(self):
        if self.food >= 10:
            cprint('{} ate'.format(self.name), color='green')
            self.fullness += 10
            self.food -= 20
        else:
            cprint('{} no food'.format(self.name), color='red')
            self.shopping()

    def work(self):
        cprint('{} worked'.format(self.name), color='cyan')
        self.money += 30
        self.fullness -= 10

    def play(self):
        cprint('{} played game all day long'.format(self.name), color='blue')
        self.fullness -= 10

    def shopping(self):
        if self.money >= 50:
            cprint('{} went to shop'.format(self.name), color='magenta')
            self.money -= 50
            self.food += 50
        else:
            cprint('{} money ran out!'.format(self.name), color='red')
            self.work()

    def act(self):
        if self.fullness <= 0:
            cprint('{} died...'.format(self.name), color='red')
            return

        dice = random.randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.money < 50:
            self.work()
        elif self.food < 10:
            self.shopping()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.play()

carabas = Man(name='Carabas')
for day in range(1, 21):
    print()
    cprint('====================== DAY {} ======================'.format(day), color='yellow')
    carabas.act()
    print(carabas)