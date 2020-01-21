# a, b = 'bic', 5
# print(a, b)
#
# my_list = []
# add = 1
# for i in range(3):
#     i = []
#     for j in range(3):
#         i.append((j+1)*add)
#     my_list.append(i)
#     add += 3
# print(my_list)
#
#
# # pair_list = [(1, 2), (3, 4), (5, 6)]
#
# for a, b, c in my_list:
#     print(a, b, c)
#     print(a+b+c)

# zoo_pets = ['lion', 'skunk', 'elephant', 'monkey', 'horse']
#
# for i, animal in enumerate(zoo_pets):
#     print(i, animal)

# new_list = [1, 4, 9, 16, 25, 36, 49]
#
# for i, number in enumerate(new_list):
#     print(i, number * 3)

# print(new_list)

#
# zoo_pets = [
#     'lion', 'skunk',
#     'elephant', 'horse',
# ]

# for animal in zoo_pets:
#     for char in animal:
#         print(char)
#     print('===')
#     print(animal)

lentach = ['¯', "\\", '_', '(', 'ツ', ')', '_', '/', '¯']

# for i in range(10):
#     print(30 * '*', end='')
#     print()
    # for j in range(10):
    #     print(j * '*', end='')
    # print()


# for i in range(4):
#     print(12 * '*', 25 * '-')
# for i in range(5):
#     print(37 * '-')

# zoo_pet_mass = {
#     'lion': 300,
#     'skunk': 5,
#     'elephant': 5000,
#     'horse': 400,
# }
#
# print(lentach)
# print(zoo_pet_mass.items())
# print(zoo_pet_mass)

# total_mass = 0
# for animal in zoo_pet_mass.values():
#     print(animal)
#     total_mass += animal
# print('Общая масса животных', total_mass)

# my_dict = {
#     'name': 'victor',
#     'surname': 'belkov',
#     'age': '34',
#     'sex': 'male',
#     'city': 'St. Petersburg',
#     'eyes': 'grey'
# }
#
# for i in my_dict:
#     print(i, my_dict[i])

# def power(number, pow):
#     print('Function called with parameters', number, pow)
#     power_value = number ** pow
#     return power_value
#
#
# my_list = [3, 14, 15, 92, 6]
# for element in my_list:
#     result = power(number=element, pow=2)
#     print(result)
#
# def create_default_user():
#     name = 'Victor'
#     age = 34
#     return name, age
#
# result = create_default_user()
# print(result)

# ---------------------------------------------------------------------------------------------------------------------

# my_list = [1, 2, 3]
#
# for elem in my_list:
#     print('for: ', elem)
# else:
#     elem = 'finito'
#
# print(elem)

# ---------------------------------------------------------------------------------------------------------------------

def add_item(item=1, add_list=[]):
    add_list.append(item)
    # print(add_list)
    return add_list


print(add_item())
print(add_item(2,))
print(add_item(3, [7, 8, 9]))
print(add_item(5))