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
    sheet_data = [{'city': 'Paris', 'iataCode': '', 'lowestPrice': 54, 'id': 2}, {'city': 'Berlin', 'iataCode': '', 'lowestPrice': 42, 'id': 3}, {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 485, 'id': 4}, {'city': 'Sydney', 'iataCode': '', 'lowestPrice': 551, 'id': 5}, {'city': 'Istanbul', 'iataCode': '', 'lowestPrice': 95, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': '', 'lowestPrice': 414, 'id': 7}, {'city': 'New York', 'iataCode': '', 'lowestPrice': 240, 'id': 8}, {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': 260, 'id': 9}, {'city': 'Cape Town', 'iataCode': '', 'lowestPrice': 378, 'id': 10}]
    
    for city in sheet_data:
        city = flight_search.search_IATA_code(city)
        data_manager.update_city_data(city["iataCode"], city["id"])

if __name__ == "__main__":
    main()