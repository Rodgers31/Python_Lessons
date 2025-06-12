from bs4 import BeautifulSoup
import requests

response = requests.get('https://appbrewery.github.io/instant_pot/')
price = response.text

soup = BeautifulSoup(price, 'html.parser')

item_price = soup.find("span", {"class": 'a-price-whole'})
item_price_d = soup.find("span", {"class": 'a-price-fraction'})
total_price = f"{item_price.text}{item_price_d.text}"
print(float(total_price))
