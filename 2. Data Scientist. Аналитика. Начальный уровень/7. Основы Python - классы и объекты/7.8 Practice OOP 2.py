import random

from termcolor import cprint


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 20
        self.house = None

    def __str__(self):
        return 'I\'m {}, fulness {}'.format(self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            cprint('{} ate'.format(self.name), color='green')
            self.fullness += 10
            self.house.food -= 20
        else:
            cprint('{} no food'.format(self.name), color='red')
            self.shopping()

    def work(self):
        cprint('{} worked'.format(self.name), color='cyan')
        self.house.money += 30
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} watched MTV all day long'.format(self.name), color='blue')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} went to shop'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} money ran out!'.format(self.name), color='red')
            self.work()

    def go_into_the_house(self, house):
        self.house = house
        self.money = 50
        self.fullness -= 10
        cprint('{} moved in home'.format(self.name), color='cyan')

    def act(self):
        if self.fullness <= 0:
            cprint('{} died...'.format(self.name), color='red')
            return
        dice = random.randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.money < 50:
            self.work()
        elif self.house.food < 10:
            self.shopping()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()

class House:

    def __init__(self):
        self.food = 50
        self.money = 50

    def __str__(self):
        return 'There are in the house: food {}, money {}'.format(self.food, self.money)

citizens = [
    Man(name='Beavis'),
    Man(name='Butthead'),
    Man(name='Kenny')
]

my_sweat_home = House()
for citizen in citizens:
    citizen.go_into_the_house(house=my_sweat_home)

for day in range(1, 21):
    print()
    cprint('====================== DAY {} ======================'.format(day), color='yellow')
    for citizen in citizens:
        citizen.act()
    print('-------------------- RESULT --------------------')
    for citizen in citizens:
        print(citizen)
    print(my_sweat_home)


