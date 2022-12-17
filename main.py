from bs4 import BeautifulSoup
import os
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

client_id = os.environ.get("SPOTIPY_CLIENT_ID")
client_secret = os.environ.get("SPOTPY_CLIENT_SECRET")
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="58b8048b059d448894ebb94d99ccac28",
        client_secret="3d56656c9ab34120b2f6019d642a8d54",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

user_date = input("Which year do you want to travel to? Type the data in this format YYYY-MM-DD: ")
response = requests.get("https://www.billboard.com/charts/hot-100/" + user_date)
year = user_date.split("-")[0]

soup = BeautifulSoup(response.text, "html.parser")
best_songs = soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")
song_titles = [song.getText().strip("\n\t") for song in best_songs]
print(song_titles)

song_uris = []
for song in song_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify, Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{user_date} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

