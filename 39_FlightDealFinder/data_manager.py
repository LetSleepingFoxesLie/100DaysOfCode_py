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
    
class UserManager:
    """Responsible for handling new users!
    Requires a Sheety endpoint.
    """
    def __init__(self, sheety_endpoint: str):
        
        # Saving the endpoint to a class attribute
        self.sheety_endpoint = sheety_endpoint
        
        # Register procedure, adding it as a function for clarity
        self.register_user()
        
        # Now let's send it through Sheety to our spreadsheet
        self.add_user_to_spreadsheet()
        
        
    def register_user(self):
        """
        Registers a new user.
        """
        print("Welcome to LSFL's not-so-secret Fright* Club.")
        print("Yes, 'fright', for you will be scared at the low low prices!")
        print("* Totally not affiliated with Necrosoft Fright Simulacrum.")
        
        self.first_name = input("Insert your first name: ").title()
        self.last_name = input("Insert your last name: ").title()
        while True:
            self.email = input("Insert your email: ")
            confirmation = input("Please enter your email again: ")
            
            if self.email == confirmation:
                return
            print("Error: emails don't match! Let's try again :)")
    
    
    def add_user_to_spreadsheet(self):
        
        # Headers
        headers = {
            "Content-Type": "application/json"
        }
        
        # Body:
        body = {
            "user": {
                "firstName": self.first_name,
                "lastName": self.last_name,
                "email": self.email
            }
        }
        
        print("Adding your name to the list, please wait...")
        
        # Send a POST request to Sheety to add a new row to our spreadsheet
        try:
            response = rq.post(
                url = self.sheety_endpoint,
                headers = headers,
                json = body
            )
        
            response.raise_for_status()
            print(f"{self.first_name} {self.last_name} ({self.email}) was added to the list!")
        except rq.exceptions.HTTPError as e:
            print("Something went wrong! Try another time...")
            raise e