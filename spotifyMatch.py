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

client_id = '46c1cfc8247e4267b8f5516f9a61affc'
client_secret = '704027695cb84a95b86351d933d63acd'
def createToken(username):
    token = util.prompt_for_user_token(
    username=username,
    scope='playlist-modify-public playlist-read-private playlist-read-collaborative',
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri="http://localhost:8889/callback")
    if token: return token

"""
Ivan's code
Gets songs from playlist chosen by user user
returns a List of string of song IDs
"""
def getPlaylistTracksIDs():
    username = getUser()
    sp = spotipy.Spotify(auth=createToken(username))
    playlist = getPlaylists()
    tracks = []
    playlist = sp.user_playlist(username, playlist)
    for item in playlist['tracks']['items']:
        track = item['track']
        tracks.append((track['id'], track['name']))
    return tracks

def getPlaylists():
    playlist = input("Enter playlist link you want to match: ")
    playlist = playlist.replace('https://open.spotify.com/playlist/', '')
    playlist = playlist.split('?')
    return playlist[0]

def getUser():
    user = input("Enter profile link for user: ")
    user = user.replace('https://open.spotify.com/user/', '')
    user = user.split('?')
    return user[0]

def compareList(track_usr1, track_usr2):
    match = []
    for track in track_usr1:
        if track in track_usr2:
            match.append(track)
    return match

print("For user 1: ")
track_usr1 = getPlaylistTracksIDs()
print("For user 2: ")
track_usr2 = getPlaylistTracksIDs()
match = compareList(track_usr1, track_usr2)
for track in match:
    print(track[1])