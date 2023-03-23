#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# "r" for raw string. Because Unicode is a bitch sometimes
INPUT_NAMES_PATH = r"24_Files\Input\Names\invited_names.txt"
INPUT_LETTER_PATH = r"24_Files\Input\Letters\starting_letter.txt"
OUTPUT_PATH = r"24_Files\Output\ReadyToSend"

def main() -> None:
    message = get_message()
    names = get_names()
    
    # Hacky
    for name in names:
        m = message.copy()
        m[0] = m[0].replace("[name]", name)
        create_file(name, m)

# Gets all the messages and puts them on a list
def get_message() -> list:
    l = list()
    with open(INPUT_LETTER_PATH, "r") as f:
        l = f.readlines()
    return l

# Same, but for the names instead
def get_names() -> list:
    l = list()
    with open(INPUT_NAMES_PATH, "r") as f:
        for line in f:
            l.append(line.strip("\n"))
    return l

# Creates all the required files
def create_file(name: str, message: list) -> None:
    with open(f"{OUTPUT_PATH}\\{name}.txt", "w") as f:
        for line in message:
            f.write(line)

main()