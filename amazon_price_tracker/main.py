import os

from bs4 import BeautifulSoup
import requests
from smtplib import SMTP
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv('MY_EMAIL')
PASSWORD = os.getenv('PASSWORD')

LINK = 'https://appbrewery.github.io/instant_pot/'
response = requests.get(LINK, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                                                     "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36", })
price = response.text

soup = BeautifulSoup(price, 'html.parser')

item_price = soup.find("span", {"class": 'a-offscreen'}).get_text()
title = soup.find("span", {"id": "productTitle"}).get_text().strip()
remove_dollar = item_price.split("$")[1]
total_price = float(remove_dollar)
title = title.replace(" ", '')
if total_price < 100:
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        print('test')
        connection.sendmail(from_addr=EMAIL, to_addrs="rodgersotieno@myyahoo.com",
                            msg=f"Subject:Amazon price alert!\n\n{title} is now ${total_price}\n\n"
                                f"Buy now: {LINK}".encode("utf-8"))
        print(connection.getreply())
