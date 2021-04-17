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

def authUser():
    user = input("Enter profile link for user: ")
    user = user.replace('https://open.spotify.com/user/', '')
    user = user.split('?')
    user = user[0]
    token = util.prompt_for_user_token(
        username=user,
        scope='playlist-modify-public',
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri="http://localhost:8889/callback"
    )
    if token:
       sp = spotipy.Spotify(auth=token)
    return sp, user

def printIDs(user, playlist, sp):
    ids  = getPlaylistTracksIDs(user, playlist, sp)
    for i in ids:
          print(i)


client_id = '46c1cfc8247e4267b8f5516f9a61affc'
client_secret = '704027695cb84a95b86351d933d63acd'

sp1, user1 = authUser()
myPlaylist = "1MhgN6Lgn83GprBszMayql"
printIDs(user1, myPlaylist, sp1)

sp2, user2 = authUser()
ryanPlaylist = "4wn7D16SNoiniwzooOYS2x"
printIDs(user2, ryanPlaylist, sp2)
