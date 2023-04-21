class Account_Handler:
    def __init__(self):
        try:
            with open (r"37_HabitTracking/pixela_account.lsfl", "r") as f:
                self.username = f.readline().strip("\n")
                self.token = f.readline().strip("\n")
        except FileNotFoundError:
            print("Literally get fucked")