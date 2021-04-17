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
from flask import Flask, request, redirect

link = 'a'
p1=True

client_id = '46c1cfc8247e4267b8f5516f9a61affc'
client_secret = '704027695cb84a95b86351d933d63acd'
def createSp(username):
    token = util.prompt_for_user_token(
    username=username,
    scope='playlist-modify-public playlist-read-private playlist-read-collaborative',
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri="http://localhost:8889/callback")
    if token: return spotipy.Spotify(auth=token)

"""
Ivan's code
Gets songs from playlist chosen by user user
returns a List of string of song IDs
"""
def getPlaylistTracksIDs(usr, username, playlist):
    tracks = []
    playlist = usr.user_playlist(username, playlist)
    for item in playlist['tracks']['items']:
        track = item['track']
        tracks.append((track['id'], track['name']))
    return tracks

def getPlaylist(usr, username, chosen):
    playlists = usr.user_playlists(username)
    for playlist in playlists['items']:
        print(playlist['name'])
    #chosen = input("Please type the name of playlist to match")
    for playlist in playlists['items']:
        if playlist['name'] == chosen: return playlist


def getUser(userData):
    user = userData
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

#print("For user 1: ")
#username1 = getUser(link)
#usr1 = createSp(username1)
#usr1_playlist = getPlaylist(usr1, username1)['id']
#track_usr1 = getPlaylistTracksIDs(usr1, username1, usr1_playlist)
#print("For user 2: ")
#username2 = getUser()
#usr2 = createSp(username2)
#usr2_playlist = getPlaylist(usr2, username2)['id']
#track_usr2 = getPlaylistTracksIDs(usr2, username2, usr2_playlist)
#match = compareList(track_usr1, track_usr2)
#for track in match:
#    print(track[1])

app = Flask(__name__)
#p1=True
@app.route('/')
def home():
    
    with open("pg1.html") as f:
        html = f.read()
    return html

@app.route('/signup', methods = ['POST'], endpoint='func1')
def signup():
    
    
    print("called user 1")
    Userlink = request.form['Spotify Profile Link']
    Playlink = request.form['Spotify Playlist Link']
    print("User link: " + Userlink)
    print("playlist name: " + Playlink)
    print()
    username1 = getUser(Userlink)
    usr1 = createSp(username1)
    usr1_playlist = getPlaylist(usr1, username1, Playlink)['id']
    track_usr1 = getPlaylistTracksIDs(usr1, username1, usr1_playlist)

    print('user 2 called')
    Userlink2 = request.form['Spotify Profile Link2']
    Playlink2 = request.form['Spotify Playlist Link2']
    print("User link: " + Userlink2)
    print("playlist name: " + Playlink2)
    print()
    username2 = getUser(Userlink2)
    usr2 = createSp(username2)
    usr2_playlist = getPlaylist(usr2, username2, Playlink2)['id']
    track_usr2 = getPlaylistTracksIDs(usr2, username2, usr2_playlist)
    match = compareList(track_usr1, track_usr2)
    for i in match:
        print(i)
    return redirect('/')
        




    
if __name__ =='__main__':
    app.run(host="0.0.0.0")
    #wrapper.__name__ = func.__name__
