'''
Функции
Домашнеезадание
1. Почему возникла ошибка? Объясните и исправьте.

'''

def factorial(n):
    f = 1
    for i in range(2, n + 1):
        f = f * i
    return f

# factorial(3)
# print(f)  # wrong
# print(factorial(3))

'''
---------------------------------------------------------------------------
NameError
Traceback(most recent call last) 
< ipython - input - 11 - 9e89138602
aa > in < module > ()
6
7
factorial(3)
----> 8
print(f)

NameError: name
'f' is not defined

Объяснение:
Функция print() обращается к локальной переменной f, которая объявлена внутри функции factorial(), что и вызывает ошибку. 
Решением может быть объявление переменной f в глобальной области видимости. Т.к. Python производит интерпретацию справа 
от оператора "=", мы получим ошибку "Local variable referenced before assignment". Нам придется внутри функции 
factorial() использовать ключевое слово global f, чтобы дать понять Python откуда брать значение переменной f. Это не 
очень хорошо, потому что в больших проектах ухудшает понимание кода. Возможно, оптимальным вариантом могло бы быть 
использование вызова функции factorial() в качестве аргумента функции print(). 
 
'f' is defined inside function and that's why it's a local variable. The problem that it's called from outer scope.
The solution is to define 'f' in outer scope.


2.Почему переменная S после запуска функции сохранила значение ноль?

'''
S = 0

def sum(n, m):
    S = n + m
    return S

# print(sum(3, 4))
# print(S)

'''
7
0
Объяснение:
Функция print(S) принимает в качестве аргумента глобальную переменную S, которая изначально была равна 0 и не менялась
по ходу выполнения программы. Внутри функции sum() присутствует другая переменная S, локальная, отличная от глобальной 
переменной S.


3. Почему возникла ошибка? Объясните и исправьте, чтобы функция могла работать с данными на входе в примере с res.
'''

def mult(*, q, w, e, r, t, y):
    return q + w + e + r + t + y


# res = mult(1, 2, 3, 4, 5, 6) # wrong
# res = mult(q=1, w=2, e=3, r=4, t=5, y=6)
# res_dict = {'q': 1, 'w': 2, 'e': 3, 'r': 4, 't': 5, 'y': 6}
# res = mult(**res_dict)


'''
---------------------------------------------------------------------------
TypeError
Traceback(most
recent
call
last)
< ipython - input - 25 - 276
f6ede15a2 > in < module > ()
1


def mult(*, q, w, e, r, t, y):
    2
    return q + w + e + r + t + y


----> 3
res = mult(1, 2, 3, 4, 5, 6)

TypeError: mult() takes 0 positional arguments but 6 were given 

Объяснение: знак "*" в параметрах функции mult(), говорит о том, что все аргументы на вход функции должны
 быть именованными. Есть два варианта решения ошибки: напрямую указывать ключи при вызове функции, либо 
 распаковывать на вход функции mult() словарь с аргументами mult(**res_dict). 

4. Почему возникла ошибка? Объясните и исправьте, чтобы функция могла работать с данными на входе в примере.

'''
def power(a, s, *, d):
    res = a ** s ** d
    print(res)


# power(d=4, 5, 6) # wrong
# power(5, 6, d=4)

'''
File
"<ipython-input-28-4c11a09d0cf9>", line
4
power(d=4, 5, 6)
^
SyntaxError: positional argument follows keyword argument

Объяснение: наличие позиционных аргументов после именованного в вызове функции вызывает ошибку. Следует перенести 
именованный аргумент в конец списка аргументов.

5.
Почему возникла ошибка? Объясните и исправьте, чтобы функция могла работать с данными на входе в примере.
'''

def mult2(*args):
    res = 1
    for i in args:
        res += i
    return res


