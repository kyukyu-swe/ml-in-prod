import requests

api_key = '5d805c06af2326dc72ec9c3921d9439a'
#Mandalay
lat = 21.9588
lon = 96.0891

#Yangon
lat = 16.48
lon = 96.09

url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
response = requests.get(url)
print(f"HTTP response status code = {response.status_code}")
weather_data = response.json()

temp = weather_data['main']['temp']
temp_C = temp - 273.15
temp_F = (temp - 273.15) * 9/5 + 32

city = weather_data['name']

weather = weather_data['weather'][0]['main']

#print(weather_data)

print(f" The weather in current city {city} is {weather}, and the temperature is {temp_C:.2f}°C ({temp_F:.2f}°F).")
# print(f"Current Temp = {temp}K")
# print(f"City = {city}")
# print(f"Weather = {weather}")