from turtle import Turtle

FONT = ("Bahnschrift", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        
        # Initializing setup!
        self.score = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.setpos(-225, 250)
        
        self.draw_scoreboard()
        
    
    def draw_scoreboard(self):
        self.clear()
        self.write(arg = f"Level: {self.score}", move = False, align = "center", font = FONT)
    
    def add_score(self):
        self.score += 1