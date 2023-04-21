import requests as rq

from api_reader import Api_Reader

keyholder = Api_Reader()

def main():
    nutritionix_data = make_nlp_request("Walked for 30 minutes")
    pass

def make_nlp_request(query: str, gender = "male", weight = 93.2, height = 179, age = 24) -> dict:
    N_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
    
    headers = {
        "x-app-id": keyholder.nutritionix_id,
        "x-app-key": keyholder.nutritionix_key
    }
    
    body = {
        "query": query,
        "gender": gender,
        "weight_kg": weight,
        "height_cm": height,
        "age": age
    }
    
    response = rq.post(
        url = N_ENDPOINT,
        headers = headers,
        json = body
    )
    
    response.raise_for_status()
    return response.json()
    

if __name__ == "__main__":
    main()