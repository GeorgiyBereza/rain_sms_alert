import requests
import os
from twilio.rest import Client

from_number = "initial number"
to_number = "the receiver's number"
api_key = os.environ.get("OPEN_WEATHER_MAP_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
MY_LATITUDE = 41.715137
MY_LONGITUDE = 44.827095

url = f"https://api.openweathermap.org/data/2.5/forecast?lat={MY_LATITUDE}&lon={MY_LONGITUDE}&appid={api_key}&cnt=4"
print(url)
response = requests.get(url=url)
response.raise_for_status()
print(response.status_code)
data = response.json()

will_rain = False
for n in range(4):
    if data['list'][n]['weather'][0]['id'] < 700:
        will_rain = True

def send_sms():
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain! Don't forget an umbrella",
        from_=from_number,
        to=to_number
    )
    print(message.status)

if will_rain:
    send_sms()

