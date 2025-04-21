import time

import requests
from datetime import datetime
import smtplib

from sunset.main import current_hour

MY_EMAIL = "vijayaragul2005@gmail.com"
MY_LAT = 20.593683 # Your latitude
MY_LONG = 78.962883 # Your longitude
PASSWORD = "ejjl yerv tzgr yiyj"
body_text = """
Heads up!

Your automated ISS tracker detected that the International Space Station is currently close to your location in Kumbakonam.

Since it is dark, this is a good time to look up towards the sky for a potential sighting!

Happy spotting!

---
Sent by your ISS tracking script.
"""


#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

def is_night():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    if sunrise<hour>sunset:
        return True
    else:
        return False

time_now = datetime.now()
def iss_near_checker():
    response1 = requests.get(url="http://api.open-notify.org/iss-now.json")
    response1.raise_for_status()
    data1 = response1.json()

    iss_latitude = float(data1["iss_position"]["latitude"])
    iss_longitude = float(data1["iss_position"]["longitude"])

    if (MY_LONG-5 >= iss_longitude <=MY_LONG+5) and  (MY_LAT-5 <= iss_latitude <= MY_LAT+5):
        return True
    else:
        return False

hour = time_now.hour

while is_night() and iss_near_checker():

    with smtplib.SMTP("smtp.gmail.com") as connections:
        connections.starttls()
        connections.sendmail(from_addr=MY_EMAIL,to_addrs=MY_EMAIL,msg=f"SUBJECT:ISS NOTIFIER\n\n{body_text}")

    time.sleep(60)





