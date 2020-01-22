# ----------------------------------------------------------------------------------------------------------
# Skillbox 6.1 - 6.5 Python functions, namespace etc.
# https://go.skillbox.ru/course/data-scientist-1/c449f346-516e-4f66-b261-402bcacee535

# my_list = [1, 2, 3]
#
# for elem in my_list:
#     print('for: ', elem)
# else:
#     elem = 'finito'
#
# print(elem)

# -----------------------------------------------------

# demand to point out function parameters explicitly after "*":


# def vector_module(x, y, *, z):
# # def vector_module(*, x, y, z):
#     print(x + y + z)
#     return(x + y + z)
#
#
# # won't work
# # res = vector_module(3, 4, 5)
# # it's ok
# res = vector_module(3, 4, z=4)
# # res = vector_module(x=3, y=4, z=5)

# -----------------------------------------------------

# positional argument in function call can't follow the keyword argument:

# def vector_module_2(x, y, z):
# # def vector_module(*, x, y, z):
#     print(x + y + z)
#     return(x + y + z)
#
# # wrong
# res_2 = vector_module(3, y=4, 5)
# # correct
# # res_2 = vector_module(3, 4, z=5)

# -----------------------------------------------------

# unpacking parameters from list/ dict in function:

# some_list = [1, 2, 3]
# some_dict = {'x': 1, 'y': 2, 'z': 3}
#
# def vector_module_2(x, y, z):
#     print(x + y + z)
#     return(x + y + z)
#
# vector_module_2(*some_list)
# vector_module_2(**some_dict)
#
# # combined parameters from list and dict:
# new_some_list = [2, 3]
# new_dict = dict(z=4)
# new_call = vector_module_2(*new_some_list, **new_dict)
# print('new_call: ', new_call)

# -----------------------------------------------------

# default function parameters:

# def washing(who='I', what='window', when='today'):
#     print(who, 'wash', what, when)
#
# washing()
# washing(who='He', what='car', when='yesterday')

# -----------------------------------------------------

# mutable elements, like list in parameters, creates on a stage of compilation and keeps existent during work of func
# if you don't call function with set list as function parameter explicitly!

# def add_item(item=1, add_list=[]):
#     add_list.append(item)
#     # print(add_list)
#     return add_list
#
#
# print(add_item())
# print(add_item(2,))
# print(add_item(3, [7, 8, 9]))
# print(add_item(5))

# -----------------------------------------------------

# arbitrary params *args (type tuple) and **kwargs (type dict)

def print_items_v1(*args):
    print('*args function')
    print(type(args))
    print(args)
    for i, item in enumerate(args):
        print(f'{i} - {item} - {type(item)}')
    return args


# print_items('a', 1, 6.9, False, [1, 2, 3])
# print_items('a', 1, 6.9, False, [1, 2, 3], ('hello', 5), print_items())

# unpacking - '*' let us unpack elements of list like separate param in args:

# my_list = ['a', 1, 6.9, False, [1, 2, 3], ('hello', 5)]
# print_items_v1(*my_list)


# kwargs = keyword arguments

# def print_items_v2(**kwargs):
#     print('**kwargs function:  ', '\n')
#     print(type(kwargs))
#     print(kwargs)
#     for key, value in kwargs.items():
#         print(f'{key} - {value} - {type(value)}')
#     return kwargs
#
# print_items_v2(name='Victor', age=34, address=['SPB', 'Nevskiy', 1])
#
# # unpacking dictionary to function
# user = {'name': 'Victor', 'age': 34}
# print_items_v2(**user)


def print_items_v3(a, b=3, *args, **kwargs):
    print('Function with combined parameters:  ', '\n')
    print(f'a = {a}, b = {b}')
    print('args: ', args, type(args))
    print('kwargs: ', kwargs, type(kwargs))


print_items_v3(1, 3, 5, 8, 256, 17, 'new', name='Victor', age=34, address=['SPB', 'Nevskiy', 1])


