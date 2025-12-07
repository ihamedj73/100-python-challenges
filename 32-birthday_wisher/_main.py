import smtplib
import datetime as dt
import random


my_email = "YourEmail"
password = "yourPass"
recipient = "email"

if dt.datetime.now().weekday() == 6:
    with open("./quotes.txt") as file:
        quotes = file.readlines()

    message = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipient,
            msg=f"Subject:Monday Motivation\n\n{message}")
