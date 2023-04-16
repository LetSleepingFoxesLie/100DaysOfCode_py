class API_Reader:
    def __init__(self):
        self.key: str
        try:
            with open(r"35_WeatherAPI\api.lsfl", "r") as f:
                self.key = f.read()
        except FileNotFoundError:
            self.key = "Get rekt"
        