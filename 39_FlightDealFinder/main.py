#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from keyholder import Keyholder
from data_manager import DataManager, UserManager
from flight_data import FlightData # Ended up not using it.
from flight_search import FlightSearch
from email_account import EmailAccount

keyholder = Keyholder()
data_manager = DataManager(keyholder.sheety_endpoint)
user_manager = UserManager(keyholder.sheety_endpoint_users)
flight_search = FlightSearch()

import requests as rq
from datetime import datetime as dt

import smtplib

def main():
    
    # Gets the data from our spreadsheet through Sheety
    sheet_data = data_manager.get_sheety_data()
    
    # Register procedure, adding it as a function for clarity
    user_manager.register_user()
        
    # Now let's send it through Sheety to our spreadsheet
    user_manager.add_user_to_spreadsheet()
    
    # Flight list! Initializing it for later purposes
    f = list()
    
    # Search flightsd 
    
    # Now let's fetch good flight deals
    for city in sheet_data:
        
        flights = flight_search.search_flights(city["iataCode"], keyholder.tequila_key)
        found = False
        
        # Search for each flight
        try:
            for flight in flights["data"]:
                if flight["price"] <= city["lowestPrice"]:
                    found = True
                    f.append(flight)
        except KeyError:
            continue
                
        if found:
            print(f"Found good flights for {city['city']}!")
        else:
            print(f"Found no flights for {city['city']} priced lower than £{city['lowestPrice']}!")

    # If the list of found flights is NOT empty, write an email with all cheap flights.
    if len(f) > 0:
        print("Writing an email! :)")
        write_message(f)
    else:
        print("Found no flights! :(")
        

# Rewriting to get all emails from out spreadsheet
def write_message(flights: list):
    GMAIL_SMTP = "smtp.gmail.com"

    sender = EmailAccount("39_FlightDealFinder\e_sender.lsfl")
    receiver_list = user_manager.get_emails()
    
    # Send an email for each individual in our list
    for user in receiver_list:
        
        print(f"Composing an email for {user['email']}...")
        
        # Generate message string:
        message_header = f"Subject:[FlightDealFinder] I found cheap flights just for you, {user['firstName']}!\n\n"
        message_header += f"Hello, {user['firstName']} {user['lastName']}! Look at our selection of cheap flights: \n\n"
        message_body = str()
        i = 1
        
        # For each flight... add relevant information
        for flight in flights:
            
            outbound = flight["route"][0]["local_departure"].split("T")[0]
            inbound = flight["route"][1]["local_departure"].split("T")[0]
        
            message_body += f"Flight #{i}: £{flight['price']}\n"
            message_body += f"> {flight['cityFrom']}/{flight['flyFrom']} to {flight['cityTo']}/{flight['flyTo']}\n"
            message_body += f"> From {outbound} to {inbound}\n\n"
            # message += f"> Book the flight here: {flight['deep_link']}\n\n"
            # ^ Adds too many lines :(
            i += 1
        
        message = message_header + message_body
        
        # Actually send the email
        with smtplib.SMTP(GMAIL_SMTP, port = 587) as connection:
            connection.starttls()
            
            connection.login(
                user = sender.username,
                password = sender.password
            )
        
            connection.sendmail(
                from_addr = sender.username,
                to_addrs = user["email"],
                msg = message.encode("utf-8")
            )

            print(f"Email sent to {user['email']}!")
        

if __name__ == "__main__":
    main()