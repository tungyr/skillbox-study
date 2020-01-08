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


# def max_value():
#     """Function for defining maximum value in entered range of integers"""
#     integers = input('Input digits: ')
#     integers = integers.split(',')
#     integers = [int(i) for i in integers]
#     i_max = integers[0]
#     for i in integers:
#         if i > i_max:
#             i_max = i
#     print(f'Maximum integer is {i_max}')


# max_value()





'''
2
Напишите программу, которая будет запрашивать на вход числа (каждое с новой строки) до тех пор, пока не будет введен 
ноль (0). На выход должно выводиться второе по величине значение.

Ограничение: нельзя пользоваться готовой функцией для нахождения максимума (например, max()), готовыми функциями и 
методами сортировки (например, sort(),sorted()).
'''


# def get_integers():
#     """Function for getting integers from user and pack it in list"""
#     gotten_integers = []
#     while True:
#         integer = int(input('Input integer: '))
#         if integer == 0:
#             break
#         gotten_integers.append(integer)
#     return gotten_integers
#
#
# def max_value_fr_list(values_list):
#     """Function for defining maximum value in list"""
#     i_max = values_list[0]
#     for i in values_list:
#         if i > i_max:
#             i_max = i
#     return i_max


# integers_list = get_integers()
# initial_list = str(integers_list)
# print(f'Received integers are: {integers_list}')
# integers_list.remove(max_value_fr_list(values_list=integers_list))
# print(f'Second maximum value in list {initial_list} is {max_value_fr_list(values_list=integers_list)}')



'''
3
Напишите программу, которая принимает на вход год, а на выход выдает количество дней в этом году.

'''


# def year_days(year):
#     """Function calculates quantity days in year"""
#     if year % 400 == 0:
#         print(f'{year} year is leap year with 366 days in it')
#     elif year % 100 == 0:
#         print(f'{year} year is reqular with 365 days in it')
#     elif year % 4 == 0:
#         print(f'{year} year is leap year with 366 days in it')
#     else:
#         print(f'{year} year is reqular with 365 days in it')
#

# year_days(year=2000)
# year_days(year=2100)
# year_days(year=1600)


'''
​
4
Напишите программу, которая на вход получает координаты двух клеток шахматной доски и выводит соощение о том, являются 
ли эти клетки одного цвета.

'''
# chess_letters = {
#     'a': 1,
#     'b': 2,
#     'c': 3,
#     'd': 4,
#     'e': 5,
#     'f': 6,
#     'g': 7,
#     'h': 8,
# }
#
#
# def chess_field_color(field):
#     """Function defines chess field color by it number"""
#     letter_value = chess_letters[field[0]]
#     if (letter_value + int(field[1])) % 2 == 0:
#         field_color = 'black'
#     else:
#         field_color = 'white'
#     return field_color
#
#
# def get_chess_field():
#     """Function get from user chess field number and check correction of input"""
#     while True:
#         field_number = input('Enter field:')
#         letter, digit = field_number[0], field_number[1]
#         if letter.isalpha() is False or digit.isdigit() is False:
#             print('Wrong format! Example: a1.')
#             continue
#         else:
#             return field_number


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


# def type_of_digit(digit):
#     """Function defines whether entered integer natural or composite"""
#     dividers = list(range(1, digit + 1))
#     counter = 0
#     for i in dividers:
#         if digit % i == 0:
#             counter += 1
#
#     if counter == 2:
#         print(f'Inserted integer {digit} is natural number.')
#     else:
#         print(f'Inserted integer {digit} is composite number.')


