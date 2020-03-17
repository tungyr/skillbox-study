# 5.16 Skillbox hometask

'''Циклы и условия

Домашняя работа

Эта домашняя работа должна быть решена БЕЗ использования готовых функций (если именно они "решают" задачу) и сторонних
библиотек. Используйте циклы и условия.

1
Напишите программу, которая будет запрашивать на вход числа (через запятую на одной строке) и выводить наибольшее
значение из списка.

Ограничение: нельзя пользоваться готовой функцией для нахождения максимума (например, max()), готовыми функциями и
методами сортировки (например, sort(),sorted()).'''
# import time

# def time_of_function(function):
#     """Decorator function for defining time elapsed. For python 3.8
#     For python 3.7 and less replace perf_counter() by clock()"""
#     def wrapped(*args):
#         start_time = time.process_time()
#         res = function(*args)
#         result = (time.process_time() - start_time)
#         print('time:', result)
#         return res
#     return wrapped
#
#
# @time_of_function
# def func():
#     for i in range(2000):
#         a = i * i
#         print(a)
#
# func()


def max_value() -> int:
    """Function for definition maximum value in entered range of integers"""
    integers = input('Input integers separated by comma (,): ')
    integers = integers.split(',')  # convert inserted input string to list by .split() method
    integers = [int(i) for i in integers]
    i_max = integers[0]  # set first item from integers list as biggest integer
    for i in integers:
        if i > i_max:
            i_max = i
    print(f'Maximum integer is {i_max}')
    return i_max


# max_value()

'''
2
Напишите программу, которая будет запрашивать на вход числа (каждое с новой строки) до тех пор, пока не будет введен 
ноль (0). На выход должно выводиться второе по величине значение.

Ограничение: нельзя пользоваться готовой функцией для нахождения максимума (например, max()), готовыми функциями и 
методами сортировки (например, sort(),sorted()).
'''

# First version of programm:

# def get_integers() -> list:
#     """Function for getting integers from user and pack it in list"""
#     gotten_integers = []
#     while True:
#         try:
#             #  check for correct input from user
#             integer = int(input('Input integer, for exit type 0: '))
#         except ValueError:
#             if input('Last item not integer! Complete input? y/n ') == 'n':
#                 continue
#             else:
#                 break
#         if integer == 0:
#             break
#         gotten_integers.append(integer)
#     print(f'Received integers are: {gotten_integers}')
#     return gotten_integers
#

# def max_value_fr_list(values_list) -> list:
#     """Function for defining maximum value in list, return max value and list without values duplicates"""
#     i_max = values_list[0]
#     unique_items_list = []
#     for i in values_list:
#         if i in unique_items_list:  # check list for repeated values
#             continue
#         else:
#             if i > i_max:
#                 i_max = i
#             unique_items_list.append(i)
#     return [i_max, unique_items_list]
#
#
# initial_list = get_integers()  # get list of integers from user
#
# # get max value in list
# max_int = max_value_fr_list(values_list=initial_list)[0]
#
# # get values list cleaned from duplicates for further work
# unique_values_list = max_value_fr_list(values_list=initial_list)[1]
#
# unique_values_list.remove(max_int)  # remove max value from list
#
# # get second max value in list and print it:
# print(f'Second maximum value in list {initial_list} is {max_value_fr_list(values_list=unique_values_list)[0]}')

# ---------------------------------------------------------------------------------------------------------------------

# Second and final version of program:

def get_integers() -> list:
    """Function for getting integers from user and pack it in list"""
    gotten_integers = []
    while True:
        try:
            #  check for correct input from user
            integer = int(input('Input integer, when finish type 0: '))
        except ValueError:
            if input('Last item not integer! Complete input? y/n ') == 'n':
                continue
            else:
                break
        if integer == 0:
            break
        gotten_integers.append(integer)
    print(f'Received integers are: {gotten_integers}')
    return gotten_integers


