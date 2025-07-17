from bs4 import BeautifulSoup
import requests
from smtplib import SMTP
LINK = 'https://appbrewery.github.io/instant_pot/'
response = requests.get(LINK)
price = response.text
MY_EMAIL = "rodgerdoger003@gmail.com"
PASSWORD = "qyovfibexhjqoris"

soup = BeautifulSoup(price, 'html.parser')

item_price = soup.find("span", {"class": 'a-offscreen'}).get_text()
title = soup.find("span", {"id": "productTitle"}).get_text().strip()
remove_dollar = item_price.split("$")[1]
total_price = float(remove_dollar)

title = title.replace(" ", '')
print(total_price)
if total_price < 100:
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        print('test')
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="rodgersotieno@myyahoo.com",
                            msg=f"Subject:Amazon price alert!\n\n{title} is now ${total_price}\n\n"
                                f"Buy now: {LINK}".encode("utf-8"))
        print(connection.getreply())
