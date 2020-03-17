'''

Классы
Домашнее задание
Вопросы по лекциям
1.
Напишите название функции, которая является конструктором класса.

Ответ:

__init__(self)

2.
На что указывает переменная self?

Ответ:

На сам объект(instance)

3.
С помощью какой функции можно проверить, что некая строка является именем одного из атрибутов объекта?

Ответ:

hasattr()

4.
Когда вызывается метод __del__? (относительно события удаления объекта)

Ответ:

Метод __del__ вызывается каждый раз, когда на объект в коде не остается ни одной ссылки. Можно вызвать __del__
явно для удаления объекта в конце выполнения функции, например.


5.
Верно ли, что атрибут класса перекрывает атрибут объекта?

Ответ:

Если объекту присваивается атрибут с таким же именем как в классе, то он перекрывает, или переопределяет, атрибут класса.

6.
Можно ли атрибуты базового класса вызывать в дочернем классе? Если да, то напишите, нет ли исклчений?

Ответ:

Вызывать атрибуты базового класса можно в дочернем, если только они не системные и не начинаются с двойного подчеркивания.

7.
Объясните своими словами для чего нужен метод super.

Ответ:

Метод super позволяет вызывать базовый метод и на его основе дополнять нужную функциональность в методе дочернего класса.

Практика

Напишите класс Fraction для работы с дробями. Пусть дробь в нашем классе предстает в виде числитель/знаменатель.
Дробное число должно создаваться по запросу Fraction(a, b), где a – это числитель, а b – знаменатель дроби.
Добавьте возможность сложения (сложения через оператор сложения) для дроби. Предполагается, что операция сложения
может проводиться как только между дробями, так и между дробью и целым числом. Результат оперции должен быть
представлен в виде дроби.

Добавьте возможность взятия разности (вычитания через оператор вычитания) для дробей. Предполагается, что операция
вычитания может проводиться как только для двух дробей, так и для дроби и целого числа. Результат оперции должен быть
представлен в виде дроби.

Добавьте возможность умножения (умножения через оператор умножения) для дробей. Предполагается, что операция умножения
может проводиться как только для двух дробей, так и для дроби и целого числа. Результат оперции должен быть представлен
в виде дроби.

Добавьте возможность приведения дроби к целому числу через стандартную функцию int().
Добавьте возможность приведения дроби к числу с плавающей точкой через стандартную функцию float().
Создайте дочерний класс OperationsOnFraction и добавьте туда собственные методы getint и getfloat, которые будут
возвращять целую часть дроби и представление дроби в виде числа с плавающей точкой соответственно.
### YOUR CODE HERE ###
​
'''


