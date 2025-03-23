import datetime as dt
import smtplib
import pandas
import random

my_email = "rodgerdoger003@gmail.com"
password = "qyovfibexhjqoris"
now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 6:
    with open("quotes.txt", mode="r") as data_file:
        data = pandas.DataFrame(data_file)
        all_quotes = data.to_dict(orient="records")
        today_quote = random.choice(all_quotes)
        print(today_quote[0])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="rodgersotieno@myyahoo.com",
                            msg=f"Subject:Today's Motivation\n\n {today_quote[0]}")

