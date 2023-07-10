class Keyholder:
    def __init__(self):
        with open(r"46_SpotifyStuffQuestionMark\spotify.lsfl", "r") as f:
            self.id = f.readline().strip("\n")
            self.secret = f.readline().strip("\n")
        
    def __str__(self):
        return f"Client ID: {self.id}\nClient secret: {self.secret}"