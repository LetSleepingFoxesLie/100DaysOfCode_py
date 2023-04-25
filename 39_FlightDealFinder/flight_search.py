import requests as rq
from datetime import datetime as dt
from datetime import timedelta

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    
    def __init__(self):
        pass
    
    def get_IATA_code(self, city: dict, tequila_api: str) -> dict:
        
        headers = {
            "Content-Type": "application/json",
            "apikey": tequila_api
        }
        
        body = {
            "term": city["city"]
        }
        
        response = rq.get(
            url = "https://api.tequila.kiwi.com/locations/query",
            headers = headers,
            params = body
        )
        
        response.raise_for_status()
        city["iataCode"] = response.json()["locations"][0]["code"]
        return city
        
        
    
    def search_flights(self, city: str, tequila_api: str) -> dict:
        
        now = dt.now()
        max_search_range = now + timedelta(days = 180)
        
        headers = {
            "Content-Type": "application/json",
            "apikey": tequila_api
        }
        
        body = {
            "fly_from": "LON",
            "fly_to": city,
            "date_from": dt.strftime(now, "%d/%m/%Y"),
            "date_to": dt.strftime(max_search_range, "%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "curr": "GBP",
            "max_stopovers": 0
        }
        
        response = rq.get(
            url = "https://api.tequila.kiwi.com/v2/search",
            headers = headers,
            params = body
        )
        response.raise_for_status()
        
        return response.json()