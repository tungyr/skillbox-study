# 5.16 Skillbox hometask

'''Циклы и условия

Домашняя работа

Эта домашняя работа должна быть решена БЕЗ использования готовых функций (если именно они "решают" задачу) и сторонних библиотек. Используйте циклы и условия.

1
Напишите программу, которая будет запрашивать на вход числа (через запятую на одной строке) и выводить наибольшее значение из списка.

Ограничение: нельзя пользоваться готовой функцией для нахождения максимума (например, max()), готовыми функциями и методами сортировки (например, sort(),sorted()).'''
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


def max_value():
    """Function for defining maximum value in entered range of integers"""
    integers = input('Input digits: ')
    integers = integers.split(',')
    integers = [int(i) for i in integers]
    i_max = integers[0]
    for i in integers:
        if i > i_max:
            i_max = i
    print(f'Maximum integer is {i_max}')


# max_value()





'''
2
Напишите программу, которая будет запрашивать на вход числа (каждое с новой строки) до тех пор, пока не будет введен ноль (0). На выход должно выводиться второе по величине значение.

Ограничение: нельзя пользоваться готовой функцией для нахождения максимума (например, max()), готовыми функциями и методами сортировки (например, sort(),sorted()).
'''


def get_integers():
    """Function for getting integers from user and pack it in list"""
    gotten_integers = []
    while True:
        integer = int(input('Input integer: '))
        if integer == 0:
            break
        gotten_integers.append(integer)
    return gotten_integers


def max_value_fr_list(values_list):
    """Function for defining maximum value in list"""
    i_max = values_list[0]
    for i in values_list:
        if i > i_max:
            i_max = i
    return i_max


# integers_list = get_integers()
# initial_list = str(integers_list)
# print(f'Received integers are: {integers_list}')
# integers_list.remove(max_value_fr_list(values_list=integers_list))
# print(f'Second maximum value in list {initial_list} is {max_value_fr_list(values_list=integers_list)}')



'''
3
Напишите программу, которая принимает на вход год, а на выход выдает количество дней в этом году.

'''


def year_days(year):
    """Function calculates quantity days in year"""
    if year % 400 == 0:
        print(f'{year} year is leap year with 366 days in it')
    elif year % 100 == 0:
        print(f'{year} year is reqular with 365 days in it')
    elif year % 4 == 0:
        print(f'{year} year is leap year with 366 days in it')
    else:
        print(f'{year} year is reqular with 365 days in it')


# year_days(year=2000)
# year_days(year=2100)
# year_days(year=1600)


'''
​
4
Напишите программу, которая на вход получает координаты двух клеток шахматной доски и выводит соощение о том, являются ли эти клетки одного цвета.

'''
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


def chess_field_color(field):
    """Function defines chess field color by it number"""
    letter_value = chess_letters[field[0]]
    if (letter_value + int(field[1])) % 2 == 0:
        field_color = 'black'
    else:
        field_color = 'white'
    return field_color


def get_chess_field():
    """Function get from user chess field number and check correction of input"""
    while True:
        field_number = input('Enter field:')
        letter, digit = field_number[0], field_number[1]
        if letter.isalpha() is False or digit.isdigit() is False:
            print('Wrong format! Example: a1.')
            continue
        else:
            return field_number


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


def type_of_digit(digit):
    """Function defines whether entered integer natural or composite"""
    dividers = list(range(1, digit + 1))
    counter = 0
    for i in dividers:
        if digit % i == 0:
            counter += 1

    if counter == 2:
        print(f'Inserted integer {digit} is natural number.')
    else:
        print(f'Inserted integer {digit} is composite number.')


