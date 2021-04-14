# Get weather detail of current location
import requests

res = requests.get('https://ipinfo.io/')
data = res.json()

location = data['loc'].split(',')
latitude = location[0]
longitude = location[1]

url = "http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=34ed74cca4569e3edc01e507e77ae629&units=metric".format(latitude, longitude)

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
