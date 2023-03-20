from turtle import Turtle

WINDOW_WIDTH = 960
WINDOW_HEIGHT = 640
OFFSET = 20
MOVE_STEP = 4

PADDLE_WIDTH = 20 # ?
PADDLE_HEIGHT = 180 # ?

class Paddle(Turtle):
    
    # Initialization
    def __init__(self) -> None:
        
        # Inheritance
        super().__init__()
        
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
        
        self.shapesize(stretch_len = 1.0, stretch_wid = 9.0)
        self.setpos(-WINDOW_WIDTH * 0.5 + OFFSET, 0)

    # Add safeguards to avoid going too high up
    # But fucking how, though
    
    def press_paddle_up(self):
        self.sety(self.ycor() + MOVE_STEP)
        
    def release_paddle_up(self):
        return
    
    def press_paddle_down(self):
        self.sety(self.ycor() - MOVE_STEP)
        
    def release_paddle_down(self):
        return
    