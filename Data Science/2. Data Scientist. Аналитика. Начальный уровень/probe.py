import random

operators = ['+', '-', '*', '/', '//', '%']

for i in range(21):
    print(f'{random.randint(0, 100)} {random.choice(operators)} {random.randint(0, 100)}')