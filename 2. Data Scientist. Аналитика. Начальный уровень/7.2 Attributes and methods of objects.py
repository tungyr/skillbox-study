# ----------------------------------------------------------------------------------------------------------

# Skillbox, 7.2. Attributes and methods of objects
# https://go.skillbox.ru/course/data-scientist-1/c8fab48a-d06d-4ca2-91c5-bbaffa311d91

# TODO: watch lesson one more time - part about getattr, hasattr, etc.

class Robot:

    def __init__(self):
        self.name = 'R2D2'

    def hello(self):
        print(f'Hello world! My name is {self.name}')


robot = Robot()

print(robot.hello())

robot.temperature = 1

while robot.temperature < 10:
    robot.temperature *= 2
print(robot.temperature)
del robot.temperature

