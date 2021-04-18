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
<<<<<<< Updated upstream
from flask import Flask, request, redirect
=======
from flask import Flask, redirect, request
>>>>>>> Stashed changes

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
<<<<<<< Updated upstream
def getPlaylistTracksIDs(usr, username):
    playlist = getPlaylist(usr, username)['id']
    tracks = []
    playlist = usr.user_playlist(username, playlist)
    for item in playlist['tracks']['items']:
=======
def getPlaylistTracksIDs(usr, username, selected=None):
    playlist = getPlaylist(usr, username, selected)
    tracks = []
    playlist = usr.user_playlist(username, playlist['id'])
    for item in playlist['tracks']['items']:
        
>>>>>>> Stashed changes
        track = item['track']
        tracks.append((track['id'], track['name']))
    return tracks

<<<<<<< Updated upstream
def getPlaylist(usr, username):
    playlists = usr.user_playlists(username)
    for playlist in playlists['items']:
        print(playlist['name'])
    chosen = input("Please type the name of playlist to match: ")
=======
def getPlaylist(usr, username, selected=None):
    playlists = usr.user_playlists(username)
    for playlist in playlists['items']:
        print(playlist['name'])
    #chosen = input("Please type the name of playlist to match: ")
    chosen=selected
>>>>>>> Stashed changes
    for playlist in playlists['items']:
        if playlist['name'] == chosen: return playlist


<<<<<<< Updated upstream
def getUser():
    user = input("Enter profile link for user: ")
=======
def getUser(usrID=None):
    #user = input("Enter profile link for user: ")
    user=usrID
>>>>>>> Stashed changes
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

<<<<<<< Updated upstream
# #Set up
# #print("For User 1: ")
# #username1 = getUser()
=======
def buildPlaylist(track1, track2):
    match = compareList(track_usr1, track_usr2)
    trackIDs = []
    #Output matches
    for track in match:
        print(track[1])
        trackIDs.append(track[0])
    New_usr1 = usr1.user_playlist_create(username1, name = "The New Shared Playlist",
                                        public = True, collaborative = False)['uri']
    usr1.user_playlist_add_tracks(username1, New_usr1, trackIDs)


# #Set up
# print("For User 1: ")
# username1 = getUser()
>>>>>>> Stashed changes
# token = util.prompt_for_user_token(
#     username=username1,
#     scope='playlist-modify-public playlist-read-collaborative',
#     client_id=client_id,
#     client_secret=client_secret,
#     redirect_uri="http://localhost:8889/callback")
# if token:
#     usr1 = spotipy.Spotify(auth=token)
# usr1 = createSp(username1)
# track_usr1 = getPlaylistTracksIDs(usr1, username1)
# print("For User 2: ")
# username2 = getUser()
# token = util.prompt_for_user_token(
#     username=username2,
#     scope='playlist-modify-public playlist-read-collaborative',
#     client_id=client_id,
#     client_secret=client_secret,
#     redirect_uri="http://localhost:8889/callback")
# if token:
#     usr2 = spotipy.Spotify(auth=token)
# usr2 = createSp(username2)
# track_usr2 = getPlaylistTracksIDs(usr2, username2)
# #Matches
# match = compareList(track_usr1, track_usr2)
# trackIDs = []
# #Output matches
# for track in match:
#     print(track[1])
#     trackIDs.append(track[0])
# New_usr1 = usr1.user_playlist_create(username1, name = "The New Shared Playlist",
#                                      public = True, collaborative = False)['uri']
# usr1.user_playlist_add_tracks(username1, New_usr1, trackIDs)

app = Flask(__name__)
#p1=True
@app.route('/')
<<<<<<< Updated upstream
def home():
    
=======
def home():   
>>>>>>> Stashed changes
    with open("pg1.html") as f:
        html = f.read()
    return html

<<<<<<< Updated upstream
@app.route('/signup', methods = ['POST'], endpoint='func1')
def signup():
    
    
    print("called user 1")
    Userlink = request.form['Spotify Profile Link']
    Playlink = request.form['Spotify Playlist Link']
    print("User link: " + Userlink)
    print("playlist name: " + Playlink)
    print()
=======
@app.route('/signup', methods = ['POST'])
def signup():
    
    print("called user 1")
    Userlink = request.form.get('Spotify Profile Link')
    playlistName = request.form.get('Spotify Playlist Name')
    print("User link: " + Userlink)
    print("playlist name: " + playlistName)
    print()

