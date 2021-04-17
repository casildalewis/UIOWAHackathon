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
def createSp(username):
    token = util.prompt_for_user_token(
    username=username,
    scope='playlist-modify-public playlist-read-collaborative',
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri="http://localhost:8889/callback")
    if token: return spotipy.Spotify(auth=token)

"""
Ivan's code
Gets songs from playlist chosen by user user
returns a List of string of song IDs
"""
def getPlaylistTracksIDs(usr, username):
    playlist = getPlaylist(usr, username)['id']
    tracks = []
    playlist = usr.user_playlist(username, playlist)
    for item in playlist['tracks']['items']:
        track = item['track']
        tracks.append((track['id'], track['name']))
    return tracks

def getPlaylist(usr, username):
    playlists = usr.user_playlists(username)
    for playlist in playlists['items']:
        print(playlist['name'])
    chosen = input("Please type the name of playlist to match: ")
    for playlist in playlists['items']:
        if playlist['name'] == chosen: return playlist


def getUser():
    user = input("Enter profile link for user: ")
    user = user.replace('https://open.spotify.com/user/', '')
    user = user.split('?')
    print(user[0])
    return user[0]

def compareList(track_usr1, track_usr2):
    match = []
    for track in track_usr1:
        if track in track_usr2:
            match.append(track)
    return match

#Set up
print("For User 1: ")
username1 = getUser()
token = util.prompt_for_user_token(
    username=username1,
    scope='playlist-modify-public playlist-read-collaborative',
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri="http://localhost:8889/callback")
if token:
    usr1 = spotipy.Spotify(auth=token)
usr1 = createSp(username1)
track_usr1 = getPlaylistTracksIDs(usr1, username1)
print("For User 2: ")
username2 = getUser()
token = util.prompt_for_user_token(
    username=username2,
    scope='playlist-modify-public playlist-read-collaborative',
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri="http://localhost:8889/callback")
if token:
    usr2 = spotipy.Spotify(auth=token)
usr2 = createSp(username2)
track_usr2 = getPlaylistTracksIDs(usr2, username2)
#Matches
match = compareList(track_usr1, track_usr2)
trackIDs = []
#Output matches
for track in match:
    print(track[1])
    trackIDs.append(track[0])
New_usr1 = usr1.user_playlist_create(username1, name = "The New Shared Playlist",
                                     public = True, collaborative = False)['uri']
usr1.user_playlist_add_tracks(username1, New_usr1, trackIDs)