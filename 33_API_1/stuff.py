import requests
import smtplib

from datetime import datetime as dt
from LSFL_account import LSFL_Account
from time import sleep

LATITUDE = -23.2927
LONGITUDE = -51.1732
GMT_OFFSET = -3

api_parameters = {
    "lat": LATITUDE,
    "lng": LONGITUDE,
    "formatted": 0
}

response_iss = requests.get(url = "http://api.open-notify.org/iss-now.json")
response_iss.raise_for_status()

iss_latitude = float(response_iss.json()["iss_position"]["latitude"])
iss_longitude = float(response_iss.json()["iss_position"]["longitude"])

response_sunset = requests.get(url = "https://api.sunrise-sunset.org/json", params = api_parameters)
response_sunset.raise_for_status()
ds = response_sunset.json()
p_sunrise = int(ds["results"]["sunrise"].split("T")[1].split(":")[0]) + GMT_OFFSET
p_sunset = int(ds["results"]["sunset"].split("T")[1].split(":")[0]) + GMT_OFFSET

now = dt.now()

while True:
    if abs(iss_latitude - LATITUDE) <= 5 and abs(iss_longitude - LONGITUDE) <= 5:
        print("ISS near you soon! Checking whether it's night time...")
        if now.hour > p_sunset or now.hour < p_sunrise:
            print("Looks like it is night time! So we're sending you an email...")
            with smtplib.SMTP(host = "smtp.gmail.com", port = 587) as connection:
                sender = LSFL_Account(r"33_API_1\data.lsfl")
                receiver = LSFL_Account(r"33_API_1\receiver.lsfl")
                connection.starttls()
                connection.login(sender.username, sender.password)
                connection.sendmail(sender.username, receiver.username,
                                    "Subject:Look up at the sky!\n\nThe ISS is flying over your head soon. Look up!")
    else:
        print("ISS is far from you! Sleeping for 60 seconds...")
        sleep(60)                