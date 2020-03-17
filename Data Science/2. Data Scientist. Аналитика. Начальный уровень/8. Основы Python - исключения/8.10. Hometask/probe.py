class NotNameError(Exception):
    """Name exception class with possibility of setting user error message"""
    message = 'name is invalid!'

    def __init__(self, value, message=message):
        self.value = value
        self.message = message

    def __str__(self):
        return f'Name error: "{self.value}" {self.message}'


class NotEmailError(Exception):
    """E-mail exception class with possibility of setting user error message"""
    message = 'address is invalid!'

    def __init__(self, value, message=message):
        self.value = value
        self.message = message

    def __str__(self):
        return f'E-mail error: "{self.value}" {self.message}'


def validate(registration):
    """Validate registration data"""

    registration = registration.split()
    if len(registration) < 3:
        raise ValueError(f'Only {len(registration)} field(s) present!')

    elif registration[0].isalpha() is False:
        raise NotNameError(registration[0])

    elif '.' and '@' not in registration[1]:
        raise NotEmailError(registration[1])

    try:
        if int(registration[2]) not in range(10, 100):
            raise ValueError(f'"{registration[2]}" is not valid age!')
    finally:
        pass


def read_file():
    """Read file with registration data and catch exceptions"""
    registration_good = []
    registration_bad = []
    with open('registrations_.txt', 'r') as ff:
        for line in ff:
            line = line.rstrip('\n')
            try:
                validate(line)
            except BaseException as exc:
                # exc already consist of error type so BaseException used
                registration_bad.append(line + f' - {str(exc)}\n')
                continue
            else:
                registration_good.append(line + '\n')
        write_file(registration_good, registration_bad)


def write_file(registration_good, registration_bad):
    """Write files with good and bad registration data"""
    with open('registration_good.txt', 'w') as ff:
        for registration in registration_good:
            ff.write(registration)

    with open('registration_bad.txt', 'w') as ff:
        for registration in registration_bad:
            ff.write(registration)


read_file()