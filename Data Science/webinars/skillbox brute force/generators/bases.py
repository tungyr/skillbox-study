states = {
    # state_key: 0
}
symbols = '0123456789qwertyuiopasdfghjklzxcvbnm'


def get_next_str():
    if state_key not in states:
        states[state_key] = 0

    password_index = states[state_key]
    password = ''

    index = password_index
    while index > 0:
        rest = index % len(symbols)
        index = index // len(symbols)

        password += symbols[rest]

    states[state_key] += 1
    return password


if __name__ == '__main__':
    for step in range(10):
        print(get_next_str('1'))
        print(get_next_str('2'))