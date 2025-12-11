
import requests

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "Your_KEY"

my_latitude = 38.252529
my_longitude = 48.301529

parameters = {
    "lat": my_latitude,
    "lon": my_longitude,
    "appid": API_KEY,
    "cnt": 4,
}

res = requests.get(url=OWM_ENDPOINT, params=parameters)
res.raise_for_status()

weather_data = res.json()

will_rain = False

for hour_data in weather_data['list']:
    condition_code = print(hour_data['weather'][0]['id'])
    if condition_code != None:
        if int(condition_code) < 700:
            will_rain = True


if will_rain:
    print("Bring an umbrella.")
