#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from keyholder import Keyholder
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch

keyholder = Keyholder()
data_manager = DataManager(keyholder.sheety_endpoint)
flight_search = FlightSearch()

def main():
    # sheet_data = data_manager.get_sheety_data()
    sheet_data = [{'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 54, 'id': 2}, {'city': 'Berlin', 'iataCode': 'BER', 'lowestPrice': 42, 'id': 3}, {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 485, 'id': 4}, {'city': 'Sydney', 'iataCode': 'SYD', 'lowestPrice': 551, 'id': 5}, {'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice': 95, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 414, 'id': 7}, {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 240, 'id': 8}, {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 260, 'id': 9}, {'city': 'Cape Town', 'iataCode': 'CPT', 'lowestPrice': 378, 'id': 10}]
    
    for city in sheet_data:
        # city = flight_search.get_IATA_code(city, keyholder.tequila_key)
        # data_manager.update_city_data(city["iataCode"], city["id"])
        flights = flight_search.search_flights(city["iataCode"], keyholder.tequila_key)
        
        # Search for each flight
        for flight in flights["data"]:
            if flight["price"] <= city["lowestPrice"]:
                print("Found cheaper flight! Use write_message() passing 'flight' as a parameter.")
#                print(f">> {flight['price']}")

def write_message():
    pass

if __name__ == "__main__":
    main()