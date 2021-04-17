import spotipy
from spotipy import oauth2
import time
from IPython.core.display import clear_output
from spotipy import SpotifyClientCredentials, util
import pandas as pd
import time
import numpy as np
import csv
import matplotlib.pyplot as plt
import numpy as np
import requests
import json
from xml.dom import minidom
import xml.etree.ElementTree as ET
from datetime import date
from dotenv import load_dotenv
import sys


def getPlaylistTracksIDs(user, playlist_id, sp):
    ids = []
    playlist = sp.user_playlist(user, playlist_id)
    for item in playlist['tracks']['items']:
        track = item['track']
        ids.append(track['id'])
    return ids

client_id = '46c1cfc8247e4267b8f5516f9a61affc'
client_secret = '704027695cb84a95b86351d933d63acd'
myPlaylist = "1MhgN6Lgn83GprBszMayql"
ryanPlaylist = "4wn7D16SNoiniwzooOYS2x"

user = input("Enter profile link for user: ")
user = user.replace('https://open.spotify.com/user/', '')
user = user.split('?')
user = user[0]
token = util.prompt_for_user_token(
    username=user,
    scope='playlist-modify-public playlist-modify-private playlist-read-collaborative user-library-read user-follow-read',
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri="http://localhost:8889/callback"
)
if token:
   sp = spotipy.Spotify(auth=token)

user2 = input("Enter profile link for user: ")
user2 = user2.replace('https://open.spotify.com/user/', '')
user2 = user2.split('?')
user2 = user2[0]
token = util.prompt_for_user_token(
    username=user2,
    scope='playlist-modify-public playlist-modify-private playlist-read-collaborative user-library-read user-follow-read',
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri="http://localhost:8889/callback",
    show_dialog = True
)
if token:
   sp2 = spotipy.Spotify(auth=token)



artists1 = sp.current_user_followed_artists()
artists2 = sp2.current_user_followed_artists()
for i in range(len(artists1['artists']['items'])):
    print(artists1['artists']['items'][i]['name'])
print()
for i in range(len(artists2['artists']['items'])):
    print(artists2['artists']['items'][i]['name'])
#print(artists1)
#print(artists2)
