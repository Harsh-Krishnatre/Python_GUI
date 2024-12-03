import requests
from datetime import datetime
import smtplib,time

MY_LAT = 20.593683
MY_LNG = 78.962883
my_email = "sneder305@gmail.com"
my_passw = "pcbrfxxfrhgjziul"
def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LNG-5 <= iss_longitude <= MY_LNG+5 and MY_LAT-5 <= iss_latitude <= MY_LAT+5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()
    hour_now = time_now.hour
    if sunset < hour_now < sunrise:
        return True
    else:
        return False
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    if iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connect:
            connect.starttls()
            connect.login(user=my_email,password=my_passw)
            connect.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg="Subject:Time to watch ISS\n\nHey\nThe ISS is right above your head in sky and its night. So, go watch it."
            )
    time.sleep(60)
