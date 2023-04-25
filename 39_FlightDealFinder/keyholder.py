class Keyholder:
    
    def __init__(self):
        
        # 1. Sheety
        with open(self.return_relative_path("api_sheety"), "r") as f:
            self.sheety_endpoint = f.readline().strip("\n")
            print(self.sheety_endpoint)
    
    
    def return_relative_path(self, file_name: str) -> str:
        return f"39_FlightDealFinder\\{file_name}.lsfl"
    

# a = Keyholder()