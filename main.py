from bs4 import BeautifulSoup
import os
import requests
import spotipy
from spotipy.oauth2 import

client_id = os.environ.get("SPOTIPY_CLIENT_ID")
client_secret = os.environ.get("SPOTPY_CLIENT_SECRET")
user_date = input("Which year do you want to travel to? Type the data in this format YYYY-MM-DD: ")
response = requests.get("https://www.billboard.com/charts/hot-100/" + user_date)

soup = BeautifulSoup(response.text, "html.parser")
best_songs = soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")
song_titles = [song.getText().strip("\n\t") for song in best_songs]
print(song_titles)


#article_upvotes = [int(score.getText().split()[0]) for score in soup.findAll("span", class_="score")]


# with open("website.html") as file:
#     contents = file.read()
# soup = BeautifulSoup(contents, "html.parser")
# all_anchors = soup.findAll(name="a")
# print(all_anchors)
# for anchor in all_anchors:
#     print(anchor.get("href"))
# heading = soup.find(name="h1", id="name")
# company_url = soup.select_one("p a")
# print(company_url)
# headings = soup.select(".heading")
# print((headings))
