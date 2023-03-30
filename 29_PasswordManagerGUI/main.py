from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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

canvas.pack()

window.mainloop()