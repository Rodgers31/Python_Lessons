from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movies_web = response.text

soup = BeautifulSoup(movies_web, "html.parser")

# movies_list = []
movies = soup.find_all("h3", {"class": 'title'})
# get the split will ge the first item after a space, and the -1 will get the last item from the individual movie
movies_list = [x.text.split(" ", 1)[-1] for x in movies]
# reverse the movie list from first to last
reverse = movies_list[::-1]

with open('100movies.txt', 'a', encoding="utf-8") as file:
    for index, movie in enumerate(reverse, start=1):
        value = f"{index}. {movie}"
        file.write(f"{value} \n")