def sort_list(values_list) -> list:
    """Function for sorting list, returns list without duplicates of values"""
    counter = 0
    while counter < len(values_list):
        counter = 1
        for i in range(len(values_list) - 1):
            if values_list.count(values_list[i]) > 1:  # check for duplicates in list
                values_list.remove(values_list[i])
                break
            elif values_list[i] > values_list[i + 1]:  # compare two nearby values
                values_list[i], values_list[i + 1] = values_list[i + 1], values_list[i]
                counter -= 1
            counter += 1
    return values_list


# initial_list = get_integers()  # get list of integers from user
# sorted_list = sort_list(values_list=initial_list)  # get sorted list
# print(f'Second maximum value in sorted list {initial_list} is {sorted_list[-2]}')

'''
3
Напишите программу, которая принимает на вход год, а на выход выдает количество дней в этом году.

'''


def year_days():
    """Function calculates quantity days in year"""
    year = int(input('Enter a number of year: '))
    if year % 400 == 0:
        print(f'{year} year is leap year with 366 days in it')
    elif year % 100 == 0:
        print(f'{year} year is regular with 365 days in it')
    elif year % 4 == 0:
        print(f'{year} year is leap year with 366 days in it')
    else:
        print(f'{year} year is regular with 365 days in it')


# year_days()

'''
​
4
Напишите программу, которая на вход получает координаты двух клеток шахматной доски и выводит соощение о том, являются 
ли эти клетки одного цвета.

'''

# dictionary for decoding field letters to integers
chess_letters = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
}


def get_chess_field() -> str:
    """Function get from user chess field number and check correction of input"""
    while True:
        field_number = input('Enter field (example a1):')
        letter, digit = field_number[0], field_number[1]
        # check for correct order of letters and digits in input
        if letter.isalpha() is False or digit.isdigit() is False:
            print('Wrong format! Example: a1.')
            continue
        else:
            return field_number


def chess_field_color(field) -> str:
    """Function defines chess field color by it number"""
    # decoding field letter to integer with chess_letters dict
    letter_value = chess_letters[field[0]]
    if (letter_value + int(field[1])) % 2 == 0:
        field_color = 'black'
    else:
        field_color = 'white'
    return field_color


# field_1 = chess_field_color(get_chess_field())
# field_2 = chess_field_color(get_chess_field())
#
# if field_1 == field_2:
#     print('Fields are equal')
# else:
#     print('Fields are not equal')


'''
​
​
5
Напишите программу, которая на вход получает число, а на выходе сообщает, простое это число или составное.

'''


def type_of_digit():
    """Function defines whether entered integer natural or composite"""
    while True:
        digit = input('Enter an integer: ')
        # check for correct digit in input
        if digit.isdigit() is False:
            print('Wrong format!.')
            continue
        else:
            digit = int(digit)
            break

    dividers = list(range(1, digit + 1))
    counter = 0
    for i in dividers:
        if digit % i == 0:
            counter += 1

    if counter == 2:
        print(f'Inserted integer {digit} is natural number.')
    else:
        print(f'Inserted integer {digit} is composite number.')


# type_of_digit()

'''
​
6
Напишите программу, которая на вход получает целое число больше 2 и выводит по нему его наименьший натуральный делитель,
 отличный от 1.

'''
# def the_least_divider(number):
#     least_divider = 0
#     for i in range(2, int(number)):
#         if number % i == 0:
#             least_divider = i
#             if least_divider > 0:
#                 print(f'The least divider for integer {number} is {least_divider}')
#             break
#     if least_divider == 0:
#         print(f'There is no the least divider for integer {number}, other then 1')


