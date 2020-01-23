# ----------------------------------------------------------------------------------------------------------

# Skillbox, 6.8 - 6.9. built-in functions
# https://go.skillbox.ru/course/data-scientist-1/bc6862da-fbd2-4547-afd1-79950f6a5dd8
# https://docs.python.org/3.3/library/functions.html


# # list/set composes only from keys of dict during converting dict -> list/set:
# my_dict = {1: 2, 3: 4}
# print('my_dict -> list: ', list(my_dict))
# print('my_dict -> set: ', set(my_dict))
#
# # creation dict from list list -> dict:
# dict_fr_list = dict([('a', 1), ('b', 2), ('c', 3)])  # list must consist of tuples with pair elements key - value
# print('list -> dict: ', dict_fr_list)

# -----------------------------------------------------

# # max(), min() work only with same type elements in list:
# figure_list = [5, 3, 1, 4, 2]
# # figure_list = [1, 2, 3, '4', 5]
# letter_list = ['d', 'c', 'b', 'a']
# # letter_list = ['a', 'b', 4, 'd']
# print(f'max in {figure_list} is {max(figure_list)}')
# print(f'max in {letter_list} is {max(letter_list)}')
# print(f'min in {figure_list} is {min(figure_list)}')
# print(f'min in {letter_list} is {min(letter_list)}')
#
#
# # https://docs.python.org/3/howto/sorting.html
# # sorted for any iterables, sort only for lists
# print('before sorted func: ', figure_list)
# print('sorted figure_list: ', sorted(figure_list))
# print('after sorted func: ', figure_list)
# print('sort figure_list: ', figure_list.sort())
# print('after sort method: ', figure_list)


# -----------------------------------------------------

# # zip function:
# # https://docs.python.org/3.3/library/functions.html#zip
#
# days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
# # days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat']
# profit = [100, 200, 50, 120, 300, 180, 0]
# # profit = [100, 200, 50, 120, 300, 180]
# revenue_for_list = zip(days, profit)
# revenue_for_dict = zip(days, profit)
#
# # result of zip function should be converted to list/dict to display!
# print('revenue list: ', list(revenue_for_list))
# print('revenue dict: ', dict(revenue_for_dict))

# -----------------------------------------------------

# # additional about zip from docs.python.org:
#
# # to unzip a list:
#
# days1 = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
# profit1 = [100, 200, 50, 120, 300, 180, 0]
#
# days_unzip, profit_unzip = zip(*zip(days1, profit1))
# print('days_unzip: ', days_unzip, type(days_unzip))
# print('profit_unzip: ', profit_unzip, type(profit_unzip))
# print(f'lists days, profit = days_unzip, profit_unzip? ', days1 == list(days_unzip) and profit1 == list(profit_unzip))
#
#
# import itertools
#
# days2 = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
# profit2 = [100, 200, 50, 120]
#
# print('itertolls.zip_longest: ', list(itertools.zip_longest(days2, profit2, fillvalue='-')))

# -----------------------------------------------------

# # functions all, any
# test_list = [1, 2, "hello", 4.9, True, [8, 'a']]
#
# print('all True: ', all(test_list))
# print('all False: ', all([1, 2, "hello", 4.9, True, [8, 'a'], 0]))
#
# print('any True: ', any([1, 2, "hello", 4.9, True, [8, 'a']]))
# print('any False: ', any([0, False, False, 0, 0]))
#
# results_list = []
# for i in test_list:
#     if isinstance(i, str):
#         results_list.append(1)
#     else:
#         results_list.append(0)
# print('results_list: ', results_list)
#
# print('all for results_list: ', all(results_list))
# print('any for results_list: ', any(results_list))

# -----------------------------------------------------

# # dir func
#
# my_list = [1, 2, "hello", 4.9, True, [8, 'a']]
#
# # attributes of list my_list represented in column
# [print(i) for i in dir(my_list)]
# [print(i) for i in dir([])]
# [print(i) for i in dir({})]
#
# # help func
#
# help([])
# help(print)

# -----------------------------------------------------

# # id func
#
# a = [1, 2, 3]
# b = [1, 2, 3]
#
# print(f'comparison based on values: ', a == b)
# print(f'comparison based on id-s: ', id(a) == id(b))
# # is faster, than ==
# print(f'same as above - a is b?: ', a is b)

# -----------------------------------------------------

# # hash, isinstance, type
#
# print(dir(hash), help(hash))
# print(hash('Victor'), '\n')
# print(dir(isinstance), help(isinstance), '\n')
# print('Is "Hello" type is one from tuple?: ', isinstance("Hello", (float, int, str, list, dict, tuple)))
# print(dir(type), help(type))

# -----------------------------------------------------

# TODO: play a little more with open!

# open function
# https://docs.python.org/3.3/library/functions.html#open

# print(dir(open), help(open))

# ff = open('D:\Programming\Projects\skillbox study\\2. Data Scientist. Аналитика. Начальный уровень\open.py', 'r')
ff = open('open.py', 'r')
for line in ff:
    print(line, end='')
ff.close()







