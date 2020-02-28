'''
Исключения
Домашняя работа
Вопросы по лекциям.

Как поймать вообще все ошибки, которые могут произойти?

Ответ:
написать в коде "except BaseException"

Сколько раз подряд можно указывать except?
Ответ:
Неограниченное количество раз

Вы хотите с помощью print вывести название ошибки в консоль, как это сделать?

Ответ:
Это можно сделать обернув класс ошибки в менеджер контекста "with...as" и вывести с помощью print:
except ValueError as error:
    print(error)


Вы хотите с помощью print вывести параметры ошибки в консоль, как это сделать?

Ответ:
С помощью менеджера контекста "with...as" можно вывести параметры ошибки ".args:" с помощью print:
except ValueError as error:
    print(error.args)

Что такое DeprecationWarning?

Ответ:
DeprecationWarning используется в библиотеках при вызове тех или иных функций. С помощью DeprecationWarning разработчики
библиотеки дают понять пользователям библиотеки, что используемая функция не будет поддерживаться в следующих версиях
библиотеки и вследствие этого могут возникнуть трудности в совместимости версий в будущем.

Разминочные задания.

Вам даны две функции. Поисследуйте, какие ошибки могут возникнуть при их реализации.Обработайте эти ошибки.

'''


def div():
    for i in range(2):
        x = input("enter a number: ")
        y = input("enter another number: ")
        try:
            x, y = int(x), int(y)
            print(x, '/', y, '=', x / y)
        except ValueError as exc:
            print(f'Error: {exc.args} \nx and y must be integers!')
        except ZeroDivisionError as exc:
            print(f'Error: {exc.args} \nSecond number must be greater then 0!')

# div()


def sumOfPairs(L1, L2):
    try:
        sum = 0
        sumOfPairs = []
        for i in range(len(L1)):
            sumOfPairs.append(L1[i] + L2[i])
        return sumOfPairs

    except TypeError as exc:
        print(f'Function parameters should be lists or strokes only:', {exc.args})
    except IndexError as exc:
        print(f'First function parameter length should be less then second parameter length:', {exc.args})



sumOfPairs([1, 2], [1, 2, 3])

'''
Задание 1. 
Есть файл с протоколом регистраций пользователей на сайте(registrations.txt). Каждая строка содержит 
информацию о имени, электронной почте и возрасте человека.

Надо проверить данные из файла, для каждой строки:

- присутсвуют все три поля 
- поле имени содержит только буквы 
- поле email содержит @ и .
- и поле возраст является числом от 10 до 99

В результате проверки нужно сформировать два файла registrations_good.log для правильных данных, записывать строки как
есть registrations_bad.log для ошибочных, записывать строку и вид ошибки. Для валидации строки данных написать метод, 
который может выкидывать исключения:

- НЕ присутсвуют все три поля: ValueError
- поле имени содержит НЕ толькобуквы: NotNameError(кастомное исключение)
- поле email НЕ содержит @ и.(точку): NotEmailError(кастомное исключение)
- поле возраст НЕ является числом от 10 до 99: ValueError Вызов метода обернуть в try-except.
'''
class NotNameError(Exception):
    """Name exception class with possibility of setting user error message"""
    message = 'name is invalid!'

    def __init__(self, value, message=message):
        self.value = value
        self.message = message

    def __str__(self):
        return f'Name error: "{self.value}" {self.message}'


class NotEmailError(Exception):
    """E-mail exception class with possibility of setting user error message"""
    message = 'address is invalid!'

    def __init__(self, value, message=message):
        self.value = value
        self.message = message

    def __str__(self):
        return f'E-mail error: "{self.value}" {self.message}'


def validate(registration):
    """Validate registration data"""

    registration = registration.split()
    if len(registration) < 3:
        raise ValueError(f'Only {len(registration)} field(s) present!')

    elif registration[0].isalpha() is False:
        raise NotNameError(registration[0])

    elif '.' and '@' not in registration[1]:
        raise NotEmailError(registration[1])

    try:
        if int(registration[2]) not in range(10, 100):
            raise ValueError(f'"{registration[2]}" is not valid age!')
    finally:
        pass


def read_file():
    """Read file with registration data and catch exceptions"""
    registration_good = []
    registration_bad = []
    with open('registrations_.txt', 'r') as ff:
        for line in ff:
            line = line.rstrip('\n')
            try:
                validate(line)
            except BaseException as exc:
                # exc already consist of error type so BaseException used
                registration_bad.append(line + f' - {str(exc)}\n')
                continue
            else:
                registration_good.append(line + '\n')
        write_file(registration_good, registration_bad)


def write_file(registration_good, registration_bad):
    """Write files with good and bad registration data"""
    with open('registration_good.txt', 'w') as ff:
        for registration in registration_good:
            ff.write(registration)

    with open('registration_bad.txt', 'w') as ff:
        for registration in registration_bad:
            ff.write(registration)


read_file()
'''