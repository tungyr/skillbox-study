from random import choice, randint

# class Lemming:
#     names = ['Peter', 'Anna', 'Nik', 'Maria', 'Donn', 'Lora', 'Victor', 'Bred', ]
#     tail_length = 20
#
#     def __init__(self):
#         self.tail_length = randint(15, 25)
#         self.name = choice(Lemming.names)
#
#     def __str__(self):
#         return 'Lemming ' + self.name + ' with tail length ' + str(self.tail_length)
#
#
# # check class attribute tail_length
# print('class attribute tail_length: ', Lemming.tail_length)
#
# new_lemming = Lemming()
# # when call attribute "tail_length" through instance, firstly Python look for such attribute in instance, and if don't
# # find it there go further and look for attribute "tail_length" in class. If instance has its own attribute
# # "tail_length" this instance attribute overlays class attribute.
# print('instance attribute tail_length: ', new_lemming.tail_length)
# print(new_lemming)

# ----------------------------------------------------------------------------------------------------------

# # wrong calculation of lemmings quantity:
#
# class Lemming:
#     names = ['Peter', 'Anna', 'Nik', 'Maria', 'Donn', 'Lora', 'Victor', 'Bred', ]
#     total = 0
#     tail_length = 20
#
#     def __init__(self):
#         self.tail_length = randint(15, 25)
#         self.name = choice(Lemming.names)
#         # wrong sentence, we trying to count lemmings quantity inside of lemming instance and got self.total = 0,
#         # and we don't even get 1, because Lemming instance has no its own "total" attribute and Python takes class
#         # attribute "total", which is 0:
#         self.total = self.total + 1
#         # correct:
#         # Lemming.total = Lemming.total + 1
#
#     def __str__(self):
#         return 'Lemming ' + self.name + ' with tail length ' + str(self.tail_length)
#
#
# burrow = []
# burrow_depth = randint(90, 100)
# while len(burrow) < burrow_depth:
#     family = []
#     family_size = randint(16, 32)
#     while len(family) < family_size:
#         new_lemming = Lemming()
#         family.append(new_lemming)
#     burrow.append(family)
# print('Lemmings total: ', Lemming.total)

# ----------------------------------------------------------------------------------------------------------
# variables with identical name in different namespaces


class SomeClass:
    x = 67

    def __init__(self):
        # avoid overlay global variables by local like here
        self.x = 78

    def method_one(self):
        x = 23
        print('method_one', x)

    def method_two(self):
        x = 34
        def func_one():
            x = 56
            print('func_one', x)
        func_one()
        print('method_two', x)


x = 12
obj = SomeClass()
print('SomeClass x', SomeClass.x)
print('obj x', obj.x)
obj.method_one()
obj.method_two()
print('global', x)
