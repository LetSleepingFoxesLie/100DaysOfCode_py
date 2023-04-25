class DataManager:
    #This class is responsible for talking to the Google Sheet.
    
    def __init__(self, sheety_endpoint: str):
        self.sheety_endpoint = sheety_endpoint
