class Api_Reader:
    def __init__(self):
        
        # Read Nutritionix API stuff. No try/except!
        with open(r"38_WorkoutTracker\nutritionix.lsfl", "r") as f:
            self.nutritionix_id = f.readline().strip("\n")
            self.nutritionix_key = f.readline().strip("\n")
        
        # Read Sheety endpoint
        with open(r"38_WorkoutTracker\sheety.lsfl", "r") as f:
            self.sheety_endpoint = f.readline().strip("\n")