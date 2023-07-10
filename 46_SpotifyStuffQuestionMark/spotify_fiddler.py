import spotipy
from spotipy.oauth2 import SpotifyOAuth

from keyholder import Keyholder
from song import Song

# 1. We gotta log in somehow

def setup_spotify() -> spotipy.Spotify:
    keys = Keyholder()

    sp = spotipy.Spotify(
        auth_manager = SpotifyOAuth(
            client_id = keys.id,
            client_secret = keys.secret,
            redirect_uri = "https://example.com",
            scope = "playlist-modify-private playlist-modify-private playlist-modify-public"
        )
    )
    
    return sp

# https://spotipy.readthedocs.io/en/latest/
# user_id = sp.current_user()["id"]
# print(user_id)

# 2. Searching for songs?
def get_song_URI(sp: spotipy.Spotify, track: Song, year: int = 0):
    
    if year == 0:
        query = f"artist:{track.artist} track:{track.title}"
    else:
        query = f"artist:{track.artist} track:{track.title} year:{year}"
    
    response = sp.search(
        q = query,
        limit = 1,
        type = "track"
    )
    
#    print(response)

    ## Handling the response json
    # print(response["tracks"]["items"][0]["uri"])
    # print(response["tracks"]["items"][0]["external_urls"]["spotify"])
    
    try:
        return response["tracks"]["items"][0]["uri"]
    except IndexError:
        if year != 0:
            print(f"{track.artist} - {track.title} ({year}) not found!")
        else:
            print(f"{track.artist} - {track.title} not found!")
        return None

# Generating list of URIs from our scraped list
def get_list_of_URIs(sp: spotipy.Spotify, track_list: list):
    URI_list = list()

    for track in track_list:
        URI: str = get_song_URI(sp, track)
        
        if URI == None:
            continue
        
        URI_list.append(URI.split(":")[2])
        
    print(f"List of URIs is {len(URI_list)} elements long")
    return URI_list

# Create a playlist, returns the playlist's ID
def create_playlist(sp: spotipy.Spotify, time_machine_target: str):
    return sp.user_playlist_create(
        user = sp.current_user()["id"],
        name = f"{time_machine_target} Billboard top 100!",
        public = False,
        description = "Generated automatically by sleepy, drooly foxes! Or government drones :)"
    )

# Add songs to a playlist based on URI
def add_to_playlist(sp: spotipy.Spotify, track_URIs: list, playlist_id: str):
    sp.playlist_add_items(
        playlist_id = playlist_id,
        items = track_URIs
    )

'''   
def test():
    sp = setup_spotify()
    song = Song("Michael Jackson", "Black or White")
    print(get_song_URI(sp, song))

def test_playlist_add():
    sp = setup_spotify()
    song = Song("Michael Jackson", "Black or White")
    playlist_id = "3iY2qqtLxqrfiRHL12xkOd"
    
    song_URI = get_song_URI(sp, song)
    add_to_playlist(sp, song_URI, playlist_id) 

sp = setup_spotify()
URI = get_song_URI(sp, Song("Evanescence", "My Immortal"))
add_to_playlist(sp, [URI], "3iY2qqtLxqrfiRHL12xkOd")
'''