import smtplib
import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()
MY_EMAIL = "rodgerdoger003@gmail.com"
PASSWORD = "qyovfibexhjqoris"

if weekday == 6:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

        print(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="rodgersotieno@myyahoo.com",
                            msg=f"Subject:Today's motivation\n\n{quote}")


