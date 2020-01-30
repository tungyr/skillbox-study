import random

# class Lemming:
#     pass
#
# total_lemmings = 0
# lemming_1 = Lemming()
# total_lemmings += 1
# lemming_2 = Lemming()
# total_lemmings += 1
# Lemming_3 = Lemming()
# total_lemmings += 1
#
# family = []
# family_size = random.randint(16, 32)
# while len(family) < family_size:
#     new_lemming = Lemming()
#     family.append(new_lemming)
#     total_lemmings += 1
#
# # print(total_lemmings)

# ----------------------------------------------------------------------------------------------------------

# better solution, than above:

# class Lemming:
#
#     # class level attribute, which keeps lemming quantity
#     total = 0
#
#     def __init__(self):
#         # every new instance creation add 1 to class attribute Lemming.total
#         Lemming.total += 1
#
#
# burrow = []
# burrow_depth = random.randint(90, 100)
# while len(burrow) < burrow_depth:
#     family = []
#     family_size = random.randint(16, 32)
#     while len(family) < family_size:
#         new_lemming = Lemming()
#         family.append(new_lemming)
#     burrow.append(family)
# print(Lemming.total)
# print(burrow)

# ----------------------------------------------------------------------------------------------------------

# another example:


class Pupil:
    total, names = 0, ['Peter', 'Anna', 'Nik', 'Maria', 'Donn', 'Lora', 'Victor', 'Bred', ]
    names_count = len(names)
    some_text = 'Do not go gentle into that good night '
    some_var = some_text + names[-2]

    def __init__(self):
        Pupil.total += 1
        self.name = random.choice(Pupil.names)

    def __str__(self):
        return 'Pupil ' + self.name

    def check_class_attr(self):
        print('Pupil.total', Pupil.total)
        print('Pupil.names', Pupil.names)
        print('Pupil.names_count', Pupil.names_count)
        print('Pupil.some_text', Pupil.some_text)
        print('Pupil.some_var', Pupil.some_var)


new_pupil = Pupil()
print('Pupil.total', Pupil.total)
print('Pupil.names', Pupil.names)
print('Pupil.names_count', Pupil.names_count)
print('Pupil.some_text', Pupil.some_text)
print('Pupil.some_var', Pupil.some_var)
# calling class attributes through the instance
# new_pupil.check_class_attr()

