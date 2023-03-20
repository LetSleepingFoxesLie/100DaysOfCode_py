from turtle import Turtle

WINDOW_WIDTH = 960
WINDOW_HEIGHT = 640
OFFSET = 20
MOVE_STEP = 20

# Upper and lower bound to limit the paddle's movement in some way.
UPPER_BOUND = 230
LOWER_BOUND = -224

class Paddle(Turtle):
    
    # Initialization
    def __init__(self, starting_x: int, starting_y: int) -> None:
        
        # Inheritance
        super().__init__()
        
        # Setting the paddles up
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
        
        self.shapesize(stretch_len = 1.0, stretch_wid = 9.0)
        self.setpos(starting_x, starting_y)

    # Add safeguards to avoid going too high up
    # But fucking how, though
    
    # Ok, so managed to limit the movement of the paddles through spaghetti code.
    # Here's hoping it will never blow up (it will blow up)
    
    def press_paddle_up(self) -> None:
        current_y = self.ycor()
        if current_y + MOVE_STEP >= UPPER_BOUND:
            return
        else:
            self.sety(self.ycor() + MOVE_STEP)
        
    def release_paddle_up(self) -> None:
        return
    
    def press_paddle_down(self) -> None:
        current_y = self.ycor()
        if current_y - MOVE_STEP <= LOWER_BOUND:
            return
        else:
            self.sety(self.ycor() - MOVE_STEP)
        
    def release_paddle_down(self) -> None:
        return
    