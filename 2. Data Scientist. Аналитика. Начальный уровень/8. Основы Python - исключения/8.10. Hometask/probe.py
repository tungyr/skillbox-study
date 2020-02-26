class RegistrationError(Exception):

    def __init__(self, error_type, message, input_data):
        self.error_type = error_type
        self.message = message
        self.input_data = input_data

    def value_error(self, input_data):
        self.error_type = 'ValueError: '
        self.message = 'Not all 3 fields in '
        self.input_data = input_data
        return self.error_type + self.message + input_data


def validate(registration):

    registration = registration.split()
    print(registration)
    if len(registration) < 3:
        raise ValueError(f'Only {len(registration)} fields in [{line}]')
    if registration[0].isalpha() is False:
        raise ValueError(f'Only letters should be in [{registration[0]}]')
    if '.' and '@' not in registration[1]:
        raise ValueError(f'"." and "@" should be in [{registration[1]}]')
    if int(registration[2]) not in range(10, 100):
        raise ValueError(f'{registration[2]} is not valid age')



with open('registrations_.txt', 'r') as ff:
    for line in ff:
        # line = line[:-1]
        try:
            validate(line)
        finally:
            pass