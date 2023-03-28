import tkinter

def main():
    # The window!
    window = tkinter.Tk()
    window.title("Crap program name")
    window.minsize(width = 480, height = 320)
    
    # Labels?
    my_label = tkinter.Label(
        text = "I'm a label!",
        font = (
            "Bahnschrift",
            18,
            "normal"
        )
    )
    my_label.pack()
    
    # Keeps the window on screen. Just like Turtle!
    # Must be at the end
    window.mainloop()
    
main()