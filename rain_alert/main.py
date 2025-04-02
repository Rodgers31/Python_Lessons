import requests
api_key = "f88b9e7b8dfb56ea4ac4eca0c08c06a3"

parameters = {
    "lat": 43.038902,
    "lon": -87.906471,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast?", params=parameters)
response.raise_for_status()
data = response.json()
for weather in data["list"]:
    for weather_id in weather["weather"]:
        if int(weather_id["id"]) < 700:
            print("Bring an umbrella")


