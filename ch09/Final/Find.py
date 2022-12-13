import requests
import json
class City():
  def __init__(self):
    City = input("What city would you like?")
    '''
    This takes your desired city and gives the name of the city in other languages and as well provides coordinates
    '''
    url = "http://api.openweathermap.org/geo/1.0/direct?q=" + City + "&limit=&appid=cf7c118584b22e1db567ce037a9b4bb6"
    result = requests.get(url).json()
    #return(response['main']['lon'])
    #print(longitude)
    
    print(result)