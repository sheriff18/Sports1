import requests
import json

API_TOKEN = 'your_api_token_here'
CITY = 'your_city_here'

# Fetch data from the API
url = f'https://api.waqi.info/feed/{CITY}/?token={API_TOKEN}'
response = requests.get(url)
data = response.json()

# Extract relevant data
if data['status'] == 'ok':
    weather_data = data['data']['iaqi']
    aqi = data['data']['aqi']
else:
    print('Failed to fetch data')
