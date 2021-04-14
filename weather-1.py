import requests
from pprint import pprint

city = input("Enter your city: ")

url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=34ed74cca4569e3edc01e507e77ae629&units=metric".format(city)

res = requests.get(url)

data = res.json()

#pprint(data)

temp = data['main']['temp']
wind_speed = data['wind']['speed']

latitude = data['coord']['lat']
longitude = data['coord']['lon']

description = data['weather'][0]['description']

print('Temperature: {} degree celcius'.format(temp))
print('Wind speed: {}'.format(wind_speed))
print('Latitude: {}'.format(latitude))
print('longitude: {}'.format(longitude))
print("Description: {}".format(description))
