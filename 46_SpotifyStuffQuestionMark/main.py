from scraper import get_track_list
import spotify_fiddler

# 1. Get the user's input and append it to the Billboard's URL
time_machine_target = input("Which year do you want to travel to? Input your date like this: YYYY-MM-DD: ")
if time_machine_target == "" or time_machine_target == "s" or len(time_machine_target) != 10:
    time_machine_target = "1992-01-03"

# 2. Get the track list from that specific time
track_list = get_track_list(time_machine_target)

# 3. Setup Spotify
sp = spotify_fiddler.setup_spotify()

# 4. Create a playlist
playlist = spotify_fiddler.create_playlist(sp, time_machine_target)

# 5. Generate a list of URIs based on our scraped list
tracks = spotify_fiddler.get_list_of_URIs(sp, track_list)

print(tracks)

# 6. Populate the playlist
spotify_fiddler.add_to_playlist(sp, tracks, playlist["id"])