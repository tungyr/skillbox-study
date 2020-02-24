# def calc(value):
#     # print(f'Read line {value}')
#     operand1, operation, operand2 = line.split(' ')
#     operand1, operand2 = int(operand1), int(operand2)
#     if operation == '+':
#         value = operand1 + operand2
#     elif operation == '-':
#         value = operand1 - operand2
#     elif operation == '/':
#         value = operand1 / operand2
#     elif operation == '*':
#         value = operand1 * operand2
#     elif operation == '//':
#         value = operand1 // operand2
#     elif operation == '%':
#         value = operand1 + operand2
#     else:
#         print(f'Unknown operand {operation}')
#     return value
#
#
# total = 0
# errors = 1
# with open('calc.txt', 'r') as ff:
#     for line in ff:
#         line = line[:-1]
#         try:
#
#             total += calc(line)
#         except ValueError as exc:
#             print(exc)
#             # print(f'Error {errors}::Cannot convert to int: {exc}, {exc.args}')
#             errors += 1
#             continue
#
# print('total: ', total)

# def div():
#     for i in range(2):
#         x = input("enter a number: ")
#         y = input("enter another number: ")
#         try:
#             x = int(x)
#             y = int(y)
#             x / y
#         except ValueError as exc:
#             print(f'Error: {exc.args} \nx and y must be integers!')
#             continue
#         except ZeroDivisionError as exc:
#             print(f'Error: {exc.args} \nSecond number must be greater then 0!')
#             continue
#         print(x, '/', y, '=', x / y)


def sumOfPairs(L1, L2):
    sum = 0
    sumOfPairs = []
    for i in range(len(L1)):
        sumOfPairs.append(L1[i] + L2[i])
    return sumOfPairs


print("sumOfPairs = ", sumOfPairs([1,2], [2, 3]))
# print("sumOfPairs = ", sumOfPairs(1, [2, 3]))# TypeError: object of type 'int' has no len()
# print("sumOfPairs = ", sumOfPairs(1, 3)) # TypeError: object of type 'int' has no len()
# print("sumOfPairs = ", sumOfPairs([a, 'b'], ['2', '3'])) # NameError: name 'a' is not defined
# print("sumOfPairs = ", sumOfPairs(['a', 'b', 'c'], ['2', '3'])) # IndexError: list index out of range
# print("sumOfPairs = ", sumOfPairs(['a', 'b'], [2, '3'])) # TypeError: can only concatenate str (not "int") to str
# print("sumOfPairs = ", sumOfPairs(['a', 'b'], [2, '3'])) # SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
print("sumOfPairs = ", sumOfPairs([-5, 'b'], [2, '3'])) # SyntaxError: closing parenthesis ')' does not match opening parenthesis '['