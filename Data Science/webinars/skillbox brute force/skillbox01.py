import requests
for i in range(10):
    r = requests.get('https://www.google.ru/')
    print(r.text)
