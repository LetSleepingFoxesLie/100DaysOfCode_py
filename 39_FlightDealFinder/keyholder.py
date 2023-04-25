class Keyholder:
    
    def __init__(self):
        
        # 1. Sheety
        with open(self.return_relative_path("api_sheety"), "r") as f:
            self.sheety_endpoint = f.readline().strip("\n")
            
        # 2. Tequila
        with open(self.return_relative_path("api_tequila"), "r") as f:
            self.tequila_key = f.readline().strip("\n")
        
        # 3. Telegram instead of Twilio... because I'm a rebel
        with open(self.return_relative_path("api_telegram"), "r") as f:
            self.telegram_token = f.readline().strip("\n")
    
    
    def return_relative_path(self, file_name: str) -> str:
        return f"39_FlightDealFinder\\{file_name}.lsfl"
    

# a = Keyholder()