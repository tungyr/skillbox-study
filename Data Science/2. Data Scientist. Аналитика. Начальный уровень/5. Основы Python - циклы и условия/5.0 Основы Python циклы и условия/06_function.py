# def power(number, pow):
#     """This function involutes any integer"""
#     print('Function called with parameters', number, pow)
#     power_value = number ** pow
#     return power_value
#
#
# my_list = [3, 14, 15, 92, 6]
# for element in my_list:
#     result = power(number=element, pow=2)
#     print(result)

# def create_default_user():
#     """This function creates default user"""
#
#     name = 'Victor'
#     age = 34
#     return name, age
#
# result = create_default_user()
# print(result)
#
# user_name, user_age = create_default_user()
# print(user_name, user_age)
#
# print(power.__doc__)
# print(create_default_user.__doc__)

# def multiply(number_1, number_2):
#     """Function for multiplication of integers"""
#     if isinstance(number_1, int):
#         print('Function called with parameters ', number_1, number_2)
#         value = number_1 * number_2
#         return value
#     else:
#         return 'error'


# print(multiply(number_1=42, number_2=27))
# print(multiply(number_1='hello ', number_2=34))

def remove_fr_list(some_list, removing_item):
    """Function for removing items from list"""
    if isinstance(some_list, list):
        is_found = removing_item in some_list
        if is_found:
            some_list.remove(removing_item)
            print(removing_item, 'removed from list ', some_list)
            return is_found
        else:
            print('No item ', removing_item, 'in list', some_list)
    else:
        print('Wrong type of parameter!', type(some_list))


zoo_list = ['lion', 'skunk', 'elephant', 'horse', 'elephant']
remove_fr_list(some_list=6, removing_item='zebra')
print(remove_fr_list.__doc__)
# remove_fr_list(some_list=zoo_list, removing_item='elephant')
# remove_fr_list(some_list=zoo_list, removing_item='elephant')


