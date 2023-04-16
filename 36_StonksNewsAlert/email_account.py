class Email_Account:
    def __init__(self, input_file: str):
        try:
            with open(input_file, "r") as f:
                self.username = f.readline().strip("\n")
                self.password = f.readline().strip("\n")
        except FileNotFoundError:
            print("File not found! Using dummy credentials that won't work.")
            self.username = "exampleaccount@gmail.com"
            self.password = "examplepassword"