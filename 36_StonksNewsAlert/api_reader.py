FOLDER_NAME = "36_StonksNewsAlert\\"

class API_Reader:
    def __init__(self, file_name: str):
        self.key: str
        try:
            file_path = FOLDER_NAME + file_name
            print(file_path)
            with open(file_path, "r") as f:
                self.key = f.read()
        except FileNotFoundError:
            self.key = "Get rekt"
        