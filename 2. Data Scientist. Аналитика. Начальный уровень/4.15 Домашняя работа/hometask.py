# 4.15 Skillbox hometask

L = [
    [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    ],
    [
        [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
        [31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
    ],
    [
        [41, 42, 43, 44, 45],
        [46, [47, 48], 49, 50],
        [51, 52, 53, 54, 55],
        [56, 57, 58, 59, 60]
    ],
    [61, 62, 63,
     [64, 65, 66, 67, 68, 69, 70, 71],
     72, 73, 74,
     [75,
      [76, 77, 78],
      79],
     80],
    [81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
]

# print(L[3][7][1][1:])


def watch_time():
    seconds = int(input('Input seconds quantity: '))
    hours = seconds // 3600
    minutes = (seconds % (hours * 3600)) // 60
    sec = (seconds % 60)

    if minutes < 10:
        minutes = '0' + str(minutes)

    if sec < 10:
        sec = '0' + str(sec)

    print(hours, ':',  minutes, ':',  sec)

# watch_time()


def mkad_km():
    velocity = int(input('Velocity: '))
    time_movement = int(input('Hours: '))
    km = (velocity * time_movement) % 109
    print(km)

# mkad_km()

def figures_summ():
    figure = input('Input digits: ')
    figure_summ = 0
    for i in range(len(figure)):
        figure_summ = figure_summ + int(figure[i])
    print(figure_summ)

# figures_summ()

def digit_swap():
    digits = input('Input digits: ')
    result = digits[2:] + digits[0:2]
    print(result)

# digit_swap()

# ___________________________________
def days_for_dist(km_per_day):
    # km_per_day = int(input('Km by car D: '))
    # distance = int(input('Distance to go P: ')) '))
    # km_per_day = 121
    distance = 120 - 1
    # days = (distance / km_per_day)
    # rest = (distance % km_per_day) *
    # print('rest: ', rest)
    days = (distance / km_per_day) + 1 * (distance // km_per_day)
    # days = (distance / km_per_day) + 1 * (distance // km_per_day)
    # days = (distance / (km_per_day + 1)) + 1 * (distance // km_per_day)
    #    days = round(days)
    days_raw = days
    days = round(days - 0.5)
    # days_str = days[0]
    return days_raw, days


# days_for_dist()

# D_km_car = list(range(5, 220, 1))
#
# for d in D_km_car:
#     result = days_for_dist(d)
#     print(d, ':', result, '; ')
#_______________________________________________



'''21. Напишите программу, которая считает, сколько рублей и копеек нужно заплатить за N авокадо, если один авокадо стоит R рублей и K копеек.

Формат ввода:
40 20
5
Формат вывода:
201 руб. 00 коп.'''

def avocado_price():
    price = input('Price: ')
    avocado_n = int(input('Quantity: '))
    price = price.split()
    rubles_r = int(price[0])
    kopeek_k = int(price[1])
    kopeek_total = (rubles_r * 100 + kopeek_k) * avocado_n
    rubles_price = kopeek_total // 100
    kopeek_price = kopeek_total - rubles_price * 100
    kopeek_price = str(kopeek_price)

    if len(kopeek_price) == 1:
        kopeek_price = '0' + kopeek_price

    print(rubles_price, 'руб.', kopeek_price, 'коп.')

# avocado_price()

'''22.
Пусть организаторы мероприятия неправильно составили гугл-форму и просили людей указывать ФИО в неправильном порядке. 
Сначала спрашивали имя, потом отчество, затем фамилию. Напишите программу, которая будет переставлять ФИО в нужный порядок.

Формат ввода:
Иван Иванович Иванов

Формат вывода:
Иванов Иван Иванович'''

def name_correction():
    name = input('Name: ')
    name = name.split()
    name[1], name[2] = name[2], name[1]
    name[0], name[1] = name[1], name[0]
    print('{0} {1} {2}'.format(*name))

name_correction()

'''23.
У вас есть список с заказом в ресторане. Напишите программу, которая меняет указанное по названию блюдо на другое. 
При этом новое блюдо в списке будет расположено на месте того, что было заменено.

Формат ввода:
белое вино
красное вино

Формат вывода:
['красное вино', 'салат Цезарь', 'паста Карбонара', 'чизкейк', 'шоколадный сорбет']'''