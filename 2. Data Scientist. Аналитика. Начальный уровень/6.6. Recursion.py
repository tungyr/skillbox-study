# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------

# # Skillbox, 6.6 - 6.7. Recursion
# # https://go.skillbox.ru/course/data-scientist-1/03299f49-36a8-444b-83a6-c2cfd2b2dc95
#
# def factorial(n):
#     print('factorial ', n)
#     if n == 1:
#         print('n = 1!')
#         return 1
#     factorial_n_minus_1 = factorial(n=n-1)
#     print(f'{n} (n) * {factorial_n_minus_1} (factorial_n_minus_1) = {n * factorial_n_minus_1}')
#     return n * factorial_n_minus_1
#
# print(factorial(6))

# -----------------------------------------------------

# TODO: grasp on how this recursive beast is working!!!

some_list = [1, 2, 3]
function_calls = 0

def summary(summ_list, i):
    global function_calls
    function_calls += 1
    print('summary with i ', i)
    if i == 0:
        print('i = 0!')
        return summ_list[i]
    print('before next_call')
    next_call = summary(summ_list, i=i-1)
    print('after next_call')
    if i < len(summ_list):
        next_call = next_call + summ_list[i]
        print('next_call + summ_list[i]', next_call)
        return next_call
    else:
        print('final next_call: ', next_call)
        return next_call

summary(some_list, 3)

# -----------------------------------------------------

# # recursion for searching in trees
#
# html_dom = {
#     'html': {
#         'head': {
#             'title': 'Colobok',
#         },
#         'body': {
#             'h2': 'Hello!',
#             'div': 'Would you like I tell you fairytale?',
#             'p': 'Once upon a time lived old man with his wife...',
#         }
#     }
# }
#
#
# def find_element(tree, element_name):
#     if element_name in tree:
#         return tree[element_name]
#     for key, sub_tree in tree.items():
#         if isinstance(sub_tree, dict):  # check whether object dict
#             result = find_element(tree=sub_tree, element_name=element_name)
#             if result:
#                 break
#         else:
#             result = None
#         return result
#
# res = find_element(tree=html_dom, element_name='html')
# print(res)
#
# # print(html_dom['html']['body'])
# # print(html_dom['html']['body']['p'])