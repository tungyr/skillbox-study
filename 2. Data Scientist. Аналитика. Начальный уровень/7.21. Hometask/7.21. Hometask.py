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
    """Class of fraction consits of numerator a and denominator b"""

    def __init__(self, numerator_a, denominator_b=1):
        # validate numerator and denominator
        try:
            numerator_a = int(numerator_a)
        except ValueError:
            print(f'Numerator {numerator_a} is not an integer!')
            return

        try:
            denominator_b = int(denominator_b)
        except ValueError:
            print(f'Denominator {denominator_b} is not an integer!')
            return

        self.numerator_a = numerator_a
        self.denominator_b = denominator_b
        self.fraction = str(numerator_a) + '/' + str(denominator_b)

    def __str__(self):
        return f'{self.__class__.__name__} {self.fraction}'

    def least_common_multiple(self, other_denominator):
        least_common_mult = self.denominator_b
        while (least_common_mult % self.denominator_b + least_common_mult % other_denominator) != 0:
            least_common_mult += 1
        return least_common_mult

    def __add__(self, other):
        least_common_multiple = self.denominator_b
        # check denominators of fractions and if no define their least common multiple
        if self.denominator_b != other.denominator_b:
            least_common_multiple = self.least_common_multiple(other.denominator_b)

        common_numerator = (least_common_multiple / self.denominator_b * self.numerator_a) + \
                       (least_common_multiple / other.denominator_b * other.numerator_a)
        # if common_numerator % least_common_multiple == 0:
        #     common_numerator = common_numerator / least_common_multiple
        res = Fraction(common_numerator, least_common_multiple)

        return res

    def __sub__(self, other):
        least_common_multiple = self.denominator_b
        # check denominators of fractions and if no define their least common multiple
        if self.denominator_b != other.denominator_b:
            least_common_multiple = self.least_common_multiple(other.denominator_b)

        common_numerator = (least_common_multiple / self.denominator_b * self.numerator_a) - \
                           (least_common_multiple / other.denominator_b * other.numerator_a)
        # if common_numerator % least_common_multiple == 0:
        #     common_numerator = common_numerator / least_common_multiple
        res = Fraction(common_numerator, least_common_multiple)

        return res

    def __mul__(self, other):
        common_numerator = self.numerator_a * other.numerator_a
        common_denominator = self.denominator_b * other.denominator_b
        # if common_numerator % least_common_multiple == 0:
        #     common_numerator = common_numerator / least_common_multiple
        res = Fraction(common_numerator, common_denominator)

        return res





my_fraction = Fraction(6, 9)
other_fraction = Fraction(5, 8)
print(my_fraction)
print(other_fraction)
summ = my_fraction + other_fraction
print('summ:', summ)
subs = my_fraction - other_fraction
print('subs:', subs)
mult = my_fraction * other_fraction
print('mult:', mult)