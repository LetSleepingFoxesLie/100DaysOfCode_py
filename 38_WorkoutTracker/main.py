import requests as rq
import datetime as dt

from api_reader import Api_Reader

keyholder = Api_Reader()

def main():
    
    # Get input
    workout = input("Describe your workout: ")
    
    # Get data from Nutritionix
    nutritionix_data = make_nlp_request(workout)
    
    # For each exercise...
    for exercise in nutritionix_data["exercises"]:
        print(exercise)
        
        # And then parse the data
        activity = exercise["name"].title()
        duration = exercise["duration_min"]
        calories = exercise["nf_calories"]
        
        # Parse dates
        now = dt.datetime.now()
        date = now.strftime("%d/%m/%Y")    
        time = now.strftime("%H:%M:%S")
        
        # Make API call to add something to my spreadsheet
        add_data_to_spreadsheet(
            date = date,
            time = time,
            exercise = activity,
            duration = duration,
            calories = calories
        )

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

def add_data_to_spreadsheet(date: str, time: str, exercise: str, duration: str, calories: str):
    # Headers: date, time, exercise, duration, calories
    
    headers = {
        "Content-Type": "application/json"
    }
    
    body = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise,
            "duration": duration,
            "calories": int(calories)
        }
    }
    
    response = rq.post(
        url = keyholder.sheety_endpoint,
        headers = headers,
        json = body
    )
    
    response.raise_for_status()
    print(response.text)

if __name__ == "__main__":
    main()