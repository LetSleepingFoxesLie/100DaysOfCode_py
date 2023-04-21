from account import Account_Handler
from typing import Union
import requests
import datetime as dt

class Pixel:
    
    def __init__(self):
        self.ENDPOINT = "https://pixe.la/v1/users"
        self.ACCOUNT = Account_Handler()

    def add_pixel(self, quantity: Union[float, int], graph_id: str) -> None:
        GRAPH_ENDPOINT = f"{self.ENDPOINT}/{self.ACCOUNT.username}/graphs/{graph_id}"
        
        headers = {
            "X-USER-TOKEN": self.ACCOUNT.token
        }
        
        today = dt.datetime.now()
        today = today.strftime("%Y%m%d")
        print(today)
        
        body = {
            "date": today,
            "quantity": str(quantity),
        }
        
        r = requests.post(
            url = GRAPH_ENDPOINT,
            json = body,
            headers = headers
        )
        
        print(r.text)
    
    def update_pixel(self, quantity: Union[float, int], graph_id: str, date: str) -> None:
        """_summary_

        Args:
            quantity (Union[float, int]): Accepts either a float or an int
            graph_id (str): The ID of your Pixela graph
            date (str): Write in the following format: "yyyyMMdd"
        """
        
        GRAPH_ENDPOINT = f"{self.ENDPOINT}/{self.ACCOUNT.username}/graphs/{graph_id}/{date}"
        
        headers = {
            "X-USER-TOKEN": self.ACCOUNT.token
        }
        
        body = {
            "quantity": str(quantity),
        }
        
        r = requests.put(
            url = GRAPH_ENDPOINT,
            json = body,
            headers = headers
        )
        print(r.text)

    def delete_pixel(self, graph_id: str, date: str) -> None:
        """ Deletes a Pixela pixel
        
        Args:
            date (str): "yyyyMMdd" format
        """
        GRAPH_ENDPOINT = f"{self.ENDPOINT}/{self.ACCOUNT.username}/graphs/{graph_id}/{date}"
        
        headers = {
            "X-USER-TOKEN": self.ACCOUNT.token
        }
        
        r = requests.delete(
            url = GRAPH_ENDPOINT,
            headers = headers
        )
        
        print(r.text)