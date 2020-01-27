# ----------------------------------------------------------------------------------------------------------

# Skillbox, 7.2. Attributes and methods of objects
# https://go.skillbox.ru/course/data-scientist-1/c8fab48a-d06d-4ca2-91c5-bbaffa311d91

# TODO: watch lesson one more time - part about getattr, hasattr, etc.

class Robot:

    def __init__(self):
        self.name = 'R2D2'

    def hello(self):
        print(f'Hello world! My name is {self.name}')

    def go(self, x, y):
        print(f'I\'m on my way to position with coordinates {x} and {y}')


robot = Robot()

print(robot.hello())

# robot.temperature = 1
#
# while robot.temperature < 10:
#     robot.temperature *= 2
# print(robot.temperature)
# del robot.temperature
#
# attr_name = 'model'
# if hasattr(robot, attr_name):
#     print('hasattr: ', robot.model)
# else:
#     setattr(robot, attr_name, 'android')
# print('setattr: ', robot.model)
#
# print('getattr: ', getattr(robot, attr_name))
#
# delattr(robot, attr_name)
#
#
# for attr_name in ('weight', 'height'):
#     setattr(robot, attr_name, 42)
# print(robot.weight)
# print(robot.height)

print(robot.go(x=5, y=7))

