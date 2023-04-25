import requests as rq

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    
    def __init__(self, sheety_endpoint: str):
        self.sheety_endpoint = sheety_endpoint

    def get_sheety_data(self):
        response = rq.get(url = self.sheety_endpoint)
        response.raise_for_status()
        return response.json()["prices"]
    
    def update_city_data(self, IATA_code: str, row_id: int) -> None:
        
        headers = {
            "Content-Type": "application/json"
        }
        
        body = {
            "price": {
                "iataCode": IATA_code
            }
        }
        
        response = rq.put(
            url = f"{self.sheety_endpoint}/{row_id}",
            headers = headers,
            json = body
        )
        response.raise_for_status()
        print(response.text)