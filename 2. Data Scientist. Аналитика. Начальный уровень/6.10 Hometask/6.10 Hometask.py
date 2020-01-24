Функции
Домашнеезадание
1.
Почему возникла ошибка? Объясните и исправьте.

def factorial(n):
    f = 1
    for i in range(2, n + 1):
        f = f * i
    return f

​
factorial(3)
print(f)
---------------------------------------------------------------------------
NameError
Traceback(most
recent
call
last)
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

2.
Почему
переменная
S
после
запуска
функции
сохранила
значение
ноль?

S = 0


def sum(n, m):
    S = n + m
    return S

​
print(sum(3, 4))
print(S)
7
0
Объяснение:

3.
Почему
возникла
ошибка? Объясните
и
исправьте, чтобы
функция
могла
работать
с
данными
на
входе
в
примере
с
res.


def mult(*, q, w, e, r, t, y):
    return q + w + e + r + t + y


res = mult(1, 2, 3, 4, 5, 6)
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

TypeError: mult()
takes
0
positional
arguments
but
6
were
given

Объяснение:

4.
Почему
возникла
ошибка? Объясните
и
исправьте, чтобы
функция
могла
работать
с
данными
на
входе
в
примере.


def power(a, s, *, d):
    res = a ** s ** d
    print(res)


power(d=4, 5, 6)
​
File
"<ipython-input-28-4c11a09d0cf9>", line
4
power(d=4, 5, 6)
^
SyntaxError: positional
argument
follows
keyword
argument

5.
Почему
возникла
ошибка? Объясните
и
исправьте, чтобы
функция
могла
работать
с
данными
на
входе
в
примере.


def mult2(*args):
    res = 1
    for i in args:
        res += i
    return res

​
List = [1, 2, 3, 4, 5, 6, 7]
print(mult2(List))
---------------------------------------------------------------------------
TypeError
Traceback(most
recent
call
last)
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

6.
Почему
возникла
ошибка? Объясните
и
исправьте.


def some_function(a, b, **kwargs, *args):
    pass


File
"<ipython-input-52-efe9f896dc4b>", line
1


def some_function(a, b, **kwargs, *args):
    ^
    SyntaxError: invalid
    syntax

    Объяснение:

    7.
    Почему
    не
    был
    создан
    новый
    список
    при
    повторном
    запуске
    функции? Объясните
    и
    исправьте.

    def to_buy(*new_items, shopping_list=[]):
        for i in new_items:
            shopping_list.append(i)
        return shopping_list

    ​
    monday = to_buy('яблоки', 'молоко', 'хлеб')
    print(monday)
    ​
    tuesday = to_buy('груши', 'йогурт', 'мясо')
    print(tuesday)
    ​
    ['яблоки', 'молоко', 'хлеб']
    ['яблоки', 'молоко', 'хлеб', 'груши', 'йогурт', 'мясо']
    Объяснение:

    8.
    Измените
    данную
    функцию
    так, чтобы
    она
    распечатывала
    названия
    продуктов
    из
    словаря
    в
    примере.

    def print_all(*kwargs):
        for i in kwargs():
            print(i)

    print_all(*{'1': 'яблоки', '2': 'молоко', '3': 'хлеб', '4': 'груши', '5': 'йогурт', '6': 'мясо'})
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

    9.
    Программисты
    договорились, что
    переменные
    такого
    рода
    являются..(вопрос
    из
    лекции)

    TOKEN = ...
    Ответ:

    10.
    Напишите
    функцию, которая
    с
    помощью
    рекурсии
    считает
    сумму
    последовательности
    с
    шагом
    m.В
    качестве
    аргументов
    подаются
    целые
    положительные
    числа
    n(последний
    элемент
    последовательности) и
    m(шаг
    последовательности).Считается, что
    все
    члены
    последовательности
    являются
    целыми
    положительными
    числами.

    Пример:

    sum_of_seq(5, 1)
    15

    sum_of_seq(5, 9)
    5

    sum_of_seq(8, 2)
    20
    ### YOUR CODE HERE ###
    ​
    ​
    11.
    Напишите
    функцию, которая
    возводит
    число
    в
    положительную
    степень
    с
    помощью
    рекурсии.В
    качестве
    аргументов
    подаются
    целые
    положительные
    числа
    n(число)
    и
    m(степень).

    ### YOUR CODE HERE ###
    ​
    ​
    12.
    Напишите
    функцию, которая
    возводит
    число
    в
    отрицательную
    степень
    число
    с
    помощью
    рекурсии.В
    качестве
    аргументов
    подаются
    целое
    положительное
    число
    n(число)
    и
    целое
    отрицательное
    число
    m(степень).

    ### YOUR CODE HERE ###
    ​
    ​
    13.
    Напишите
    функцию, которая
    находит
    число
    Фиббоначи
    по
    его
    номеру.В
    качестве
    аргумента
    подается
    целое
    положительное
    число
    n(число).

    ### YOUR CODE HERE ###
    ​
    ​