from tkinter import *

WINDOW_PADDING = 50
WINDOW_HEIGHT = 480
WINDOW_WIDTH = 720

LABEL_PADDING = 20

DEFAULT_FONT = ("Bahnschrift", 18,)

def main():
    
    def convert_m2km():
        MILE = 1.608
        l_converted.config(
            text = f"{float(e_to_be_converted.get()) * MILE:.2f}"
        )
    
    
    # Creating the window
    gui = Tk(screenName = "Sucky Mile2Kilometer Converter")
    
    gui.minsize(
        width = WINDOW_WIDTH,
        height = WINDOW_HEIGHT
    )
    
    gui.config(
        padx = WINDOW_PADDING,
        pady = WINDOW_PADDING
    )
    
    # Creating the labels
    l_miles = Label(
        text = "miles",
        font = DEFAULT_FONT,
        padx = LABEL_PADDING,
        pady = LABEL_PADDING,
    ).grid(
        row = 0,
        column = 2
    )
    
    # Second label
    l_km = Label(
        text = "km",
        font = DEFAULT_FONT,
        padx = LABEL_PADDING,
        pady = LABEL_PADDING,
    ).grid(
        row = 1,
        column = 2
    )
    
    # Another label
    l_is_equal_to = Label(
        text = "is equal to",
        font = DEFAULT_FONT,
        padx = LABEL_PADDING,
        pady = LABEL_PADDING,
    ).grid(
        row = 1,
        column = 0
    )
    
    # The final label: value
    l_converted = Label(
        text = "0",
        font = DEFAULT_FONT,
        padx = LABEL_PADDING,
        pady = LABEL_PADDING,
    )
    
    l_converted.grid(
        row = 1,
        column = 1
    )
    
    b_calculate = Button(
        text = "Convert",
        width = 8,
        font = DEFAULT_FONT,
        padx = LABEL_PADDING,
        pady = LABEL_PADDING,
        command = convert_m2km
    ).grid(
        row = 2,
        column = 1
    )
    
    e_to_be_converted = Entry(
        width = 12,
    )
    
    e_to_be_converted.grid(
        row = 0,
        column = 1
    )
    
    gui.mainloop()

main()