import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, 'html.parser')

all_movies = soup.find_all(name="h3", class_="title")
movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]
# reverse starting from the last element to the first, stepping by one
# for n in range(len(movie_titles) - 1, -1, -1):
#     movies = movie_titles[n]
with open("movies.txt", mode='w', encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")



