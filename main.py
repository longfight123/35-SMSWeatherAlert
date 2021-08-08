import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv('.env')
API_KEY = os.getenv("API_KEY") # from the OWM account
account_sid = os.getenv("account_sid") # from our twilio dashboard
auth_token = os.getenv("auth_token") # from our twilio dashboard
MY_LONG = os.getenv("MY_LONG")
MY_LAT = os.getenv("MY_LAT")

MY_PARAMETERS = {
    'lat': MY_LAT,
    'lon': MY_LONG,
    'appid': API_KEY,
    'exclude':'current,minutely,daily,alerts'
}

response = requests.get(url='https://api.openweathermap.org/data/2.5/onecall', params=MY_PARAMETERS)
response.raise_for_status()
hourly_data = response.json()['hourly']

will_rain = False

for hour in hourly_data[0:12]:
    weather_id = hour['weather'][0]['id']
    if weather_id < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today, remember to bring an Umbrella ☂️.",
        from_='+12158678688', #from our twilio dashboard
        to='+14036693979'
    )
    print(message.status)