from turtle import Turtle

FONT_SETTINGS = ("Bahnschrift", 32, "normal")
class Scoreboard(Turtle):
    def __init__(self, position: tuple):
        super().__init__()
        
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setpos(position)
        # I should have made some things a constant...
        self.write(arg = self.score, move = False, align = "center", font = FONT_SETTINGS)

        
    def add_score(self):
        self.score += 1
        self.clear()
        self.write(arg = self.score, move = False, align = "center", font = FONT_SETTINGS)

    
    pass