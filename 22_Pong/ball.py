from turtle import Turtle
from paddle import Paddle
from random import randint

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
    
    def is_out_of_bounds(self):
        cx = self.xcor()
        cy = self.ycor()
        pass