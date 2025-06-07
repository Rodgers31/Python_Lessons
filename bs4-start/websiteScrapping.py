from bs4 import BeautifulSoup
import requests



response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
print(soup.title)
title = soup.find_all(class_="titleline")
value = {i.text: i.find("a") for i in title}
upvote = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]

largest_number = max(upvote)
largest_index = upvote.index(largest_number)
print(largest_number)
print(largest_index)
# print(int(upvote[0].split()[0]))


