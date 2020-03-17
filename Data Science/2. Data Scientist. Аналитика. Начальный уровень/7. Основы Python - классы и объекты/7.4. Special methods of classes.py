class Backpack():

    def __init__(self, gift=None):
        self.content = []
        if gift is not None:
            self.content.append(gift)

    def add(self, item):
        """Put something to backpack"""
        self.content.append(item)
        print('Put to backpack: ', item)

    def inspect(self):
        """Check what's inside"""
        print('In backpack is: ')
        for item in self.content:
            print('    ', item)

    # delete instance by garbage collector if no links to instance
    # def __del__(self):
    #     self.content = None
    #     print('Good by, world...')

    # redefining for print function
    def __str__(self):
        return 'Backpack: ' + ', '.join(self.content)

    def __bool__(self):
        return self.content != []

    def __len__(self):
        return len(self.content)


# # when we create instance __init__() called
# my_backpack = Backpack(gift='flash-drive')
# my_backpack.add(item='laptop')
# my_backpack.add(item='charger for laptop')
# my_backpack.inspect()
# print(my_backpack)
# # or same explicitly:
# print(my_backpack.__str__())
# print('__bool__: ', my_backpack.__bool__(), '\n', '__len__: ', my_backpack.__len__())
#
# # True/False depending on my_backpack.__bool__() method and quantity of items len depending on my_backpack.__len__()
# # if __bool__ is not redefined in class, Python consider "if my_backpack:" as True by default
# if my_backpack:
#     print('Backpack is not empty!')
#     print('It holds', len(my_backpack), 'things.')
# else:
#     print('Backpack is empty!')

