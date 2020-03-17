# equity

class Backpack():

    def __init__(self, gift=None):
        self.content = []
        if gift:
            self.content.append(gift)

    def __str__(self):
        return 'Backpack: ' + ', '.join(self.content)

    def __eq__(self, other):
        return self.content == other.content

    def __add__(self, other):
        new_obj = Backpack()
        new_obj.content.extend(self.content)
        # check whether it is comparing two instances of Backpack and if not accept other source of data:
        if isinstance(other, Backpack):
            new_obj.content.extend(other.content)
        else:
            new_obj.content.extend(other)
        return new_obj


my_backpack = Backpack(gift='sandwich')
son_backpack = Backpack(gift='banana')

# if my_backpack == son_backpack:
#     print('We are resemble')
# else:
#     print('We have different backpack content')
#
# # or same as above:
# if Backpack.__eq__(self=my_backpack, other=son_backpack):
#     print('(Method) We are resemble')
# else:
#     print('(Method) We have different backpack content')

# __add__:

# new_backpack = my_backpack + son_backpack
# print('__add__: ', new_backpack)
# another_backpack = my_backpack + ['apple', 'grape']
# print('another_backpack: ', another_backpack)

# ----------------------------------------------------------------------------------------------------------
# creation new class instances using add (another example of __add__ usage):


class Bread:

    # it changes object name in terminal from "<__main__.Sausage object at 0x02F2D328>" to "I'm sausage"
    def __str__(self):
        return "I'm bread"

    def __add__(self, other):
        return Sandwich(part1=self, part2=other)


class Sausage:

    def __str__(self):
        return "I'm sausage"

    def __add__(self, other):
        return Sandwich(part1=self, part2=other)


class Sandwich:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return "I'm sandwich. I'm made from " + str(self.part1) + " and " + str(self.part2)


# borodinsky = Bread()
# salami = Sausage()
# result = borodinsky + salami
# print(result)
# print('salami: ', salami)

# ----------------------------------------------------------------------------------------------------------
# __call__: emulation of function call


def func(*args, **kwargs):
    print(args, kwargs)


print(func)
func(a=1, b=2)


class MyFunction:

    # it's enables us to automatically run code in __call__ after call of class instance with 'func_class(a=3, b=4)'
    def __call__(self, *args, **kwargs):
        print('This is __call__ output:', args, kwargs)


# func_class = MyFunction()
# print('func_class: ', func_class)
# func_class(a=3, b=4)

# ----------------------------------------------------------------------------------------------------------
# multiplication of integers by func

class Multiplier:

    def __init__(self, factor=2):
        self.factor = factor

    def __call__(self, *args):
        res = []
        for item in args:
            res.append(item * self.factor)
        return res


mul_by_27 = Multiplier(factor=27)
mul_by_34 = Multiplier(factor=34)
# result = mul_by_27(1, 2, 3, 4)
result = mul_by_34(1, 2, 3, 4)
print(result)

# creation list of objects(functions) which calculates with diff. factors
multipliers = []
for factor in (2, 3, 4, 5):
    mul = Multiplier(factor=factor)
    multipliers.append(mul)
print(multipliers)

# call every object(function) in multipliers list to calculate multiply
for mul in multipliers:
    print(mul(10, 20, 30))