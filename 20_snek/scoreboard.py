from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setpos(0, 270)
        # I should have made some things a constant...
        self.write(arg = f"Current score: {self.score}", move = False, align = "center", font = ("Bahnschrift", 16, "normal"))

    
    # Updates the game score. Needs to be called from the game loop
    def update_score(self):
        self.score += 1
        self.clear()
        self.write(arg = f"Current score: {self.score}", move = False, align = "center", font = ("Bahnschrift", 16, "normal"))

    # Shows the game over screen. Needs to be called from the game loop
    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write(arg = f"GAME OVER", move = False, align = "center", font = ("Bahnschrift", 40, "normal"))