from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.qb = quiz_brain
        
        self.window = Tk()
        self.window.title("CrapQuiz, but with API and GUIs")
        self.window.config(
            padx = 20, pady = 20,
            bg = THEME_COLOR
        )
        
        self.score = 0
        self.score_label = Label()
        self.score_label.grid(row = 0, column = 1, padx = 20, pady = 20)
        self.score_label.config(
            text = f"Score: {self.score}",
            bg = THEME_COLOR,
            fg = "white"
        )
        
        self.canvas = Canvas(
            width = 300, height = 250,
            bg = "white",
            highlightthickness = 0
        )
        
        self.question_text = self.canvas.create_text(
            150, 125,
            width = 280,
            fill = "black",
            text = "Hello!",
            justify = "center",
            font = ("Bahnschrift", 16, "italic")
        )
        
        self.canvas.grid(row = 1, column = 0, columnspan = 2, padx = 20, pady = 20)
        
        # Buttons!
        self.image_true = PhotoImage(file = r"34_API_Quiz\images\true.png")
        self.image_false = PhotoImage(file = r"34_API_Quiz\images\false.png")
        
        self.button_true = Button(
            width = 100, height = 100,
            padx = 20, pady = 20,
            image = self.image_true,
            highlightthickness = 0,
            background = THEME_COLOR,
            relief = "flat",
            command = self.guess_true
        )
        self.button_true.config(borderwidth = 0)
        self.button_true.grid(row = 2, column = 0)
        
        self.button_false = Button(
            width = 100, height = 100,
            padx = 20, pady = 20,
            image = self.image_false,
            highlightthickness = 0,
            background = THEME_COLOR,
            relief = "flat",
            command = self.guess_false
        )
        self.button_false.config(borderwidth = 0)
        self.button_false.grid(row = 2, column = 1)

        self.get_next_question()
        
        self.window.mainloop()
        
    
    def get_next_question(self):
        self.canvas.config(bg = "white")
        if self.qb.still_has_questions():
            self.score_label.config(
                text = f"Score: {self.qb.score}"
            )
            q_text = self.qb.next_question()
            self.canvas.itemconfig(
                tagOrId = self.question_text,
                text = q_text
            )
        else:
            self.canvas.itemconfig(self.question_text, text = "Quiz is over!")
            self.button_false.config(state = "disabled")
            self.button_true.config(state = "disabled")
    
    def guess_true(self):
        is_right = self.qb.check_answer("true")
        self.flash_screen(is_right)
        
    def guess_false(self):
        is_right = self.qb.check_answer("false")
        self.flash_screen(is_right)
        
    def update_score(self):
        self.score_label.config(text = f"Score: {self.qb.score}")
    
    def flash_screen(self, is_right: bool):
        if is_right:
            self.canvas.config(bg = "lime")
        else:
            self.canvas.config(bg = "red")
        self.window.after(500, self.get_next_question)
    