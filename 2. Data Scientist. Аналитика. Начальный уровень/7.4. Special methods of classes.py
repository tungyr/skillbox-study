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

    def __del__(self):
        self.content = None
        print('Good by, world...')


# when we create instance __init__() called
my_backpack = Backpack(gift='flash-drive')
my_backpack.add(item='laptop')
my_backpack.add(item='charger for laptop')
my_backpack.inspect()

