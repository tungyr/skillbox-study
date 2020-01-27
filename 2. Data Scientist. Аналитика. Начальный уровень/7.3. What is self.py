class Backpack:

    def add(self, item):
        print('Put in backpack ', item)
        self.content = item

my_backpack = Backpack()
# self set automatically
# it's called like this: add(self=my_backpack, item='laptop')
my_backpack.add(item='laptop')

my_son_backpack = Backpack()
# it's called like this: add(self=my_son_backpack, item='book')
my_son_backpack.add(item='book')
print(my_son_backpack.content)

# class and instance methods:
print(Backpack.add)
print(my_son_backpack.add)

# we can call method add() through instance my_backpack, self is set automatically
my_backpack.add(item='phone')
# if we try to call method add() through class same way we'll got exemption about missing 'self': Python don't know
# with which instance method he has to work.
# Backpack.add(item='phone')  # wrong
Backpack.add(self=my_backpack, item='food')