# type_of_digit(2)
'''
​
​
6
Напишите программу, которая на вход получает целое число больше 2 и выводит по нему его наименьший натуральный делитель, отличный от 1.

### YOUR CODE HERE ###
​
​
7
Напишите программу, которая поможет составить план тренировок для подготовки к марафону. Она получает на вход число километров на планируемом марафоне, сколько пользователь планирует пробежать в первый день тренировок и на сколько процентов планирует увеличивать каждый день это расстояние. На выходе программа должна выдавать, сколько дней пользователю потребуется для того, чтобы подготовиться пробежать целевое количество километров.

Ограничение: нельзя пользоваться функцией ceil() из модуля math и ее аналогами.

### YOUR CODE HERE ###
​
​
8
Напишите программу, которая на вход получает число n и считает по нему сумму 1²+2²+3²+...+n².

Ограничение: нельзя пользоваться функцией sum() и ее аналогами.

### YOUR CODE HERE ###
​
​
9
Напишите программу, которая на вход получает число n и считает по нему сумму сумму 1! + 2! + 3! + ... + n!

Ограничение: нельзя пользоваться готовой функцией factorial() из модуля math, функцией sum() и их аналогами.

### YOUR CODE HERE ###
​
​
10
Напишите программу, которая получает на вход последовательность чисел (каждое число с новой строки до того момента, пока пользователь не введет 0) и считает количество четных элементов в последовательности.

### YOUR CODE HERE ###
​
​
11
Напишите программу, которая формирует список игроков женской команды по футболу. Программа должна записывать возраст и пол претендента. Возраст должен запрашиваться после пола и только в том случае, если пол претендента женский. Если пол претендента мужской, программа должна сообщать о том, что он не подходит. Возраст претенденток должен быть от 18 до 35 лет. Если кандидат удовлетворяет требованиям, должно появляться соответствующее сообщение.

### YOUR CODE HERE ###
​
​
12
Напишите программу, которая на вход получает максимальную ширину ромба и рисует его. Гарантируется, что входное число всегда нечетное.

Пример вывода для числа 5:

  *
 ***
*****
 ***
  *
### YOUR CODE HERE ###
​
​
13
Напишите программу, которая запрашивает у пользователя сторону квадрата и символ, а затем рисует этот символ по диагоналям квадрата. Гарантируется, что входное число всегда нечетное.

Пример вывода для числа 5:


#   #
 # #
  #  
 # #
#   #
### YOUR CODE HERE ###
​
​
14
В корзине лежат шары. Если разложить их в кучи по 2, останется один. Если разложить в кучи по 3, останется один. Если разложить в кучи по 4, останется один. Если разложить в кучи по 5, останется один. Если разложить в кучи по 6, останется один. Если разложить в кучи по 7, не будет остатка. Нужно найти минимальное количество шаров, удовлетворяющее условию.

### YOUR CODE HERE ###
​
​
15
Рабочие клеили обои на стены. Первую стену поклеили за M минут, а каждую следующую на 5 минут больше, чем предыдущую. Напишите программу, которая запрашивает сколько стен было в квартире под поклейку, а также время работы с первой стеной. Программа должна выводить, сколько часов рабочие потратили на поклейку обоев во всей квартире. Ответом должно быть целое число.

Ограничение: нельзя пользоваться готовыми функциями bool(), floor() и их аналогами.

### YOUR CODE HERE ###
​
​
16
Напишите программу, которая убирает из списка повторяющиеся элементы. Программа должна запрашивать на вход слова, каждое с новой строки, пока пользователь не введет пустую строку. Затем должна выводить список без повторяющихся элементов.

Ограничение: нельзя пользоваться готовой функцией set() и ее аналогами.

### YOUR CODE HERE ###
​
​
17
Напишите программу, которая выводит число пар одинаковых элементов в списке. Программа должна запрашивать на вход слова, каждое с новой строки, пока пользователь не введет пустую строку.

### YOUR CODE HERE ###
​
​
18
Будем считать, что кубик может иметь неограниченное количество граней (натуральное число). Напишите программу, которая запрашивает, сколько граней имеется у двух разных кубиков. Затем выводит все возможные комбинации результатов бросков двух таких кубиков.

### YOUR CODE HERE ###

'''