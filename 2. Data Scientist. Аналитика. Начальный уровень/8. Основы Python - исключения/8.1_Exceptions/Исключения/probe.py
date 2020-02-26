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

def div():
    for i in range(2):
        x = input("enter a number: ")
        y = input("enter another number: ")
        try:
            x = int(x)
            y = int(y)
            print(x, '/', y, '=', x / y)
        except ValueError as exc:
            print(f'Error: {exc.args} \nx and y must be integers!')
        except ZeroDivisionError as exc:
            print(f'Error: {exc.args} \nSecond number must be greater then 0!')
div()


def sumOfPairs(L1, L2):
    try:
        sum = 0
        sumOfPairs = []
        for i in range(len(L1)):
            sumOfPairs.append(L1[i] + L2[i])
        return sumOfPairs

    except TypeError:
        print('Function parameters should be lists or strokes only')
    except IndexError:
        print('First function parameter length should be less then second parameter length')



def func_check(L1, L2):
    try:
        result = "sumOfPairs = ", sumOfPairs(L1, L2)
        print(result)
        return result
    except NameError as exc:
        print(f'Function parameters should be lists or strokes only, {exc}')


func_check([1, 2], [1, 2, 3])