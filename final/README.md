import tkinter as tk

from tkinter import simpledialog
root = tk.Tk()
root.withdraw()

city = simpledialog.askstring(title="What City's Weather Intrigues You?", prompt="City:")

import requests

api_key = '8c1ca6bb55cb5247172a4162368b07eb'

data = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={api_key}')

if data.json()['cod'] == '404':
    print("Your City's not cool enough to be in this database.")
else:
    description = data.json()['weather'][0]['description']
    temperature = round(data.json()['main']['temp'])
    feels_like = round(data.json()['main']['feels_like'])
    high = round(data.json()['main']['temp_max'])
    low = round(data.json()['main']['temp_min'])

    print(f"The weather in {city[0].upper()}{city[1:]} is {temperature}° F with {description}.")
    print(f"It feels like {feels_like}° F.")
    print(f"Today's high is {high}° F and today's low is {low}° F.")
