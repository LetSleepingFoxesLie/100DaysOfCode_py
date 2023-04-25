import requests as rq

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    
    def __init__(self):
        pass
    
    def search_IATA_code(self, city: dict) -> dict:
        city["iataCode"] = "test"
        return city