>>>>>>> Stashed changes
    username1 = getUser(Userlink)
    token = util.prompt_for_user_token(
    username=username1,
    scope='playlist-modify-public playlist-read-collaborative',
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri="http://localhost:8889/callback")
    if token:
        usr1 = spotipy.Spotify(auth=token)
<<<<<<< Updated upstream
    usr1_playlist = getPlaylist(usr1, username1, Playlink)['id']
    track_usr1 = getPlaylistTracksIDs(usr1, username1, usr1_playlist)

    print('user 2 called')
    Userlink2 = request.form['Spotify Profile Link2']
    Playlink2 = request.form['Spotify Playlist Link2']
    print("User link: " + Userlink2)
    print("playlist name: " + Playlink2)
    print()
=======
    usr1 = createSp(username1)
    #print("usr1 and username1")
    #print(usr1)
    #print(username1)
    usr1_playlist = getPlaylist(usr1, username1, playlistName)
    #print("usr1_playlist")
    #print(usr1_playlist)
    track_usr1 = getPlaylistTracksIDs(usr1, username1, playlistName)
    #print("track 1")
    #print(track_usr1)

    # print('user 2 called')
    # Userlink2 = request.form.get('Spotify Profile Link2')
    # playlistName2 = request.form.get('Spotify Playlist Name2')
    # print("User link: " + Userlink2)
    # print("playlist name: " + playlistName2)
    # print()

    # username2 = getUser(Userlink2)
    # token = util.prompt_for_user_token(
    # username=username2,
    # scope='playlist-modify-public playlist-read-collaborative',
    # client_id=client_id,
    # client_secret=client_secret,
    # redirect_uri="http://localhost:8889/callback")
    # if token:
    #     usr2 = spotipy.Spotify(auth=token)

    # usr2 = createSp(username2)
    # print("usr2 and username2")
    # print(usr2)
    # print(username2)
    # usr2_playlist = getPlaylist(usr2, username2, playlistName2)
    # #print(usr2_playlist)
    # print("break")
    # print(type(usr2_playlist))
    # print(usr2_playlist)
    # #track_usr2 = getPlaylistTracksIDs(usr2, username2, playlistName2)
    # #match = compareList(track_usr1, track_usr2)
    # #buildPlaylist(usr1_playlist, usr2_playlist)
    print("called user 2")
    Userlink2 = request.form.get('Spotify Profile Link2')
    playlistName2 = request.form.get('Spotify Playlist Name2')
    print("User link: " + Userlink2)
    print("playlist name: " + playlistName2)
    print()

>>>>>>> Stashed changes
    username2 = getUser(Userlink2)
    token = util.prompt_for_user_token(
    username=username2,
    scope='playlist-modify-public playlist-read-collaborative',
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri="http://localhost:8889/callback")
    if token:
        usr2 = spotipy.Spotify(auth=token)
<<<<<<< Updated upstream
    
    usr2_playlist = getPlaylist(usr2, username2, Playlink2)
    print(usr2_playlist)
    track_usr2 = getPlaylistTracksIDs(usr2, username2, usr2_playlist)
    match = compareList(track_usr1, track_usr2)
    #for i in match:
    #    print(i)
    return redirect('/')
#print(match)
if __name__ =='__main__':
    app.run(host="0.0.0.0")
    #wrapper.__name__ = func.__name__
=======
    usr2 = createSp(username2)
    #print("usr2 and username2")
    #print(usr2)
    #print(username2)
    usr2_playlist = getPlaylist(usr2, username2, playlistName2)
    #print("usr2_playlist")
    #print(usr2_playlist)
    track_usr2 = getPlaylistTracksIDs(usr2, username2, playlistName2)
    #print("track 2")
    #print(track_usr2)

    match = compareList(track_usr1, track_usr2)
    trackIDs = []
    #Output matches
    for track in match:
        print(track[1])
        trackIDs.append(track[0])
    #New_usr1 = usr1.user_playlist_create(username1, name = "The New Shared Playlist",
    #                                    public = True, collaborative = False)['uri']
    #usr1.user_playlist_add_tracks(username1, New_usr1, trackIDs)
    
    return redirect('/')

if __name__ =='__main__':
    app.run(host="0.0.0.0")
>>>>>>> Stashed changes
