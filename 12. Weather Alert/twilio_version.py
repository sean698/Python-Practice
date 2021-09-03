import requests
from twilio.rest import Client

# If it is going to rain in the next 12 hours, send an SMS

CITY_ID = 1813451
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "c5811c44b6b0dfa9598a4898a97f91df"
MY_LAT = 40.071766
MY_LNG = 113.316421
account_sid = 'AC8aba41cd2344beadecc46c1b1f123b4c'
auth_token = '2f2eac956c100e85be9956d1a5771469'
my_phone = '+8613834257554'

# We want hourly forecast in the next 12 hours from 7am everyday
weather_params = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

res = requests.get(OWM_ENDPOINT, params=weather_params)
weather_data = res.json()
# Python slice feature
weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    weather_id = hour_data["weather"][0]["id"]
    if weather_id < 700:
        will_rain = True
    else:
        will_rain = False

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
                .create(
                     body="It's going to rain today. Remember to bring an ☂.",
                     from_='+14078908771',
                     to=my_phone
                 )
    print(message.status)

