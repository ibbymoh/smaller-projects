import requests
from twilio.rest import Client

api_key = "160c0e576939fb08472e7b1c08d7f2e3"
LAT = "30.003536"
LON = "31.320012"
account_sid = "AC7e0f277ef5f6bc3e469f5f71dae08851"
auth_token = "8e3937514ff733ceffd2f4d72db71a96"

will_rain = False
response = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?lat={LAT}&lon={LON}&appid={api_key}")

response.raise_for_status()
data = response.json()
weather = data["list"]
next_twelve_hours_weather = [weather[i]["weather"][0]["main"] for i in range(10)]
next_twelve_hours_weather.append("Rain")


if "Rain" in next_twelve_hours_weather:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body='It will rain in the next 12 hours,bring an umbrella',
        from_='+16812022991',
        to='+201097834536'
    )

    print(message.status)
