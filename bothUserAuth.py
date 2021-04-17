import spotipy
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

user1 = input("Enter profile link for user 1: ")
user1 = user1.replace('https://open.spotify.com/user/', '')
user1 = user1.split('?')
user = user1[0]
token1 = util.prompt_for_user_token(
    username=user1,
    scope='playlist-modify-public',
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri="http://localhost:8889/callback"
)

if token1:
   sp1 = spotipy.Spotify(auth=token1)

myPlaylist = "1MhgN6Lgn83GprBszMayql"

ids  = getPlaylistTracksIDs(user1, myPlaylist, sp1)
for i in ids:
      print(i)

user2 = input("Enter profile link for user 2: ")
user2 = user2.replace('https://open.spotify.com/user/', '')
user2 = user2.split('?')
user = user2[0]
token2 = util.prompt_for_user_token(
    username=user2,
    scope='playlist-modify-public',
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri="http://localhost:8889/callback"
)

if token2:
   sp2 = spotipy.Spotify(auth=token2)

ryanPlaylist = "4wn7D16SNoiniwzooOYS2x"

ids  = getPlaylistTracksIDs(user2, ryanPlaylist, sp2)
for i in ids:
    print(i)
