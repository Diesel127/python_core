import requests

API_KEY = "API key"
address = "Zitna 42 Prague"
url = f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={API_KEY}'
response = requests.get(url)
data = response.json()
if data['status'] == 'OK':
    location = data['results'][0]['geometry']['location']
    latitude = location['lat']
    londitute = location['lng']
    print(f"Coordinates for '{address}': Latitude = {latitude}, Longitude = {longitude}")
else:
        print(f"Error: {data['status']}")