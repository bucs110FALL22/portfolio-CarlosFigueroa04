import datetime as dt
import requests 
import json

class weather():
  def __init__(self):
    '''
    This method is used to find the city in witch you want to know about the weather
    '''
    latitude = input("What is your latitude?")
    longitude = input("What is your longitude?")
    lat = latitude
    lon = longitude
    url = "https://api.openweathermap.org/data/2.5/weather?lat=" + lat + "&lon=" + lon + "&appid=cf7c118584b22e1db567ce037a9b4bb6"
    result = requests.get(url).json()

    #kelvin = result['weather']['temp']
    #temp_celsius, temp_fahrenheit = kelvin_convert(kelvin)
    print(result)
  def kelvin_convert(kelvin):
    celsius = kelvin - 273
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit
    '''
    This was meant to take the given 'temp' from the list and convert it from kelvin to other units of temperature
    '''
  
weather()