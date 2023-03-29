from tkinter import *

def main():
        
    def click_button():
        my_label.config(
            text = my_entry.get()
        )

    # The window!
    window = Tk()
    window.title("Crap program name")
    window.minsize(width = 480, height = 320)
    
    # Labels?
    my_label = Label(
        text = "I'm a label!",
        font = (
            "Bahnschrift",
            18,
            "normal"
        )
    )
    my_label.pack()
    
    # Button!
    my_button = Button(
        text = "+1 click?",
        command = click_button
    )
    my_button.pack()
    
    # Entry!
    my_entry = Entry(
        width = 12
    )
    my_entry.pack()
    
    # Keeps the window on screen. Just like Turtle!
    # Must be at the end
    window.mainloop()

main()