# type_of_digit(2)
'''
​
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


# def the_least_divider():
#     """Function for calculating the least divider of integer"""
#     while True:
#         number = input('Enter integer bigger then 2: ')
#         if number.isdigit() is False:
#             print('Should be digit!')
#             continue
#         number = int(number)
#         if number <= 2:
#             print('Integer should be bigger then 2!')
#             continue
#         else:
#             least_divider = 0
#             for i in range(2, int(number)):
#                 if number % i == 0:
#                     least_divider = i
#                     if least_divider > 0:
#                         print(f'The least divider for integer {number} is {least_divider}')
#                     break
#             if least_divider == 0:
#                 print(f'There is no the least divider for integer {number}, other then 1')
#         return least_divider


# for i in range(1, 36):
#     the_least_divider(i)
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
# params_dict = {}
#
#
# def get_params():
#     # params_dict = {
#     #     1: 'marathon distance',
#     #     2: 'first day training kilometers',
#     #     3: 'percent of daily training increase'
#     # }
#
#     # params_dict['marathon distance'] = input('Enter marathon distance: ')
#     params_dict['marathon distance'] = '10'
#     # params_dict['first day training kilometers'] = input('Enter first day training km: ')
#     params_dict['first day training kilometers'] = '1'
#     # params_dict['percent of daily training increase'] = input('Enter percent of daily training increase: ')
#     params_dict['percent of daily training increase'] = '100'
#     print(params_dict)
#
#     check = 0
#     while check < 3:
#         for item in params_dict.items():
#             if item[1].isdigit() is False:
#                 # print(f'Parameter {item[0]} should be integer! Try again!')
#                 params_dict[item[0]] = input(f'Parameter {item[0]} should be integer! Try again: ')
#                 check = 0
#             else:
#                 check += 1
#
#     print(params_dict, params_dict['marathon distance'])
#     return params_dict
#
#
# def training_plan(marathon_km, first_day_km, increase_percent_km):
#     # marathon_km = 5
#     daily_training = first_day_km
#     # increase_percent_km = 50
#     training_days = 1
#     while marathon_km > daily_training:
#         # augmentation of training kilometers depending on training days
#         whole_increase_km = training_days * (first_day_km * (increase_percent_km/100))
#         daily_training = first_day_km + whole_increase_km
#         training_days += 1
#     print(training_days)


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

# def number_range_power():
#     """Function for calculating sum of series integers, raised to second power"""
#     number = ''
#     summ = 0
#     while number.isdigit() is False:
#         number = input('Enter integer: ')
#         # check for negative integer input and if so convert it to positive
#         number = number.lstrip('-') if number.startswith('-') else number
#     else:
#         for i in range(1, int(number) + 1):
#             summ = summ + i ** 2
#             print(i, i ** 2, summ, sep=' ,')
#     print(summ)
#     return summ


# number_range_power()
'''​

​
​
9
Напишите программу, которая на вход получает число n и считает по нему сумму сумму 1! + 2! + 3! + ... + n!

Ограничение: нельзя пользоваться готовой функцией factorial() из модуля math, функцией sum() и их аналогами.

'''
# import math


# def number_range_factorial():
#     """Function for calculating sum of factorials of series integers"""
#     number = ''
#     while number.isdigit() is False:
#         number = input('Enter positive integer: ')
#         # check for negative integer input and if so convert it to positive
#         number = number.lstrip('-') if number.startswith('-') else number
#     else:
#         number = int(number)
#         summ = 0
#         for i in range(1, number + 1):
#             number_factorial = 1
#             for j in range(1, i + 1):
#                 number_factorial = number_factorial * j
#             # print(f'My factorial of   {i} is {number_factorial}')
#             # print(f'Real factorial of {i} is {math.factorial(i)}')
#             summ = summ + number_factorial
#             # print('Sum: ', summ)
#             # print()
#
#     print('Final sum: ', summ)
#     return summ


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

# def even_integers_counter():
#     """Function calculates sum of even integers series"""
#     counter = 0
#     while 1:
#         integer = input('Input integer: ')
#         if integer.isdigit():
#             integer = int(integer)
#             if integer != 0 and integer % 2 == 0:
#                 counter += 1
#                 continue
#             elif integer != 0:
#                 continue
#             else:
#                 print(f'Counter: {counter}')
#                 break
#         else:
#             print('Should be integer! Try again, please')
#             continue
#     print(f'Counter: {counter}')
#     return counter


# even_integers_counter()

'''

11
Напишите программу, которая формирует список игроков женской команды по футболу. Программа должна записывать возраст и 
пол претендента. Возраст должен запрашиваться после пола и только в том случае, если пол претендента женский. 
Если пол претендента мужской, программа должна сообщать о том, что он не подходит. Возраст претенденток должен быть от 
18 до 35 лет. Если кандидат удовлетворяет требованиям, должно появляться соответствующее сообщение.

