from tkinter import *

# First time doing a program without the main() :(

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Bahnschrift"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# Pomodoro reps tracker
reps = 0

# Global window
timer_window = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    
    # Sets reps to zero
    global reps
    reps = 0
    
    # Stops the timer
    window.after_cancel(timer_window)
    
    # Resets the timer label
    label_timer.config(
        text = "Timer"
    )
    
    # And this resets the actual timer
    canvas.itemconfig(tagOrId = timer_canvas_text, text = f"00:00")

    # Resets the markers
    label_sessions.config(
        text = ""
    )
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def generate_checks(reps: int):
    s = str()
    for i in range(reps // 2):
        s += "✔️"
    return s

def start_timer():
    global reps
    
    # For testing purposes!
    M = 60
    
    if reps > 0 and reps % 8 == 0:
        reps += 1
        label_timer.config(
            text = "BREAK!",
            fg = RED
        )
        count_down(LONG_BREAK_MIN * M)
    elif reps % 2 == 0:
        reps += 1
        label_timer.config(
            text = "WORK!",
            fg = GREEN
        )
        count_down(WORK_MIN * M)
    else:
        reps += 1
        label_sessions.config(
            text = generate_checks(reps)
        )
        label_timer.config(
            text = "BREAK!",
            fg = PINK
        )
        count_down(SHORT_BREAK_MIN * M)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# Recursion!!!
def count_down(count):
    
    # Alternative formatting:
    # m = count // 60
    # s = count % 60
    # if s < 10:
    #    s = f"0{s}"
    # if m < 10:
    #    m = f"0{m}"
    
    canvas.itemconfig(tagOrId = timer_canvas_text, text = f"{str(count // 60).zfill(2)}:{str(count % 60).zfill(2)}")
    if count > 0:
        global timer_window
        timer_window = window.after(10, count_down, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Crappydoro")
window.config(
    padx = 60, pady = 50,
    bg = YELLOW
)

# PhotoImage: get hold of a particular image
tomato_image = PhotoImage(file = r"28_PomodoroGUI/tomato.png")

# Canvas?
canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0)
canvas.create_image(
    100, 112,
    image = tomato_image
)

timer_canvas_text = canvas.create_text(
    100, 132,
    text = "00:00",
    fill = "white",
    font = (FONT_NAME, 32, "bold")
)
canvas.grid(row = 2, column = 1, rowspan = 3)

# Create buttons for start and finish
button_start = Button(text = "Start", font = (FONT_NAME, 12, "normal"), width = 5,
                      command = start_timer)
button_reset = Button(text = "Reset", font = (FONT_NAME, 12, "normal"), width = 5,
                      command = reset_timer)

# padx is important to make some padding!
button_start.grid(row = 2, column = 0, padx = 20)
button_reset.grid(row = 4, column = 0, padx = 20)


# Create label for session tracker
label_timer = Label(text = "LSFL Timer", font = (FONT_NAME, 30, "normal"), fg = GREEN, bg = YELLOW)
label_timer.grid(row = 0, column = 1)

label_sessions = Label(text = "", font = (FONT_NAME, 12, "normal"), fg = GREEN, bg = YELLOW)
label_sessions.grid(row = 5, column = 1)

# Create more buttons for different timers. Maybe even add an entry?

window.mainloop()