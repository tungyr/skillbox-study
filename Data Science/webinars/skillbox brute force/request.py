import requests
for i in range(1):
    r = requests.get('https://www.google.ru/')
    print(r.text)
