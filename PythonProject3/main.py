import requests

API_KEY = "API key"
city = input("Введите название города")
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
response = requests.get(url)

if response.status_code == 200:
        data = response.json()
        print(f"Current temperature in {city}: {data['main']['temp']}°C")
        print(f"Weather description: {data['weather'][0]['description']}")
else:
        print(f"Error: {response.status_code} - {response.json()['message']}")