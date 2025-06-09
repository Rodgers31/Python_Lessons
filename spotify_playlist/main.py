from bs4 import BeautifulSoup
from dateutil import parser
import requests

# play_date = input("What year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# format_check = "%Y-%M-%D"
URL = f"https://www.billboard.com/charts/hot-100/2025-01-01/"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
}

response = requests.get(URL, headers=headers)
bill_board = response.text


soup = BeautifulSoup(bill_board, "html.parser")

song_titles = []


# data = soup.find_all("li", {"class": "o-chart-results-list__item"})
data = soup.find_all("h3", {"id": 'title-of-a-story', "class": "a-no-trucate"})

songs = [song.getText().strip() for song in data]
print(songs)







# print(songs)