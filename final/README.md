Final

import requests

api_key = '8c1ca6bb55cb5247172a4162368b07eb'

city = input("What City's weather intrigues you?: ")

data = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={api_key}')
