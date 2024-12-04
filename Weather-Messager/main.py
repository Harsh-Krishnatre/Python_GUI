import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ['https_proxy']}

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = "AC8c2bf1ef7b652eb844a68d536e478f32"
auth_token = os.environ["OWM_AUTH_TOKEN"]
api_key = os.environ["OWM_API_KEY"]

parameters = {
    "appid" : api_key,
    "lat" : 28.704060,
    "lon" : 77.102493,
    "cnt" : 4,
    "units" : "metric"
}

client = Client(account_sid, auth_token,http_client=proxy_client)
res = requests.get(url=OWM_Endpoint,params=parameters)
res.raise_for_status()
msg = None
data = res.json()

to_bring = False
for i in range(len(data["list"])):
    if data["list"][i]["weather"][0]["id"] < 700:
        to_bring = True
if to_bring:
    msg = "It is advisable to bring an umbrella."
else:
    msg = "You can go without an umbrella."

message = client.messages\
    .create(
    body=msg,
    from_="+17755490861",
    to="#######"
)

print(message.status)
