# Here we go!
import requests as rq
from bs4 import BeautifulSoup
from song import Song

BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"


# Code

def get_track_list(time_machine_target: str):

    # 2. Scrape Billboard's top 100 for that date
    response = rq.get(BILLBOARD_URL + time_machine_target)
    soup = BeautifulSoup(response.text, "html.parser")

    # 3. Extract all songs
    # I hate HTML and CSS with a passion
    # I hate HTML and CSS with a passion
    # I hate HTML and CSS with a passion
    # I hate HTML and CSS with a passion
    # I hate HTML and CSS with a passion
    # I hate HTML and CSS with a passion
    # I hate HTML and CSS with a passion
    # I hate HTML and CSS with a passion
    # I hate HTML and CSS with a passion
    # I hate HTML and CSS with a passion
    # I hate HTML and CSS with a passion
    # I hate HTML and CSS with a passion

    ## Thanks, forum!
    songs = soup.select(selector = "li ul li h3")
    artists_dirty_list = soup.select(selector = "li ul li span")

    songs = [song.text.strip("\n\t") for song in songs]

    ## Using some hacky ingenuity to avoid big ass filters to clean up our artist list!
    i: int = 0
    artists = list()

    while i < 100:
        artists.append(artists_dirty_list[7 * i].text.strip("\n\t"))
        i += 1

    ## And now we're going to generate the complete list of songs!
    artist_track_list = [Song(artists[i], songs[i]) for i in range(100)]
    
    # And return it...
    return artist_track_list