from turtle import Turtle
from paddle import Paddle
from scoreboard import Scoreboard

from random import randint
from time import sleep

BALL_RADIUS = 12 # supposedly 10
BALL_SPEED = 9

WINDOW_WIDTH = 960
WINDOW_HEIGHT = 640

class Ball(Turtle):
    
    def __init__(self) -> None:
        
        super().__init__()
        
        self.sx = randint(2, 7)
        self.sy = randint(2, 4)
        
        if randint(0, 1) % 2 == 0:
            self.sx *= -1
        if randint(0, 1) % 2 == 0:
            self.sy *= -1
        
        self.penup()
        self.shape("circle")
        self.color("turquoise")
        self.speed(0)
        
    # Ball movement
    def ball_movement(self) -> None:
        self.setx(self.xcor() + self.sx)
        self.sety(self.ycor() + self.sy)
        
    # Regenerate the ball
    def regenerate_ball(self) -> None:
        self.setpos(0, 0)
        self.sx = randint(2, 7)
        self.sy = randint(2, 4)
        
        if randint(0, 1) % 2 == 0:
            self.sx *= -1
        if randint(0, 1) % 2 == 0:
            self.sy *= -1
        
    def bounce_top_bottom(self) -> None:
        cy = self.ycor()
        
        # Check for upper boundary...
        if cy + BALL_RADIUS > WINDOW_HEIGHT * 0.5 or cy - BALL_RADIUS < -WINDOW_HEIGHT * 0.5:
            print(f"Top-bottom: {cy}")
            self.sy *= -1
            self.ball_movement()
    
    def bounce_paddle(self, paddle: Paddle) -> None:
        PADDLE_OFFSET = 40
        PADDLE_RANGE = 180 * 0.5
        
        cx = self.xcor()
        cy = self.ycor()
        
        # Testing for left paddle
        if paddle.xcor() < 0:
            if cx <= -WINDOW_WIDTH * 0.5 + PADDLE_OFFSET and (cy >= paddle.ycor() - PADDLE_RANGE and cy <= paddle.ycor() + PADDLE_RANGE):
                print("Left paddle")
                self.sx *= -1
            
        # Testing for right paddle
        if paddle.xcor() > 0:
            if cx >= WINDOW_WIDTH * 0.5 - PADDLE_OFFSET and (cy >= paddle.ycor() - PADDLE_RANGE and cy <= paddle.ycor() + PADDLE_RANGE):
                print("Right paddle")
                self.sx *= -1
    
        self.ball_movement()
            
    def is_out_of_bounds(self, scoreboard_left: Scoreboard, scoreboard_right: Scoreboard):
        cx = self.xcor()
        
        if cx <= -WINDOW_WIDTH * 0.5:
            scoreboard_right.add_score()
            self.regenerate_ball()
            sleep(1)
            
        if cx >= WINDOW_WIDTH * 0.5:
            scoreboard_left.add_score()
            self.regenerate_ball()
            sleep(1)
            