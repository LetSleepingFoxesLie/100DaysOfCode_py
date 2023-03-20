from turtle import Turtle

WINDOW_WIDTH = 960
WINDOW_HEIGHT = 640
OFFSET = 20
MOVE_STEP = 12

PADDLE_WIDTH = 20 # ?
PADDLE_HEIGHT = 180 # ?

UPPER_BOUND = 230
LOWER_BOUND = -224

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
        current_y = self.ycor()
        if current_y + MOVE_STEP >= UPPER_BOUND:
            return
        else:
            self.sety(self.ycor() + MOVE_STEP)
        
    def release_paddle_up(self):
        return
    
    def press_paddle_down(self):
        current_y = self.ycor()
        if current_y - MOVE_STEP <= LOWER_BOUND:
            return
        else:
            self.sety(self.ycor() - MOVE_STEP)
        
    def release_paddle_down(self):
        return
    