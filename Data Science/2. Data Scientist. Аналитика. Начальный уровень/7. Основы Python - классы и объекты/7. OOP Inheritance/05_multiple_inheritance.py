# -*- coding: utf-8 -*-

# Множественное наследование. Когда базовые классы реализуют каждый некую роль,
# а дочерние - собирают все вместе.


class Employee:
    """ Работник """

    def salary(self):
        """ Зарплата """
        return 15000


class Parent:
    """ Родитель """

    def childrens(self):
        """ Дети """
        return ['Вася', 'Катя']


class Man(Parent, Employee):
    """ Человек - является и Родителем и Работником """
    pass


me = Man()
print(me.childrens())
print(me.salary())


# или про роботов

class Robot:

    def __init__(self, model):
        self.model = model

    def __str__(self):
        return '{} model {}'.format(self.__class__.__name__, self.model)

    def operate(self):
        print('Робот ездит по кругу')


class CanFly:

    def __init__(self):
        self.altitude = 0  # метров
        self.velocity = 0  # км/ч

    def take_off(self):
        self.altitude = 100
        self.velocity = 300

    def fly(self):
        self.altitude = 5000

    def land_on(self):
        self.altitude = 0
        self.velocity = 0

    # def __str__(self):
    #     return '{} высота {} скорость {}'.format(
    #         self.__class__.__name__, self.altitude, self.velocity)


class Drone(Robot, CanFly):

    def operate(self):
        print('Робот ведет разведку с воздуха')


orbiter = Drone(model='Orbiter II')
orbiter.take_off()
orbiter.fly()
orbiter.operate()
orbiter.land_on()

# А что будет если есть переопределение методов, которые реализованы в разных родительских?
# Есть алгоритм MRO (method resolution order) который гарантированно обойдет всех родителей


class GrandParent:

    def method(self):
        print('call from GrandParent')


class ParentOne(GrandParent):

    def method(self):
        super().method()
        print('call from ParentOne')


class ParentTwo(GrandParent):

    def method(self):
        super().method()
        print('call from ParentTwo')


class Child(ParentOne, ParentTwo, ):

    def method(self):
        super().method()
        print('call from Child')


obj = Child()
obj.method()
print(obj.__class__.__mro__)  # так можно посмотреть в каком порядке будут искаться методы


# Как происходит поиск методов при простом множественном наследовании
# (когда предки не связаны между собой узами)

class Robot:

    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = model

    def __str__(self):
        return '{} model {}'.format(self.__class__.__name__, self.model)

    def operate(self):
        print('Class Robot def operate: Робот ездит по кругу')


class CanFly:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.altitude = 0  # метров
        self.velocity = 0  # км/ч

    def take_off(self):
        self.altitude = 100
        self.velocity = 300
        print(f'Полетели! Высота {self.altitude}, Скорость {self.velocity}')

    def fly(self):
        self.altitude = 5000

    def land_on(self):
        self.altitude = 0
        self.velocity = 0
        print('Flight is over')

    def __str__(self):
        return '{} высота {} скорость {}'.format(
            self.__class__.__name__, self.altitude, self.velocity)

    def operate(self):
        super().operate()
        print('Class CanFly def operate: Летим')


class Drone(CanFly, Robot, ):

    def __init__(self, model, gun):
        super(Drone, self).__init__(model=model)
        self.gun = gun

    def operate(self):
        super().operate()
        print('Class Drone def operate: Робот ведет разведку с воздуха')

    def __str__(self):
        return '{} - model {} '.format(self.__class__.__name__, self.model) + '{} высота {} скорость {}'.format(
            self.__class__.__name__, self.altitude, self.velocity)


print('====0====', '\n')
orbiter = Drone(model='Orbiter II', gun='turrel')
print(orbiter)
print('====1====', '\n')
orbiter.take_off()
print('====2====', '\n')
print(orbiter)
print('====3====', '\n')
orbiter.fly()
print('====4====', '\n')
print(orbiter)
print('====5====', '\n')
orbiter.operate()
print('====6====', '\n')
print(orbiter)
print('====7====', '\n')
orbiter.land_on()
