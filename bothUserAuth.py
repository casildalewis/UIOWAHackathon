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
myPlaylist = "1MhgN6Lgn83GprBszMayql"
ryanPlaylist = "4wn7D16SNoiniwzooOYS2x"

user = input("Enter profile link for user: ")
user = user.replace('https://open.spotify.com/user/', '')
user = user.split('?')
user = user[0]
token = util.prompt_for_user_token(
    username=user,
    scope='playlist-modify-public playlist-modify-private playlist-read-collaborative',
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
token2 = util.prompt_for_user_token(
    username=user2,
    scope='playlist-modify-public playlist-modify-private playlist-read-collaborative',
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri="http://localhost:8889/callback"
)
if token2:
   sp2 = spotipy.Spotify(auth=token2)

ids = getPlaylistTracksIDs(user, myPlaylist, sp)

sp.user_playlist_create(user, name = "The New Shared Playlist", public = False, collaborative = True)
id = str(sp.user_playlists(user)['items'][0]['uri'])
sp.user_playlist_add_tracks(user, id, ids)
