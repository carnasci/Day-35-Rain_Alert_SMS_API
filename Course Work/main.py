import requests
from twilio.rest import Client
from credentials import api_key, auth_t, acc_sid

parameters = {
    "lat": 47.606209,
    "lon": -122.332069,
    "units": "imperial",
    "appid": api_key,
    "cnt": 4,
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
print(response.status_code)
data = response.json()
# id = data["list"][0]["weather"][0]["id"]
# for i in range(4):
#     forecast_id = data["list"][i]["weather"][0]["id"]
#     print(forecast_id)
#     if forecast_id < 700:
#         print("Bring an umbrella.")
#After solution
will_rain = False
for hourly_data in data["list"]:
    condition_code = hourly_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True
if will_rain:
    client = Client(acc_sid, auth_t)

    message = client.messages.create(
        from_="+18337841087",
        body="It is going to rain today. Bring an ☂️",
        to="+18777804236"
    )
    print(message.status)