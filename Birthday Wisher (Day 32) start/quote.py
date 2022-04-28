import smtplib
import datetime
import random
my_email = "kartikhegde.2002@gmail.com"
password ="7338210933"

with open("quotes.txt","r") as file:
    data = file.readlines()
    msg = data[random.randint(0,100)]
now = datetime.datetime.now()
day = now.weekday()
if day == 3:




        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs="kartikhegde.1996@gmail.com",msg=f"Subject:quote,{msg}")

        connection.close()
