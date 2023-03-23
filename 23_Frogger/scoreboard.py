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
        
    # Draws the scoreboard
    def draw_scoreboard(self):
        self.clear()
        self.write(arg = f"Level: {self.score + 1}", move = False, align = "center", font = FONT)
    
    # Adds one to score. This can only be triggered by reaching the "end" in every level
    def add_score(self):
        self.score += 1
        self.draw_scoreboard()