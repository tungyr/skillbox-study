def calc(value):
    # print(f'Read line {value}')
    operand1, operation, operand2 = line.split(' ')
    operand1, operand2 = int(operand1), int(operand2)
    if operation == '+':
        value = operand1 + operand2
    elif operation == '-':
        value = operand1 - operand2
    elif operation == '/':
        value = operand1 / operand2
    elif operation == '*':
        value = operand1 * operand2
    elif operation == '//':
        value = operand1 // operand2
    elif operation == '%':
        value = operand1 + operand2
    else:
        print(f'Unknown operand {operation}')
    return value


total = 0
errors = 1
with open('calc.txt', 'r') as ff:
    for line in ff:
        line = line[:-1]
        try:

            total += calc(line)
        except ValueError as exc:
            print(exc)
            # print(f'Error {errors}::Cannot convert to int: {exc}, {exc.args}')
            errors += 1
            continue

print('total: ', total)


def div():
    for i in range(2):
        x = int(input("enter a number: "))
        y = int(input("enter another number: "))
        print(x, '/', y, '=', x / y)


def sumOfPairs(L1, L2):
    sum = 0
    sumOfPairs = []
    for i in range(len(L1)):
        sumOfPairs.append(L1[i] + L2[i])


print("sumOfPairs = ", sumOfPairs)