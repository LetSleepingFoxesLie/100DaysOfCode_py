from tkinter import *
from random import choice
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
BUTTON_ACTIVE_COLOR = "#A1CDB6"
FRENCH_WORDS = r"31_Flashcards/data/french_word.csv"

FONT_SMALL = ("Bahnschrift", 40, "normal")
FONT_BIG = ("Bahnschrift", 60, "bold")
c = None # Our global variable... I guess?
window_flip = None

# Get dictionary:
def create_dictionary() -> dict:
    try:
        with open(r"31_Flashcards\data\french_words.csv", "r", encoding = "utf-8") as f:
            data = pd.read_csv(f).to_dict(orient = "records")
    except FileNotFoundError:
        print("Foda...")
    finally:
        return [{key["French"]: key["English"]} for key in data]

def flip_card() -> None:
    
    global c
    en = ''.join(list(c.values()))
    
    # After 3 seconds, flash the flashcard!
    flashcard_canvas.itemconfig(
        tagOrId = flashcard_language_text,
        text = "English",
        fill = "white"
    )
    
    flashcard_canvas.itemconfig(
        tagOrId = flashcard_translation_text,
        text = en,
        fill = "white"
    )
    
    flashcard_canvas.itemconfig(
        tagOrId = flashcard_background,
        image = FLASHCARD_BACK
    )

def get_list_of_known_words() -> list:
    try:
        with open(r"31_Flashcards\data\known_words.txt", "r", encoding = "utf-8") as f:
            data = f.readlines()
            d = [w.strip("\n") for w in data]
            return d
    except FileNotFoundError:
        print("File was not found!")
        return list()

def clear_dict() -> list:
    global c
    fr = ''.join(list(c.keys()))
    
    for pair in word_dictionary:
        if fr in pair:
            del pair[fr]
            break
    return [word for word in word_dictionary if word]

def right_tick() -> None:
    global c, word_dictionary
    fr = ''.join(list(c.keys()))
    
    try:
        with open(r"31_Flashcards\data\known_words.txt", "a", encoding = "utf-8") as f:
            f.write(f"{fr}\n")
    except FileNotFoundError:
        with open(r"31_Flashcards\data\known_words.txt", "w", encoding = "utf-8") as f:
            right_tick()
    finally:
        word_dictionary = clear_dict()
        generate_new_word()
            
def generate_new_word() -> None:
    global c, window_flip
    
    # Cancel flipping
    if window_flip is None:
        pass
    else:
        window.after_cancel(window_flip)
    
    # Get random {fr:en} pair    
    print(len(word_dictionary))
    c = choice(word_dictionary)
    
    # Make strings out of those keys and vlaues
    fr = ''.join(list(c.keys()))

    # Checks if word is already known
    if fr in get_list_of_known_words():
        print(f"{fr} is already known!")
        generate_new_word()
    
    # print(f"{fr}: {en}")
    
    # Update our test in canvas!
    flashcard_canvas.itemconfig(
        tagOrId = flashcard_translation_text,
        text = fr,
        fill = "black"
    )
    
    flashcard_canvas.itemconfig(
        tagOrId = flashcard_language_text,
        text = "Français",
        fill = "black"
    )
    
    flashcard_canvas.itemconfig(
        tagOrId = flashcard_background,
        image = FLASHCARD_FRONT
    )
    
    window_flip = window.after(ms = 3000, func = flip_card)
    
# Generate the dictionary
word_dictionary = create_dictionary()
word_dictionary = clear_dict()

# Create the GUI
window = Tk()
window.title("Not-so-flashy flashcards")
window.config(
    width = 900,
    height = 626,
    padx = 50,
    pady = 50,
    bg = BACKGROUND_COLOR
)

# I apparently can't use these as a constant before creating the window :)
FLASHCARD_FRONT = PhotoImage(file = r"31_Flashcards/images/card_front.png")
FLASHCARD_BACK = PhotoImage(file = r"31_Flashcards/images/card_back.png")

# Create the canvas on which everything will be shown
flashcard_canvas = Canvas(
    width = 800,
    height = 526,
    highlightthickness = 0,
    background = BACKGROUND_COLOR
)

flashcard_background = flashcard_canvas.create_image(
    400, 263,
    image = FLASHCARD_FRONT
)

flashcard_language_text = flashcard_canvas.create_text(
    400, 150,
    text = "French",
    font = FONT_SMALL
)

flashcard_translation_text = flashcard_canvas.create_text(
    400, 283,
    text = "Palavre",
    font = FONT_BIG
)

flashcard_canvas.grid(row = 0, column = 0, columnspan = 2)

# Buttons

image_cross = PhotoImage(file = r"31_Flashcards/images/wrong.png")
image_tick = PhotoImage(file = r"31_Flashcards/images/right.png")

button_cross = Button(
    width = 97, height = 95,
    image = image_cross,
    highlightthickness = 0,
    background = BACKGROUND_COLOR,
    activebackground = BUTTON_ACTIVE_COLOR,
    relief = "flat",
    command = generate_new_word
)

button_cross.config(borderwidth = 0)

button_cross.grid(
    row = 1, column = 0
)

button_tick = Button(
    width = 97, height = 95,
    image = image_tick,
    highlightthickness = 0,
    background = BACKGROUND_COLOR,
    activebackground = BUTTON_ACTIVE_COLOR,
    relief = "flat",
    command = right_tick
)

button_tick.config(borderwidth = 0)

button_tick.grid(
    row = 1, column = 1
)

generate_new_word()

window.mainloop()