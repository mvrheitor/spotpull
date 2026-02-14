from dotenv import load_dotenv, find_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv(find_dotenv())

def get_client():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=os.getenv("CLIENT_ID"),
        client_secret=os.getenv("CLIENT_SECRET"),
        redirect_uri="http://127.0.0.1:8888/callback",
        scope="user-library-read"
    ))

    return sp