def func():
    value = input('Input an integer: ')
    try:
        value = int(value)
    except ValueError as err:
        print(f'Error: {err}, with params: {err.args}!')
    finally:
        return value


def another_func():
    my_float = func()
    try:
        my_float = float(my_float)
    except ValueError as val_err:
        print(f'User input is not an integer! {val_err}, {val_err.args}')
    # finally:
    #     my_float = 0
    else:
        print(f'Everythings good! {my_float}')
    return 5 / my_float

try:
    res = another_func()
except(ValueError, ZeroDivisionError) as final_err:
    print(f'Something went wrong, guys! {final_err}, {final_err.args}')
else:
    print(res)