class Fraction:
    """Class of fraction consist of numerator a and denominator b(which is 1 by default)"""

    def __init__(self, numerator_a, denominator_b=1):
        # validate numerator and denominator
        try:
            numerator_a = int(numerator_a)
        except ValueError:
            print(f'Numerator {numerator_a} is not an integer!')
            raise

        try:
            denominator_b = int(denominator_b)
        except ValueError:
            print(f'Denominator {denominator_b} is not an integer!')
            raise

        self.numerator_a = numerator_a
        self.denominator_b = denominator_b
        self.fraction = str(numerator_a) + '/' + str(denominator_b)

    def __str__(self):
        return f'{self.__class__.__name__} {self.fraction}'

    def least_common_multiple_func(self, other_denominator) -> int:
        """The least common multiple defining"""
        least_common_mult = self.denominator_b
        while (least_common_mult % self.denominator_b + least_common_mult % other_denominator) != 0:
            least_common_mult += 1
        return least_common_mult

    def common_divisor(self, numerator_a, denominator_b) -> [None, int]:
        """A common divisor defining"""
        divisors = []
        for divisor in range(2, max(numerator_a, denominator_b)):
            if max(numerator_a, denominator_b) % divisor == 0:
                divisors.append(divisor)
        for divisor in range(2, min(numerator_a, denominator_b)):
            if min(numerator_a, denominator_b) % divisor == 0:
                if divisor in divisors:
                    return divisor
        return None

    def __add__(self, other) -> object:
        """Addition of two fractions"""
        least_common_multiple = self.denominator_b
        # check denominators of fractions and if no define their least common multiple
        if self.denominator_b != other.denominator_b:
            least_common_multiple = self.least_common_multiple_func(other.denominator_b)

        common_numerator = (least_common_multiple / self.denominator_b * self.numerator_a) + \
                           (least_common_multiple / other.denominator_b * other.numerator_a)

        # check for common divisor
        common_divisor = self.common_divisor(int(common_numerator), least_common_multiple)
        if common_divisor is None:
            res = Fraction(common_numerator, least_common_multiple)
        else:
            common_numerator = common_numerator / common_divisor
            least_common_multiple = least_common_multiple / common_divisor
            res = Fraction(common_numerator, int(least_common_multiple))
        return res

    def __sub__(self, other) -> object:
        """Substitution of two fractions"""
        least_common_multiple = self.denominator_b
        # check denominators of fractions and if no define their least common multiple
        if self.denominator_b != other.denominator_b:
            least_common_multiple = self.least_common_multiple_func(other.denominator_b)

        common_numerator = (least_common_multiple / self.denominator_b * self.numerator_a) - \
                           (least_common_multiple / other.denominator_b * other.numerator_a)

        # check for common divisor
        common_divisor = self.common_divisor(int(common_numerator), least_common_multiple)
        if common_divisor is None:
            res = Fraction(common_numerator, least_common_multiple)
        else:
            common_numerator = common_numerator / common_divisor
            least_common_multiple = least_common_multiple / common_divisor
            res = Fraction(common_numerator, int(least_common_multiple))
        return res

    def __mul__(self, other) -> object:
        """Multiplication of two fractions"""
        common_numerator = self.numerator_a * other.numerator_a
        common_denominator = self.denominator_b * other.denominator_b

        # check for common divisor
        common_divisor = self.common_divisor(int(common_numerator), common_denominator)
        if common_divisor is None:
            res = Fraction(common_numerator, common_denominator)
        else:
            common_numerator = common_numerator / common_divisor
            common_denominator = common_denominator / common_divisor
            res = Fraction(common_numerator, int(common_denominator))
        return res

    def __int__(self) -> int:
        """Returns int number from fraction"""
        integer_number = self.numerator_a // self.denominator_b
        print(f'Fraction {self.fraction} integer number is {integer_number}')
        return integer_number

    def __float__(self) -> float:
        """Returns float number from fraction"""
        float_number = self.numerator_a / self.denominator_b
        print(f'Fraction {self.fraction} float number is {float_number}')
        return float_number


class OperationsOnFraction(Fraction):
    """Converting fractions to int and float types"""
    def __init__(self, numerator_a=0, denominator_b=0):
        super().__init__(numerator_a=numerator_a, denominator_b=denominator_b)

    def getint(self, fraction) -> int:
        """Returns int number from fraction based on base class __int__() method"""
        self.numerator_a = fraction.numerator_a
        self.denominator_b = fraction.denominator_b
        self.fraction = str(self.numerator_a) + '/' + str(self.denominator_b)
        return super().__int__()


    def getfloat(self, fraction) -> float:
        """Returns float number from fraction based on base class __float__() method"""
        self.numerator_a = fraction.numerator_a
        self.denominator_b = fraction.denominator_b
        self.fraction = str(self.numerator_a) + '/' + str(self.denominator_b)
        return super().__float__()






my_fraction = Fraction(9, 2)
other_fraction = Fraction(8, 3)
# print(my_fraction)
# print(other_fraction)
summ = my_fraction + other_fraction
# print('summ:', summ)
subs = my_fraction - other_fraction
# print('subs:', subs)
# mult = my_fraction * other_fraction
# print('mult:', mult)
#
# print()
# integer_summ = int(summ)
# integer_subs = int(subs)
# integer_mult = int(mult)
#
# print()
# float_summ = float(summ)
# float_subs = float(subs)
# float_mult = float(mult)

print()
operations = OperationsOnFraction()


get_integer_summ = operations.getint(summ)
get_float_subs = operations.getfloat(subs)