def the_least_divider() -> int:
    """Function for calculating the least divider of integer"""
    # check for correct input from user
    while True:
        number = input('Enter integer bigger then 2: ')
        if number.isdigit() is False:
            print('Should be digit!')
            continue
        number = int(number)
        if number <= 2:
            print('Integer should be bigger then 2!')
            continue
        else:
            least_divider = 0
            for i in range(2, int(number)):
                if number % i == 0:
                    least_divider = i
                    if least_divider > 0:
                        print(f'The least divider for integer {number} is {least_divider}')
                    break
            if least_divider == 0:
                print(f'There is no the least divider for integer {number}, other then 1')
        return least_divider


# the_least_divider()

'''
​
7
Напишите программу, которая поможет составить план тренировок для подготовки к марафону. Она получает на вход число 
километров на планируемом марафоне, сколько пользователь планирует пробежать в первый день тренировок и на сколько 
процентов планирует увеличивать каждый день это расстояние. На выходе программа должна выдавать, сколько дней 
пользователю потребуется для того, чтобы подготовиться пробежать целевое количество километров.

Ограничение: нельзя пользоваться функцией ceil() из модуля math и ее аналогами.

'''
# dictionary which saves user input data
params_dict = {}


def get_params() -> dict:
    """Function get from user initial data input and saves it in params_dict"""

    params_dict['marathon distance'] = input('Enter marathon distance: ')
    params_dict['first day training kilometers'] = input('Enter first day training km: ')
    params_dict['percent of daily training increase'] = input('Enter percent of daily training increase: ')

    # check user input
    check = 0
    while check < 3:
        for item in params_dict.items():
            if item[1].isdigit() is False:
                # print(f'Parameter {item[0]} should be integer! Try again!')
                params_dict[item[0]] = input(f'Parameter {item[0]} should be integer! Try again: ')
                check = 0
            else:
                check += 1
    print()

    return params_dict


def training_plan(marathon_km, first_day_km, increase_percent_km) -> int:
    """Function calculates quantity of training days for marathon"""
    daily_training = first_day_km
    training_days = 1
    days_list = [[training_days, daily_training]]

    while marathon_km > daily_training:
        # augmentation of training kilometers depending on training days
        whole_increase_km = training_days * (first_day_km * (increase_percent_km/100))
        daily_training = first_day_km + whole_increase_km
        training_days += 1
        # save data for further output
        days_list.append([training_days, daily_training])

    print(f'To run out marathon in {marathon_km} km you will need {training_days} day(s) of training: \n')

    print('Plan')
    for day in days_list:
        print('{0:>2} day - {1:>3} km'.format(day[0], day[1]))

    return training_days


# get_params()
#
# training_plan(marathon_km=int(params_dict['marathon distance']),
#               first_day_km=int(params_dict['first day training kilometers']),
#               increase_percent_km=int(params_dict['percent of daily training increase']))

'''​
​
8
Напишите программу, которая на вход получает число n и считает по нему сумму 1²+2²+3²+...+n².

Ограничение: нельзя пользоваться функцией sum() и ее аналогами.

'''


def number_range_power() -> int:
    """Function for calculating sum of series integers, raised to second power"""
    number = ''
    summary = 0
    while number.isdigit() is False:
        number = input('Enter integer: ')
        # check for negative integer input and if so convert it to positive
        number = number.lstrip('-') if number.startswith('-') else number
    else:
        for i in range(1, int(number) + 1):
            summary = summary + i ** 2
    print(summary)
    return summary


# number_range_power()
'''​

​
​
9
Напишите программу, которая на вход получает число n и считает по нему сумму сумму 1! + 2! + 3! + ... + n!

Ограничение: нельзя пользоваться готовой функцией factorial() из модуля math, функцией sum() и их аналогами.

'''


def number_range_factorial() -> int:
    """Function for calculating sum of factorials of series integers"""
    number = ''
    while number.isdigit() is False:
        number = input('Enter positive integer: ')
        # check for negative integer input and if so convert it to positive
        number = number.lstrip('-') if number.startswith('-') else number
    else:
        number = int(number)
        sum = 0
        for i in range(1, number + 1):
            number_factorial = 1
            for j in range(1, i + 1):
                number_factorial = number_factorial * j
            # print(f'My factorial of   {i} is {number_factorial}')
            # print(f'Real factorial of {i} is {math.factorial(i)}')
            sum = sum + number_factorial

    print('Final sum: ', sum)
    return sum


