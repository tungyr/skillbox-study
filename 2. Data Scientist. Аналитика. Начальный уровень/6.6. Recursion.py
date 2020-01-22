# ----------------------------------------------------------------------------------------------------------

# Skillbox, 6.6 - 6.7. Recursion
# https://go.skillbox.ru/course/data-scientist-1/03299f49-36a8-444b-83a6-c2cfd2b2dc95

# def factorial(n):
#     print('factorial ', n)
#     if n == 1:
#         print('n = 1!')
#         return 1
#     factorial_n_minus_1 = factorial(n=n-1)
#     print(f'{n} (n) * {factorial_n_minus_1} (factorial_n_minus_1) = {n * factorial_n_minus_1}')
#     return n * factorial_n_minus_1

# print(factorial(6))

# -----------------------------------------------------

# # TODO: finish recursive function and grasp it's work principle
#
# some_list = [1, 2, 3, 4]
# i = 0
#
# def summary(summ_list, i):
#     print('summary with i ', i)
#     if i == 0:
#         print('i = 0!')
#         return summ_list[i]
#     summary_minus_1 = summary(summ_list, i=i-1)
#     if i < len(some_list):
#         print('summary_minus_1 + some_list[i + 1]: ', summary_minus_1 + some_list[i])
#         i += 1
#         return summary_minus_1 + some_list[i]
#     else:
#         print('final summary_minus_1: ', summary_minus_1)
#         return summary_minus_1
#
# summary(some_list, len(some_list))

# -----------------------------------------------------

# # TODO: finish recursive function and grasp it's work principle
# recursion for searching in trees

html_dom = {
    'html': {
        'head': {
            'title': 'Colobok',
        },
        'body': {
            'h2': 'Hello!',
            'div': 'Would you like I tell you fairytale?',
            'p': 'Once upon a time lived old man with his wife...',
        }
    }
}


def find_element(tree, element_name):
    if element_name in tree:
        return tree[element_name]
    for key, sub_tree in tree.items():
        if isinstance(sub_tree, dict):  # check whether object dict
            result = find_element(tree=sub_tree, element_name=element_name)
            if result:
                break
        else:
            result = None
        return result

res = find_element(tree=html_dom, element_name='head')
print(res)

# print(html_dom['html']['body'])
# print(html_dom['html']['body']['p'])