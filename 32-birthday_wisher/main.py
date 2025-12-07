import random
import pandas as pd
import datetime as dt
import smtplib


my_email = "yourEmail"
password = "yourPass"


people_data = pd.read_csv("./birthdays.csv")
people_list = people_data.to_dict(orient="records")

letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt", ]
chosen_letter = random.choice(letters)

now = dt.datetime.now()
month = now.month
day = now.day

for people in people_list:
    if people["month"] == month and people["day"] == day:
        with open(f"./letter_templates/{chosen_letter}", mode="r") as letter_file:
            letter = letter_file.read()
            letter = letter.replace("[NAME]", people['name'])
            letter = letter.replace("Angela", "Hamed")

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=people['email'],
                msg=f"Subject:Happy birthday\n\n{letter}",
            )

        print(f"Email sended to {people['name']}")
