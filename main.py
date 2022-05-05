import smtplib
import requests
from datetime import datetime
import time
my_email="kartikhegde.2002@gmail.com"
password =" your password"
MY_LAT =14.776682 # Your latitude
MY_LONG = 74.738446 # Your longitude
while True:
        time.sleep(60)
        response = requests.get(url="http://api.open-notify.org/iss-now.json")
        response.raise_for_status()
        data = response.json()

        iss_latitude = float(data["iss_position"]["latitude"])
        iss_longitude = float(data["iss_position"]["longitude"])

        #Your position is within +5 or -5 degrees of the ISS position.


        parameters = {
            "lat": MY_LAT,
            "lng": MY_LONG,
            "formatted": 0,
        }

        response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
        response.raise_for_status()
        data = response.json()
        sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
        sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

        time_now = datetime.now()

        #If the ISS is close to my current position
        now =time_now.hour


        if now < sunset and now > sunrise:

           if (MY_LAT > iss_latitude - 5) and MY_LAT > iss_latitude - 5  and (MY_LONG > iss_longitude -5 and  MY_LONG > iss_longitude +5):
             connection=smtplib.SMTP("smtp.gmail.com")
             connection.starttls()
             connection.login(user=my_email,password=password)
             connection.sendmail(from_addr=my_email,to_addrs="kartikhegde.2002@gmail.com",msg="Subject:look up!!!\n\nlook up in the sky now to spot the International space station")
             connection.close()

# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



