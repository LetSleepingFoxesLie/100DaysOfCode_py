import requests
from account import Account_Handler
from pixel import Pixel

ACCOUNT = Account_Handler()
ENDPOINT = "https://pixe.la/v1/users"

pixela = Pixel()

def main():
    # pixela.add_pixel(3, "dumbfox")
    pixela.delete_pixel("dumbfox", "20230416")
    pass

def register_pixela():
    params = {
        "token": ACCOUNT.token,
        "username": ACCOUNT.username,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }
    
    response = requests.post(url = ENDPOINT, json = params)
    print(response.text)

def create_graph():
    GRAPH_ENDPOINT = f"{ENDPOINT}/{ACCOUNT.username}/graphs"
    
    g_params = {
        "id": "dumbfox",
        "name": "stuff",
        "unit": "slaps",
        "type": "int",
        "color": "ajisai"
    }
    
    headers = {
        "X-USER-TOKEN": ACCOUNT.token
    }
    
    response = requests.post(
        url = GRAPH_ENDPOINT,
        json = g_params,
        headers = headers
    )
    
    print(response.text)
    print(f"Check your new pixela graph at {GRAPH_ENDPOINT}/{g_params['id']}.html")

if __name__ == "__main__":
    main()