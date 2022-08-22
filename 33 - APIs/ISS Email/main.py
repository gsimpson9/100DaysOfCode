import requests
from datetime import datetime
import smtplib
from email.message import EmailMessage
import time

MY_EMAIL = "ENTER THE EMAIL ADDRESS TO SEND"
MY_OTHER_EMAIL = "ENTER THE EMAIL ADDRESS TO RECEIVE"
MY_PASSWORD = "PASSWORD FOR THE EMAIL THAT SENDS"

# ENTER YOUR LAT AND LONG HERE
MY_LAT = 0
MY_LONG = 0

response = requests.get(url='http://api.open-notify.org/iss-now.json')
response.raise_for_status()
longitude = float(response.json()['iss_position']['longitude'])
latitude = float(response.json()['iss_position']['latitude'])
iss_position = (latitude, longitude)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
time_now = datetime.now().hour


def is_iss_overhead():
    """function to check if your position is within +5 or -5 of the iss position"""
    if MY_LAT - 5 <= longitude <= MY_LAT + 5:
        if MY_LONG - 5 <= latitude <= MY_LONG + 5:
            return True


def is_night():
    """function to check if it's night"""
    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        msg = EmailMessage()
        msg.set_content('The ISS is currently flying overhead')
        msg['Subject'] = 'Look up☝️'
        msg['From'] = MY_EMAIL
        msg['To'] = MY_OTHER_EMAIL
        with smtplib.SMTP("ENTER YOUR SMTP DETAILS HERE") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.send_message(msg)
