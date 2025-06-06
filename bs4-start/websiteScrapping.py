from bs4 import BeautifulSoup
import requests



response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
print(soup.title)
title = soup.find_all(class_="titleline")
print(title)
value = {i.text: i.find('a') for i in title}
print(value)

