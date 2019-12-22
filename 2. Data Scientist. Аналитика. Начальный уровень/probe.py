# user_input = input('Enter your name: ')
# print(type(user_input))
# print(user_input)

# x, y map(int, input().split())
# print(type(x))
# print(x, y)

# car = '345'
# print(car.isnumeric())

# S = 's\np\ta\nbbb'
# S = r'C:\temp\new'
# S = r'C:\semp\rew'
# S = b'byte'
#
# print(S)

# my_list = [1, 2, 3, 'apple', ['a', 'b', 'c']]
# print(my_list)

# else, break and continue - все вместе
# f1, f2, count = 0, 1, 0
# while f2 < 10000:
#     count += 1
#     if count > 27:
#         print('Итераций больше чем 27. Прерываюсь.')
#         break
#     f1, f2 = f2, f1 + f2
#     if f2 < 1000:
#         continue
#     print(f2)
# else:
#     print('Было', count, 'итераций')

i, summ = 1, 0
while i < 10:
    if i % 2 == 0:
        summ = summ + i
    i += 1
    if summ > 500:
        print('summ > 500!')
        break
    if i < 900:
        continue
    print(i)
else:
    print('finito!')

