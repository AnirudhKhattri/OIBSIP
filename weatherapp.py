import requests

api_key = '11eb5f5ec83193c6503f13f163cb14e8'

city = input('Enter city name to check weather: ')

user_input = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(user_input)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    humid = data['main']["humidity"]
    desc = data['weather'][0]['description']
    print(f'Temperature: {temp} K')
    print(f'Humidity: {humid}')
    print(f'Description: {desc}')
else:
    print('Error getting the weather')