'''


# def female_football_team_form():
#     """Function creates list of female football team players"""
#
#     players = []
#     while 1:
#         name = input('Player\'s name: ')
#         sex = input('Player\'s sex (male / female): ')
#         if sex == 'female':
#             pass
#         else:
#             try_again_sex = input('Sorry, this team only for girls. Try again? y/n: ')
#             if try_again_sex == 'y':
#                 continue
#             else:
#                 print(f'Team players: {players}')
#                 break
#
#         age = input('Player\'s age: ')
#         if age.isdigit() and 18 <= int(age) <= 35:
#             print("Player is successfully added to football team!")
#             player = [name, age]
#             players.append(player)
#         else:
#             try_again_age = input('Sorry, player\'s age is not suitable for restrictions. Try again? y/n: ')
#             if try_again_age == 'y':
#                 continue
#             else:
#                 print(f'Team players: {players}')
#                 break
#
#         again = input('Do you want to add another player? y/n: ')
#         if again == 'y':
#             continue
#         else:
#             print(f'Team players: ')
#             [print(i) for i in players]
#             break


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


# def diamond():
#     """Function creates diamond from inserted symbols"""
#     symbol = input('Insert any symbol: ')
#     while 1:
#         width = input('Enter odd integer: ')
#         if width.isdigit() is False:
#             print('Should be integer! Try again')
#             continue
#         else:
#             width = int(width)
#             if width % 2 == 0:
#                 width += 1
#             spaces_number = int(width // 2)
#             symbols_number = 1
#
#             for i in range(1, width + 1):
#                 if i < (width + 1) // 2:
#                     print(' ' * spaces_number, symbol * symbols_number)
#                     spaces_number = spaces_number - 1
#                     symbols_number = symbols_number + 2
#                 else:
#                     print(' ' * spaces_number, symbol * symbols_number)
#                     spaces_number = spaces_number + 1
#                     symbols_number = symbols_number - 2
#         break


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


# def x_shape():
#     """Function creates cross from inserted symbols"""
#     symbol = input('Enter symbol: ')
#     while 1:
#         width = input('Enter odd integer: ')
#         if width.isdigit() is False:
#             print('Should be integer! Try again')
#             continue
#         else:
#             width = int(width)
#             if width % 2 == 0:
#                 width += 1
#             tab = 0
#             spaces_number = width - 2
#
#             for i in range(1, width + 1):
#                 if i < (width + 1) // 2:
#                     print(' ' * tab + symbol + ' ' * spaces_number + symbol)
#                     spaces_number = spaces_number - 2
#                     tab += 1
#                 elif i == (width + 1) // 2:
#                     tab -= 1
#                     print(' ' * tab, symbol)
#                 else:
#                     spaces_number = spaces_number + 2
#                     print(' ' * tab + symbol + ' ' * spaces_number + symbol)
#                     tab -= 1
#             break
#

# x_shape()


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

x = 61
summary = 0
checksum = 0

while checksum != 6:
    for i in range(2, 7):
        summary = summary + x % i
        checksum += 1
        if summary != checksum:
            x += 1
            checksum = 0
            break
#
#
print(x)

    # print(x)
    # break
    # continue
    #     else:
    #         if x % 7 != 0:
    #             x += 1
    #             checksum = 0
    #             break
    #         else:
    #             print(x)
    # break
















'''
​
15
Рабочие клеили обои на стены. Первую стену поклеили за M минут, а каждую следующую на 5 минут больше, чем предыдущую. 
Напишите программу, которая запрашивает сколько стен было в квартире под поклейку, а также время работы с первой стеной. 
Программа должна выводить, сколько часов рабочие потратили на поклейку обоев во всей квартире. 
Ответом должно быть целое число.

Ограничение: нельзя пользоваться готовыми функциями bool(), floor() и их аналогами.

### YOUR CODE HERE ###
​
​
16
Напишите программу, которая убирает из списка повторяющиеся элементы. Программа должна запрашивать на вход слова, 
каждое с новой строки, пока пользователь не введет пустую строку. Затем должна выводить список без повторяющихся 
элементов.

Ограничение: нельзя пользоваться готовой функцией set() и ее аналогами.

### YOUR CODE HERE ###
​
​
17
Напишите программу, которая выводит число пар одинаковых элементов в списке. Программа должна запрашивать на вход слова, 
каждое с новой строки, пока пользователь не введет пустую строку.

### YOUR CODE HERE ###
​
​
18
Будем считать, что кубик может иметь неограниченное количество граней (натуральное число). Напишите программу, которая 
запрашивает, сколько граней имеется у двух разных кубиков. Затем выводит все возможные комбинации результатов бросков 
двух таких кубиков.

### YOUR CODE HERE ###

'''