# List = [1, 2, 3, 4, 5, 6, 7]
# # print(mult2(List))  # wrong
# print(mult2(*List))
'''
---------------------------------------------------------------------------
TypeError Traceback(most recent call last)
< ipython - input - 48 - 8e59
e484de93 > in < module > ()
6
7
List = [1, 2, 3, 4, 5, 6, 7]
----> 8
print(mult2(List))

< ipython - input - 48 - 8e59
e484de93 > in mult2(*args)
2
res = 1
3
for i in args:
    ----> 4
res += i
5
return res
6

TypeError: unsupported
operand
type(s)
for +=: 'int' and 'list'

Объяснение: чтобы функция mult() могла принять в качестве аргументов элементы списка List, а не сам список,
необходимо в вызове функции распаковать список с помощью знака "*".

6.
Почему возникла ошибка? Объясните и исправьте.
'''

# def some_function(a, b, **kwargs, *args):  # wrong
def some_function(a, b, *args, **kwargs):
    pass

'''
File
"<ipython-input-52-efe9f896dc4b>", line
1


def some_function(a, b, **kwargs, *args):
    ^
    SyntaxError: invalid
    syntax

    Объяснение: *args, принимающий любые позиционные аргументы на вход функции some_function() не может стоять
     после **kwargs, принимающего любые именованные аргументы.

    7.
    Почему не был создан новый список при повторном запуске функции? Объясните и исправьте.
'''


# def to_buy(*new_items, shopping_list=[]):  # wrong
#     for i in new_items:
#         shopping_list.append(i)
#     return shopping_list

def to_buy(*new_items, shopping_list=None):
    if shopping_list == None:
        shopping_list = []
    for i in new_items:
        shopping_list.append(i)
    return shopping_list

# monday = to_buy('яблоки', 'молоко', 'хлеб')
# print(monday, id(monday))
#
# tuesday = to_buy('груши', 'йогурт', 'мясо')
# print(tuesday, id(tuesday))

'''   ​
 ['яблоки', 'молоко', 'хлеб']
 ['яблоки', 'молоко', 'хлеб', 'груши', 'йогурт', 'мясо']
 
 Объяснение: т.к. списки - это изменяемые объекты, после создания списка при первом вызове функции этот список остается 
 в памяти и используется при всех последующих вызовах функции, независимо от применения к нему новых имен. Как вариант,
 можно явно передавать в функцию свой список (каждый раз предварительно создавая новый), заменяя список по умолчанию. 
 Либо создавать список при условии его отсутствия в передаваемых при вызове функции аргументов. 

 8. Измените данную функцию так, чтобы она распечатывала названия продуктов из словаря в примере.
 '''

# def print_all(**kwargs):
#     for i in kwargs.values():
#         print(i)
#
# print_all(**{'1': 'яблоки', '2': 'молоко', '3': 'хлеб', '4': 'груши', '5': 'йогурт', '6': 'мясо'})

