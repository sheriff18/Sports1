import requests

import json

API_TOKEN = '94db1f42579e34a3c357d1440494421224d080f0'
CITY = 'accra'

# Fetch data from the API
url = f'https://api.waqi.info/feed/{CITY}/?token={API_TOKEN}'
response = requests.get(url)
data = response.json()

print(data)

# Extract relevant data
if data['status'] == 'ok':
    weather_data = data['data']['iaqi']
    aqi = data['data']['aqi']
else:
    print('Failed to fetch data')
