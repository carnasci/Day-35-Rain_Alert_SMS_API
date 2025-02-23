import requests

parameters = {
    "lat": 38.6295,
    "lon": -90.1983,
    "units": "imperial",
    "appid": "e662b0f9a40a2ea650f96201a99ad2a7",

}
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
print(response.status_code)
data = response.json()
print(data)