#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from keyholder import Keyholder
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from email_account import EmailAccount

keyholder = Keyholder()
data_manager = DataManager(keyholder.sheety_endpoint)
flight_search = FlightSearch()

import requests as rq
from datetime import datetime as dt

import smtplib

def main():
    sheet_data = data_manager.get_sheety_data()
    
    # Flight list!
    f = list()
    
    for city in sheet_data:
        # city = flight_search.get_IATA_code(city, keyholder.tequila_key)
        # data_manager.update_city_data(city["iataCode"], city["id"])
        flights = flight_search.search_flights(city["iataCode"], keyholder.tequila_key)
        found = False
        
        # Search for each flight
        for flight in flights["data"]:
            if flight["price"] <= city["lowestPrice"]:
                found = True
                f.append(flight)
                # print("Found cheaper flight! Use write_message() passing 'flight' as a parameter.")
#                print(f">> {flight['price']}")

        if found:
            print(f"Found good flights for {city['city']}!")
        else:
            print(f"Found no flights for {city['city']} priced lower than £{city['lowestPrice']}!")

    if len(f) > 0:
        print("Writing an email! :)")
        write_message(f)
    else:
        print("Found no flights! :(")
        

def write_message(flights: list):
    GMAIL_SMTP = "smtp.gmail.com"

    sender = EmailAccount("39_FlightDealFinder\e_sender.lsfl")
    receiver = EmailAccount("39_FlightDealFinder\e_receiver.lsfl")
    
    # Generate message string:
    message = "Subject:[FlightDealFinder] I found cheap flights just for you!\n\n"
    
    i = 1
    # For each flight... add relevant information
    for flight in flights:
        
        outbound = flight["route"][0]["local_departure"].split("T")[0]
        inbound = flight["route"][1]["local_departure"].split("T")[0]
    
        message += f"Flight #{i}: £{flight['price']}\n"
        message += f"> {flight['cityFrom']}/{flight['flyFrom']} to {flight['cityTo']}/{flight['flyTo']}\n"
        message += f"> From {outbound} to {inbound}\n\n"
        # message += f"> Book the flight here: {flight['deep_link']}\n\n"
        # ^ Adds too many lines :(
        i += 1
        
    # Actually send the email
    with smtplib.SMTP(GMAIL_SMTP, port = 587) as connection:
        connection.starttls()
        
        connection.login(
            user = sender.username,
            password = sender.password
        )
    
        connection.sendmail(
            from_addr = sender.username,
            to_addrs = receiver.username,
            msg = message.encode("utf-8")
        )
    
    

if __name__ == "__main__":
    main()