# number_range_factorial()

'''​
​
​
10
Напишите программу, которая получает на вход последовательность чисел (каждое число с новой строки до того момента, 
пока пользователь не введет 0) и считает количество четных элементов в последовательности.
'''

# по ошибке сделал подсчет суммы элементов в последовательности

# def even_integers_summ():
#     """Function calculates sum of even integers series"""
#     gotten_integers = []
#     integer = ''
#     while integer != 0:
#         integer = int(input('Input integer: '))
#         gotten_integers.append(integer)
#     print(gotten_integers)
#     summ = 0
#     for i in gotten_integers:
#         if i % 2 == 0:
#             summ = summ + i
#     print(summ)
#     return summ

# even_integers_summ()


# правильное решение

def even_integers_counter() -> int:
    """Function calculates quantity of even integers series received from useer"""
    counter = 0
    while 1:
        integer = input('Input integer: ')
        # check for integer in input
        if integer.isdigit():
            integer = int(integer)
            # check whether integer value is 0 and evenness of it
            if integer != 0 and integer % 2 == 0:
                counter += 1
                continue
            elif integer != 0:
                continue
            else:
                print(f'You inserted {counter} even elements')
                break
        else:
            print('Should be integer! Try again, please')
            continue

    return counter


# even_integers_counter()

'''

11
Напишите программу, которая формирует список игроков женской команды по футболу. Программа должна записывать возраст и 
пол претендента. Возраст должен запрашиваться после пола и только в том случае, если пол претендента женский. 
Если пол претендента мужской, программа должна сообщать о том, что он не подходит. Возраст претенденток должен быть от 
18 до 35 лет. Если кандидат удовлетворяет требованиям, должно появляться соответствующее сообщение.

'''


def female_football_team_form():
    """Function creates list of female football team players"""

    players = []
    while 1:
        name = input('Player\'s name: ')
        sex = input('Player\'s sex (male / female): ')

        # validate sex input
        if sex == 'female':
            pass
        else:
            try_again_sex = input('Sorry, this team only for girls. Try again? y/n: ')
            if try_again_sex == 'y':
                continue
            else:
                print(f'Team players: ')
                [print(f'{name}, {age} years old') for name, age in players]
                break

        # validate age input
        age = input('Player\'s age: ')
        if age.isdigit() and 18 <= int(age) <= 35:
            print("Player is successfully added to football team!")
            players.append([name, age])
        else:
            try_again_age = input('Sorry, player\'s age is not suitable by restrictions. Try again? y/n: ')
            if try_again_age == 'y':
                continue
            else:
                print(f'Team players: ')
                [print(f'{name}, {age} years old') for name, age in players]
                break

        next_player = input('Do you want to add another player? y/n: ')
        if next_player == 'y':
            continue
        else:
            print(f'Team players: ')
            [print(f'{name}, {age} years old') for name, age in players]
            break


# female_football_team_form()


'''
​
12
Напишите программу, которая на вход получает максимальную ширину ромба и рисует его. Гарантируется, что входное число 
всегда нечетное.

Пример вывода для числа 5:

  *
 ***
*****
 ***
  *
'''


