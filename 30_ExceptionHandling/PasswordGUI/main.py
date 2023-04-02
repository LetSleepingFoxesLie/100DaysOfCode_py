from tkinter import *
from tkinter import messagebox
from random import shuffle, choice, randint
import json

FONT_NAME = "Bahnschrift"
USUAL_EMAIL = "someonesemail@provider.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    
    entry_password.delete(0, END)
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    symbols = "!@#$%&*()_+=[];-^:,<.>"
    
    N_ALPHABET = 9
    N_NUMBERS = 3
    N_SYMBOLS = 3
    
    s = list()
    s += [choice(alphabet) if randint(0, 1) == 0 else choice(alphabet).upper() for i in range(N_ALPHABET)]
    s += [choice(numbers) for i in range(N_NUMBERS)]
    s += [choice(symbols) for i in range(N_SYMBOLS)]

    shuffle(s)
    
    password = str()
    for character in s:
        password += character
    
    window.clipboard_clear()
    window.clipboard_append(password)
    entry_password.insert(END, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

# Fetch password... if it exists:
def get_password():
    try:
        with open(r"30_ExceptionHandling\PasswordGUI\data.json", "r") as f:
            data = json.load(f)
            try:
                website = entry_website.get()
                username = data[website]["username"]
                password = data[website]["password"]
                
                entry_name.delete(0, END)
                entry_password.delete(0, END)
                
                entry_name.insert(0, username)
                entry_password.insert(0, password)

                entry_website.config(highlightcolor = "lime", highlightthickness = 1, highlightbackground = "lime")
                entry_name.config(highlightcolor = "lime", highlightthickness = 1, highlightbackground = "lime")
                entry_password.config(highlightcolor = "lime", highlightthickness = 1, highlightbackground = "lime")
            except KeyError:
                messagebox.showerror(
                    title = "Error!",
                    message = f"Website {website} not found."
                )
    except json.decoder.JSONDecodeError:
        messagebox.showwarning(
            title = "Warning",
            message = "No passwords in file!"
        )
    except FileNotFoundError:
        messagebox.showwarning(
            title = "Warning",
            message = "File was not found."
        )

# Get all relevant information and save it to a file
def save_information_to_file():
    
    website = entry_website.get().lower()
    username = entry_name.get()
    password = entry_password.get()
    
    data = {
        website: {
            "username": username,
            "password": password
        }
    }
    
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(
            title = "Error - Empty fields",
            message = "Please fill all blank fields."
        )
        if len(website) == 0:
            entry_website.config(highlightcolor = "red", highlightthickness = 1, highlightbackground = "red")
        if len(username) == 0:
            entry_name.config(highlightcolor = "red", highlightthickness = 1, highlightbackground = "red")
        if len(password) == 0:
            entry_password.config(highlightcolor = "red", highlightthickness = 1, highlightbackground = "red")
        return
    
    confirm = messagebox.askokcancel(
        title = website, 
        message = f"These are the details you entered: \nUsername: {username}\nPassword: {password}\nConfirm?"
    )
    
    if confirm:
        try:
            with open(r"30_ExceptionHandling\PasswordGUI\data.json", "r") as f:
                
                try:
                    # Dumping the data into a ,json file
                    current_data = json.load(f)
                    if website in current_data:
                        messagebox.showerror(
                            title = "Error!",
                            message = "Site already exists."
                        )
                        return
                except json.decoder.JSONDecodeError:
                    pass
                else:
                    data.update(current_data) # Adding all the file's data into data
                            
            with open(r"30_ExceptionHandling\PasswordGUI\data.json", "w") as f:
                
                json.dump(data, f, indent = 4)
                # f.write(f"{website} | {username} | {password}\n")
                
                entry_website.delete(0, END)
                entry_password.delete(0, END)
                
                entry_website.config(highlightthickness = 0)
                entry_name.config(highlightthickness = 0)
                entry_password.config(highlightthickness = 0)
                
                messagebox.showinfo(
                    title = "Success!", 
                    message = f"Password for {website} saved successfully."
                )
                
        except OSError:
            with open(r"30_ExceptionHandling\PasswordGUI\data.json", "w") as f:
                
                json.dump(data, f, indent = 4)
                
                entry_website.delete(0, END)
                entry_password.delete(0, END)
                
                entry_website.config(highlightthickness = 0)
                entry_name.config(highlightthickness = 0)
                entry_password.config(highlightthickness = 0)
                
                messagebox.showinfo(
                    title = "Success!", 
                    message = f"Password for {website} saved successfully."
                )

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Crapword Manager")
window.config(
    padx = 20, pady = 20,
    bg = "white"
)

# Logo + Canvas
image_logo = PhotoImage(file = r"30_ExceptionHandling\PasswordGUI\logo.png")
canvas = Canvas(
    width = 200, height = 200,
    bg = "white",
    highlightthickness = 0
)
canvas.create_image(
    100, 100,
    image = image_logo
)

canvas.grid(
    row = 0, column = 1
)

## Labels
label_website = Label(text = "Website:", font = (FONT_NAME, 10, "normal"), bg = "white")
label_name = Label(text = "Email/Username:", font = (FONT_NAME, 10, "normal"), bg = "white")
label_password = Label(text = "Password:", font = (FONT_NAME, 10, "normal"), bg = "white")

label_website.grid(row = 1, column = 0)
label_name.grid(row = 2, column = 0)
label_password.grid(row = 3, column = 0)

## Entries
entry_website = Entry()
entry_website.focus() # So less clicks are needed. Magic!
entry_name = Entry()
entry_name.insert(0, USUAL_EMAIL)
entry_password = Entry()

entry_website.grid(row = 1, column = 1, columnspan = 2, sticky = "EW", padx = (10, 10))
entry_name.grid(row = 2, column = 1, columnspan = 2, sticky = "EW", padx = (10, 10))
entry_password.grid(row = 3, column = 1, columnspan = 2, sticky = "EW", padx = (10, 10))

## Buttons
button_generate_pw = Button(text = "Generate password", font = (FONT_NAME, 9, "normal"),
                            command = generate_password)
button_generate_pw.grid(row = 3, column = 2, sticky = "EW", padx = (10, 10))

button_get_login = Button(text = "Search", font = (FONT_NAME, 9, "normal"),
                          command = get_password)
button_get_login.grid(row = 1, column = 2, sticky = "EW", padx = (10, 10))

button_add_to_file = Button(text = "Add to file", font = (FONT_NAME, 9, "normal"),
                            command = save_information_to_file)
button_add_to_file.grid(row = 4, column = 1, columnspan = 2, sticky = "EW", padx = (10, 10))


window.mainloop()