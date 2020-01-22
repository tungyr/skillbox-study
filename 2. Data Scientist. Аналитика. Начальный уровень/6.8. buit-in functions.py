# ----------------------------------------------------------------------------------------------------------

# Skillbox, 6.8 - 6.9. built-in functions
# https://go.skillbox.ru/course/data-scientist-1/bc6862da-fbd2-4547-afd1-79950f6a5dd8


# # list/set composes only from keys of dict during converting dict -> list/set:
# my_dict = {1: 2, 3: 4}
# print(list(my_dict))
# print(set(my_dict))
#
# # creation dict from list list -> dict:
# dict_fr_list = dict([('a', 1), ('b', 2), ('c', 3)])
# print(dict_fr_list)

# -----------------------------------------------------

# # max(), min() work only with same type elements in list:
# figure_list = [5, 3, 1, 4, 2]
# # figure_list = [1, 2, 3, '4', 5]
# letter_list = ['a', 'b', 'c', 'd']
# # letter_list = ['a', 'b', 4, 'd']
# print(f'max in {figure_list} is {max(figure_list)}')
# print(f'max in {letter_list} is {max(letter_list)}')
# print(f'min in {figure_list} is {min(figure_list)}')
# print(f'min in {letter_list} is {min(letter_list)}')
#
# print(sorted(figure_list))

# -----------------------------------------------------

# zip function:

days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
# days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat']
profit = [100, 200, 50, 120, 300, 180, 0]
# profit = [100, 200, 50, 120, 300, 180]
revenue_for_list = zip(days, profit)
revenue_for_dict = zip(days, profit

# result of zip function should be converted to list/dict to display!
print('revenue list: ', list(revenue_for_list))
print('revenue dict: ', dict(revenue_for_dict))

