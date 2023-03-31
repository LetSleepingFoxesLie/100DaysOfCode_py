from tkinter import *

FONT_NAME = "Bahnschrift"
USUAL_EMAIL = "someonesemail@provider.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# Get all relevant information and save it to a file
def save_information_to_file():
    try:
        with open(r"29_PasswordManagerGUI/passwords.txt", "a") as f:
            website = entry_website.get()
            username = entry_name.get()
            password = entry_password.get()
            f.write(f"{website} | {username} | {password}")
    except OSError:
        with open(r"29_PasswordManagerGUI/passwords.txt", "w"):
            save_information_to_file()
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Crapword Manager")
window.config(
    padx = 20, pady = 20,
    bg = "white"
)

# Logo + Canvas
image_logo = PhotoImage(file = r"29_PasswordManagerGUI/logo.png")
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
button_generate_pw = Button(text = "Generate password", font = (FONT_NAME, 9, "normal"))
button_generate_pw.grid(row = 3, column = 2, sticky = "EW", padx = (10, 10))

button_add_to_file = Button(text = "Add to file", font = (FONT_NAME, 9, "normal"),
                            command = save_information_to_file)
button_add_to_file.grid(row = 4, column = 1, columnspan = 2, sticky = "EW", padx = (10, 10))


window.mainloop()