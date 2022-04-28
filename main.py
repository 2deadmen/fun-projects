##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
import random
import pandas

my_email = "kartikhegde.2002@gmail.com"
password ="7338210933"

connection = smtplib.SMTP("smtp.gmail.com")





PLACEHOLDER = "[NAME]"
# 1. Update the birthdays.csv
letter1 = "letter_templates/letter_1.txt"
letter2 = "letter_templates/letter_2.txt"
letter3 = "letter_templates/letter_3.txt"
letter_list = [letter1, letter2, letter3]
letter = random.choice(letter_list)
# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
month =now.month
day = now.day
with open("birthdays.csv") as file:
    data = pandas.read_csv(file)
    entries = len(data.month)
    for i in range(0,entries):
        if month == data.month[i] and day == data.day[i]:

            with open(letter) as lett:
                contents = lett.read()
                new_letter=contents.replace(PLACEHOLDER,data.name[i])

            to_mail = data.email[i]
            connection = smtplib.SMTP("smtp.gmail.com")
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=to_mail, msg=f"Subject:Happy Birthday\n\n{new_letter}")

            connection.close()

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




