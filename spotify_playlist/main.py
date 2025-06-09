import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
from dateutil import parser
import requests

load_dotenv("key.env")
play_date = input("What year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{play_date}/"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
}

response = requests.get(URL, headers=headers)
bill_board = response.text


soup = BeautifulSoup(bill_board, "html.parser")

song_titles = []

data = soup.find_all("h3", {"id": 'title-of-a-story', "class": "a-no-trucate"})

songs = [song.getText().strip() for song in data]

client_id = os.getenv("CLIENT_ID")
secret = os.getenv("CLIENT_SECRET")
url = "https://spotify.com/jacob"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=secret, redirect_uri=url,
                                               scope="playlist-modify-private", username="Doger", show_dialog=True,))

user_id = sp.current_user()["id"]
song_url = []
for song in songs:
    play_list = sp.search(type="track", q=f"{song}", limit=1)
    url = play_list['tracks']['items']
    for track in url:
        song_url.append(track['uri'])

# add to playlist
playlist = sp.user_playlist_create(user=user_id, name=f"{play_date} Billboard 100", public=False)
print(playlist)
add_playlist = sp.playlist_add_items(playlist_id=playlist["id"], items=song_url)
print(add_playlist)



