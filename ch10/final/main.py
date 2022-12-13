import datetime as dt
import requests 
import json

class weather():
  def __init__(self):

    latitude = input("What is your latitude?")
    longitude = input("What is your longitude?")
    lat = latitude
    lon = longitude
    url = "https://api.openweathermap.org/data/2.5/weather?lat=" + lat + "&lon=" + lon + "&appid=cf7c118584b22e1db567ce037a9b4bb6"
    result = requests.get(url).json()
    print(result)
weather()