def diamond():
    """Function creates diamond from inserted symbols"""
    symbol = input('Insert any symbol: ')
    while 1:
        width = input('Enter odd integer: ')

        # validate integer in input
        if width.isdigit() is False:
            print('Should be integer! Try again')
            continue
        else:
            # validate oddness of integer and add 1 to integer if integer is even
            width = int(width)
            if width % 2 == 0:
                width += 1

            # define number of spaces for indent before symbols
            spaces_number = int(width // 2)
            symbols_number = 1

            for i in range(1, width + 1):
                if i < (width + 1) // 2:
                    # upper part of diamond
                    print(' ' * spaces_number, symbol * symbols_number)
                    spaces_number = spaces_number - 1
                    symbols_number = symbols_number + 2
                else:
                    # lower part of diamond
                    print(' ' * spaces_number, symbol * symbols_number)
                    spaces_number = spaces_number + 1
                    symbols_number = symbols_number - 2
        break


# diamond()

'''
​
​
13
Напишите программу, которая запрашивает у пользователя сторону квадрата и символ, а затем рисует этот символ по 
диагоналям квадрата. Гарантируется, что входное число всегда нечетное.

Пример вывода для числа 5:


#   #
 # #
  #  
 # #
#   #
'''


def cross_shape():
    """Function creates cross from inserted symbols"""
    symbol = input('Enter symbol: ')
    while 1:
        width = input('Enter odd integer: ')

        # validate integer in input
        if width.isdigit() is False:
            print('Should be integer! Try again')
            continue
        else:
            width = int(width)
            # validate oddness of integer and add 1 to integer if integer is even
            if width % 2 == 0:
                width += 1

            tab = 0  # variable of indents outside of cross
            spaces_number = width - 2  # variable of spaces between 'legs' of cross

            for i in range(1, width + 1):
                # upper part of cross
                if i < (width + 1) // 2:
                    print(' ' * tab + symbol + ' ' * spaces_number + symbol)
                    spaces_number = spaces_number - 2
                    tab += 1
                # middle part of cross
                elif i == (width + 1) // 2:
                    print(' ' * tab + symbol)
                    tab -= 1
                # lower part of cross
                else:
                    spaces_number = spaces_number + 2
                    print(' ' * tab + symbol + ' ' * spaces_number + symbol)
                    tab -= 1
            break


# cross_shape()


'''
​
​
14
В корзине лежат шары. Если разложить их в кучи по 2, останется один. Если разложить в кучи по 3, останется один. Если 
разложить в кучи по 4, останется один. Если разложить в кучи по 5, останется один. Если разложить в кучи по 6, 
останется один. Если разложить в кучи по 7, не будет остатка. Нужно найти минимальное количество шаров, 
удовлетворяющее условию.

'''
# numbers_list = range(1000)
#
# is_divide_2 = lambda x: x % 2 == 1
# is_divide_3 = lambda x: x % 3 == 1
# is_divide_4 = lambda x: x % 4 == 1
# is_divide_5 = lambda x: x % 5 == 1
# is_divide_6 = lambda x: x % 6 == 1
# is_divide_7 = lambda x: x % 7 == 0
#
# numbers_2 = list(filter(is_divide_2, numbers_list))
# print(numbers_2)
#
# numbers_3 = list(filter(is_divide_3, numbers_2))
# print(numbers_3)
#
# numbers_4 = list(filter(is_divide_4, numbers_3))
# print(numbers_4)
#
# numbers_5 = list(filter(is_divide_5, numbers_4))
# print(numbers_5)
#
# numbers_6 = list(filter(is_divide_6, numbers_5))
# print(numbers_6)
#
# numbers_7 = list(filter(is_divide_7, numbers_6))
# print(numbers_7)


# x = 1
#
# while 1:
#     # validate 5 first conditions for dividing integer by 2, 3, 4, 5, 6 without reminder
#     first_check = 0
#     for i in range(2, 7):
#         if x % i != 1:
#             break
#         else:
#             # sum of successful checks
#             first_check = first_check + x % i
#
#     # validate last condition for dividing integer by 7 without reminder
#     if first_check == 5 and x % 7 == 0:
#         print('Minimum balls quantity: ', x)
#         break
#     else:
#         x += 1
#         continue


'''
​
15
Рабочие клеили обои на стены. Первую стену поклеили за M минут, а каждую следующую на 5 минут больше, чем предыдущую. 
Напишите программу, которая запрашивает сколько стен было в квартире под поклейку, а также время работы с первой стеной. 
Программа должна выводить, сколько часов рабочие потратили на поклейку обоев во всей квартире. 
Ответом должно быть целое число.


Ограничение: нельзя пользоваться готовыми функциями bool(), floor() и их аналогами.

# '''


def time_for_walls() -> int:
    """Function calculates required time for glueing wallpapers on the number of walls"""
    walls = int(input('Walls: '))
    minutes_for_wall = int(input('Minutes per wall: '))
    whole_time = 0

    # define whole time in minutes spent for all walls
    for i in range(1, walls + 1):
        whole_time = whole_time + minutes_for_wall * i

    # define whole time in hours spent for all walls
    hours_for_walls = whole_time // 60
    reminder_minutes = whole_time - (hours_for_walls * 60)

    # depends on reminder of minutes add or don't add another hour
    if reminder_minutes >= 30:
        hours_for_walls += 1
    print(f'Hours for all walls: {hours_for_walls}')
    return hours_for_walls


# time_for_walls()


'''
​
​
16
Напишите программу, которая убирает из списка повторяющиеся элементы. Программа должна запрашивать на вход слова, 
каждое с новой строки, пока пользователь не введет пустую строку. Затем должна выводить список без повторяющихся 
элементов.

Ограничение: нельзя пользоваться готовой функцией set() и ее аналогами.

'''


def get_words() -> list:
    """Function for getting words from user and pack it in list"""
    gotten_words = []
    while 1:
        word = input('Input word: ')
        # check for empty string
        if word == '':
            break
        gotten_words.append(word)
    print(gotten_words)
    return gotten_words


def remove_duplicate(checking_list) -> list:
    """Function seek for duplicate elements in list and returns unique elements list"""
    unique_elements_list = []
    for i in checking_list:
        if i in unique_elements_list:
            pass
        else:
            unique_elements_list.append(i)
    print(unique_elements_list)
    return unique_elements_list


# remove_duplicate(get_words())

'''
​
​
17
Напишите программу, которая выводит число пар одинаковых элементов в списке. Программа должна запрашивать на вход слова, 
каждое с новой строки, пока пользователь не введет пустую строку.

'''


def get_words() -> list:
    """Function for getting words from user and pack it in list"""
    gotten_words = []
    while 1:
        word = input('Input word: ')
        # check for empty string
        if word == '':
            break
        gotten_words.append(word)
    return gotten_words


def pairs_quantity(checking_list) -> dict:
    """Function for calculation of pair elements in list"""
    pair_element_dict = {}
    for i in checking_list:
        # define how many pairs might be done from every element quantity if it has duplicates
        if checking_list.count(i) > 1:
            pair_element_dict[i] = checking_list.count(i) // 2

    counter = 0
    for key, value in pair_element_dict.items():
        print(f'Element {key} has {value} pair(s)')
        counter += 1
    print(f'{counter} elements have pairs in list')
    return pair_element_dict


# pairs_quantity(get_words())

'''
​
​
18
Будем считать, что кубик может иметь неограниченное количество граней (натуральное число). Напишите программу, которая 
запрашивает, сколько граней имеется у двух разных кубиков. Затем выводит все возможные комбинации результатов бросков 
двух таких кубиков.
'''


def dice_combinations() -> int:
    """Function defines all possible combinations of two dices"""
    while 1:
        try:
            dice1_sides, dice2_sides = map(int, input('Enter sides quantity at first and second dice separated by '
                                                      'space: ').split())
        # validate user input
        except ValueError:
            if input('Unsupported data! Try again? y/n ') == 'y':
                continue
            else:
                break

        print('Possible combinations: ', '\n')
        combinations = 0
        for i in range(1, dice1_sides + 1):
            for j in range(1, dice2_sides + 1):
                combinations += 1
                print(f'{combinations}. {i} x {j}')
        return combinations


dice_combinations()