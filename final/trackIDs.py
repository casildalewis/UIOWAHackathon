import spotipy
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


def getPlaylistTracksIDs(user, playlist_id):
    ids = []
    playlist = sp.user_playlist(user, playlist_id)
    for item in playlist['tracks']['items']:
        track = item['track']
        ids.append(track['id'])
    return ids

client_id = '17405d2547fb46feb163562e0749d55d'
client_secret = '40aa39d95521404b9bbbb2ae6538a65f'
token = util.prompt_for_user_token(
    username='92y2ill9uonu0cqagd25rvztt',
    scope='playlist-modify-public',
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri="http://localhost:8000/callback/"
)
if token:
   sp = spotipy.Spotify(auth=token)
ids  = getPlaylistTracksIDs('92y2ill9uonu0cqagd25rvztt', '1MhgN6Lgn83GprBszMayql')
for i in ids:
    print(i)
