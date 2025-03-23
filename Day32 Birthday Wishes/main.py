# import smtplib
#
# my_email = "rodgerdoger003@gmail.com"
# password = "qyovfibexhjqoris"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="rodgersotieno@myyahoo.com",
#                         msg="Subject:Hello\n\nThis is the body of my email")

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
if year == 2025:
    print("bring me my money")
    print(month)
    print(day_of_week)
print(year)

date_of_birth = dt.datetime(year=1999, month=3, day=31, hour=4)
print(date_of_birth)
