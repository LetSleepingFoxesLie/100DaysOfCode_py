from turtle import Turtle

WINDOW_WIDTH = 960
WINDOW_HEIGHT = 640
OFFSET = 20
MOVE_STEP = 10

class Paddle(Turtle):
    
    # Initialization
    def __init__(self) -> None:
        
        # Inheritance
        super().__init__()
        
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
        
        print("!")
        
        self.shapesize(stretch_len = 1.0, stretch_wid = 15.0)
        self.setpos(-WINDOW_WIDTH * 0.5 + OFFSET, 0)

    # Add safeguards to avoid going too high up        
    def move_paddle_up(self):
        self.sety(self.ycor() + MOVE_STEP)
        
    def move_paddle_down(self):
        self.sety(self.ycor() - MOVE_STEP)