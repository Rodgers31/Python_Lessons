from bs4 import BeautifulSoup
import requests

response = requests.get('https://appbrewery.github.io/instant_pot/')
price = response.text

soup = BeautifulSoup(price, 'html.parser')

item_price = soup.find("span", {"class": 'a-offscreen'}).getText()
remove_dollar = item_price.split("$")[1]
total_price = float(remove_dollar)
print(total_price)
