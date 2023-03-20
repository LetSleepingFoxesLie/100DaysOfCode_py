from turtle import Turtle
from paddle import Paddle
from scoreboard import Scoreboard

from random import randint
from time import sleep

BALL_RADIUS = 10 # supposedly 10
BALL_SPEED = 10

WINDOW_WIDTH = 960
WINDOW_HEIGHT = 640

class Ball(Turtle):
    
    def __init__(self) -> None:
        
        super().__init__()
        
        self.angle = randint(0, 360)
        self.ball_set_angle(self.angle)
        
        self.penup()
        self.shape("circle")
        self.color("turquoise")
        self.speed(0)
        
    # Ball movement
    def ball_movement(self) -> None:
        self.forward(BALL_SPEED)
        
    # Regenerate the ball
    def regenerate_ball(self) -> None:
        self.setpos(0, 0)
        self.seth(randint(0, 360))
    
    # Ball set angle
    def ball_set_angle(self, angle: int) -> None:
        self.seth(angle)
        
    def bounce_top_bottom(self) -> None:
        cy = self.ycor()
        
        # Check for upper boundary...
        if cy + BALL_RADIUS >= WINDOW_HEIGHT * 0.5 or cy - BALL_RADIUS <= -WINDOW_HEIGHT * 0.5:
            self.angle = 360 - self.angle
            self.ball_set_angle(self.angle)
    
    def bounce_paddle(self, paddle: Paddle) -> None:
        PADDLE_OFFSET = 40
        PADDLE_RANGE = 180 * 0.5
        
        cx = self.xcor()
        cy = self.ycor()
        
        # Testing for left paddle
        if cx <= -WINDOW_WIDTH * 0.5 + PADDLE_OFFSET and (cy >= paddle.ycor() - PADDLE_RANGE and cy <= paddle.ycor() + PADDLE_RANGE):
            self.angle = 180 - self.angle
            self.ball_set_angle(self.angle)
        
        # Testing for right paddle
        if cx >= WINDOW_WIDTH * 0.5 - PADDLE_OFFSET and (cy >= paddle.ycor() - PADDLE_RANGE and cy <= paddle.ycor() + PADDLE_RANGE):
            self.angle = 180 - self.angle
            self.ball_set_angle(self.angle)
    
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
            