##################### Extra Hard Starting Project ######################
import pandas as pd, smtplib as sm
import datetime as dt
import random
my_email = "sneder305@gmail.com"
my_passw = "pcbrfxxfrhgjziul"
global email_body
# 1. Update the birthdays.csv
data = pd.read_csv("./birthdays.csv")
# 2. Check if today matches a birthday in the birthdays.csv
dates = {(val.month, val.day): val for (key,val) in data.iterrows()}
dt_today = dt.datetime.now()
today = (dt_today.month,dt_today.day)
if today in dates:
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    to_choose = ["letter_1.txt","letter_2.txt","letter_3.txt"]
    form = random.choice(to_choose)
    with open(file=f"./letter_templates/{form}",mode="r") as data_file:
        bd_name = dates[today]
        body = data_file.read()
        email_body = body.replace("[NAME]",bd_name["name"])
# 4. Send the letter generated in step 3 to that person's email address.
        with sm.SMTP("smtp.gmail.com") as connect:
            connect.starttls()
            connect.login(my_email,my_passw)
            connect.sendmail(
                from_addr=my_email,
                to_addrs=bd_name["email"],
                msg=f"Subject:Happy Birthday\n\n{email_body}"
            )