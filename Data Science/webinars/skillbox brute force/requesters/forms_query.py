import requests


def request(login, password):
    r = request.post('http://127.0.0.1:6000/auth', data={'login': login, 'password': password})
    return r.status_code == 200