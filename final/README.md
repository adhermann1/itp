Weather: A Python Program Documentation

**What I Did**

I made a web-based weather program that uses a Graphical User Interface in order to receive a city to tell the person what the weather there is.

**How I Did It**

I first started looking up how to make a web-based weather program, and I found a lot of different sources that all had a very similar method, using the Weather API from OpenWeatherMap. I looked at a few different versions of programs that ultimately did everything the same, looking to write it how I thought best, and I got this:

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

From there on, I began researching GUI's in order to create my user input. I once again took to the internet to soothe my programming woes. I found an article (https://thenewstack.io/python-for-beginners-how-to-build-a-gui-application/) that gave me some basic code to use as a template for my GUI portion of my code:

import tkinter as tk

from tkinter import simpledialog
root = tk.Tk()
root.withdraw()

city = simpledialog.askstring(title="What City's Weather Intrigues You?", prompt="City:")

It took me literal hours to figure out what was wrong with tkinter at first, until I finally updated pip and tkinter and then realized my python language support wasn't updated😭😭😭.

Finally, I simply attached the two different programs to get my final program (found in 'weatherapp.py').
