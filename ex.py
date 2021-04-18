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
from flask import Flask, redirect, request

client_id = '46c1cfc8247e4267b8f5516f9a61affc'
client_secret = '704027695cb84a95b86351d933d63acd'

def createSp():
    token = util.prompt_for_user_token(
        username="92y2ill9uonu0cqagd25rvztt",
        scope='playlist-modify-public playlist-read-collaborative',
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri="http://localhost:8889/callback"
    )
    if token: return spotipy.Spotify(auth=token)

def getNewPlaylistID(sp):
    id = str(sp.user_playlists(userID)['items'][0]['uri'])
    print(id)

sp = createSp()
getNewPlaylistID(sp)
