# def greeting(person_name):
#     if person_name == "Don":
#         raise BaseException('It\'s not a place for Don!')
#     print(f'Hello {person_name}')
#
#
# greeting('Don')


# try:
#     raise NameError('This is error')
# except NameError as exc:
#     print(f'Exception of type {type(exc)} passed by. Its parameters are {exc.args}')
#     raise TypeError('TypeError here')

# class HeroDiedError(Exception):
#     pass
#
# class GameOverError(Exception):
#     pass
#
# try:
#     raise HeroDiedError('Private Sandler')
# except HeroDiedError as exc:
#     print(f'An exception has caught {exc}')
#     raise GameOverError('Mission failed!')

class DivisionError(Exception):

    def __init__(self, message, input_data=None):
        self.message = message
        self.input_data = input_data

    def __str__(self):
        return self.message

def division(a, b):
    if a < b:
        raise DivisionError('Нельзя делить меньшее на большее', input_data=dict(a=a, b=b))
    return a/b


try:
    division(1, 2)
except DivisionError as exc:
    print(f'Поймано моё исключение {exc}, входные данные при ошибке {exc.input_data}')