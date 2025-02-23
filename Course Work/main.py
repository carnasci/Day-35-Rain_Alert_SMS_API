import requests
from credentials import api_key

parameters = {
    "lat": 38.6295,
    "lon": -90.1983,
    "units": "imperial",
    "appid": api_key,
    "cnt": 4,
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
print(response.status_code)
data = response.json()
id = data["list"][0]["weather"][0]["id"]
for i in range(4):
    forecast_id = data["list"][i]["weather"][0]["id"]
    print(forecast_id)
    if forecast_id < 700:
        print("Bring an umbrella.")