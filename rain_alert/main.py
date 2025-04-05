import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv("weather.env")
parameters = {
    "lat": 47.038902,
    "lon": -87.906471,
    "appid": os.getenv("weather_api_key"),
    "cnt": 4
}

condition_codes = []
will_rain = False
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast?", params=parameters)
response.raise_for_status()
data = response.json()
for weather in data["list"]:
    condition_code = weather["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella.",
        from_="whatsapp:+14155238886",
        to="whatsapp:+14147797306",
    )

    print(message.body)
    print(message.status)
