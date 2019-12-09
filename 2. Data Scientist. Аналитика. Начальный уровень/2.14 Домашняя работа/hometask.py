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

def days_for_dist():
    km_per_day = int(input('Km by car D: '))
    distance = int(input('Distance to go P: '))
    days = (distance // km_per_day) + (distance - (distance % km_per_day))
    print(round(days))

days_for_dist()