'''
 ---------------------------------------------------------------------------
 TypeError
 Traceback(most
 recent
 call
 last)
 < ipython - input - 63 - 23
 f30bebf8ac > in < module > ()
 3
 print(i)
 4
 ----> 5
 print_all(**{'x': 'яблоки', 'y': 'молоко', 'z': 'хлеб', 'e': 'груши', 'o': 'йогурт', 'p': 'мясо'})

 < ipython - input - 63 - 23
 f30bebf8ac > in print_all(**kwargs)
 1

 def print_all(**kwargs):

     ----> 2
 for i in kwargs():
     3
     print(i)
     4
     5
     print_all(**{'x': 'яблоки', 'y': 'молоко', 'z': 'хлеб', 'e': 'груши', 'o': 'йогурт', 'p': 'мясо'})

 TypeError: 'dict'
 object is not callable

 9. Программисты договорились, что переменные такого рода являются..(вопрос из лекции)

 TOKEN = ...
 Ответ: Константы

 10. Напишите функцию, которая с помощью рекурсии считает сумму последовательности с шагом m.В качестве аргументов 
 подаются целые положительные числа n(последний элемент последовательности) и m(шаг последовательности).Считается, что
 все члены последовательности являются целыми положительными числами.

 Пример:

 sum_of_seq(5, 1)
 15

 sum_of_seq(5, 9)
 5

 sum_of_seq(8, 2)
 20

'''
#
#
# def summary():
#     """Function recursively calculates summary of integers row, defined by user"""
#     result = 0
#
#     def recursive_sum(calc_list, countdown):
#         """Recursive calculation of integers range sum"""
#         if countdown == 0:
#             return calc_list[countdown]
#         next_call = recursive_sum(calc_list, countdown=countdown - 1)
#         if countdown < len(calc_list):
#             next_call = next_call + calc_list[countdown]
#             return next_call
#         else:
#             return next_call
#
#     while True:
#         user_input = input('Enter amount of integers n, calculation step m separated by comma. Example: 1, 2: ')
#
#         # check whether user input consist of integers
#         try:
#             user_input = user_input.split(',')
#             user_input = [int(i) for i in user_input]
#             range_n, step_m = user_input
#             print(f'You have entered: n = {range_n}, m = {step_m}')
#         except ValueError:
#             again = input('Something went wrong! Input should be like this: 1, 2. Try again? y/n: ')
#             if again == 'y':
#                 continue
#             else:
#                 break
#         else:
#             # check whether user input consist of positive integers
#             if range_n <= 0 or step_m <= 0:
#                 again = input('Integers are less or equal to 0! Input should be like this: 1, 2. Try again? y/n: ')
#                 if again == 'y':
#                     continue
#                 else:
#                     break
#
#         generated_list = list(range(1, range_n + 1))
#         print(generated_list)
#         # check for step bigger than last integer row value
#         if range_n <= step_m:
#             print(f'Sum of integers in row {generated_list} with step {step_m} is {generated_list[-1]}')
#         else:
#             # include in integer row only values as per step m
#             generated_list = generated_list[step_m - 1::step_m]
#             print('generated_list[::m]: ', generated_list)
#             result = recursive_sum(calc_list=generated_list, countdown=range_n)
#             print(f'Sum of integers in row {generated_list} with step {step_m} is {result}')
#         return result


# summary()


'''
​
11. Напишите функцию, которая возводит число в положительную степень с помощью рекурсии.В качестве аргументов подаются
целые положительные числа n(число) и m(степень).

'''


def exponent():
    """Function recursively calculates power of integer with base number and exponent defined by user"""
    result = 0



    while True:
        user_input = input('Enter base integer n, exponent - integer m separated by comma. Example: 2, 3: ')

        # check whether user input consist of integers
        try:
            user_input = user_input.split(',')
            user_input = [int(i) for i in user_input]
            base_n, exponent_m = user_input
            print(f'You have entered: base n = {base_n}, exponent m = {exponent_m}')
        except ValueError:
            again = input('Something went wrong! Input should be like this: 2, 3. Try again? y/n: ')
            if again == 'y':
                continue
            else:
                break
        else:
            # check whether user input consist of positive integers
            if base_n <= 0 or exponent_m <= 0:
                again = input('Integers are less or equal to 0! Input should be like this: 2, 3. Try again? y/n: ')
                if again == 'y':
                    continue
                else:
                    break


        def recursive_exponent(base, exponent):
            """Recursive calculation power of integer"""
            if exponent == 0:
                return base * base
            next_call = recursive_exponent(base, exponent=exponent - 1)
            next_call = next_call + base * base
            print(next_call)
            return next_call

        recursive_exponent(base=base_n, exponent=exponent_m)


exponent()


'''

12. Напишите функцию, которая возводит число в отрицательную степень число с помощью рекурсии.В качестве аргументов
подаются целое положительное число n(число) и целое отрицательное число m(степень).

### YOUR CODE HERE ###
​
​
13. Напишите функцию, которая находит число Фиббоначи по его номеру.В качестве аргумента подается целое положительное
число n(число).

### YOUR CODE HERE ###
'''