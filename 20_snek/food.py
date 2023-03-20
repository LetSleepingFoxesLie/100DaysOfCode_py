from turtle import Turtle
from random import randint

SCREEN_SIZE = 600
SCREEN_PADDING = 20

class Food(Turtle):
    
    def __init__(self) -> None:
        
        # Inheritance
        super().__init__()
        
        # Due to inheritance, we can access Turtle's methods!
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        
        self.color("turquoise")
        self.speed("fastest")
        self.generate_food()

    # Generates a food Turtle-object within the game window's constraints
    def generate_food(self):
        rx = randint(-SCREEN_SIZE * 0.5 + SCREEN_PADDING, SCREEN_SIZE * 0.5 - SCREEN_PADDING)
        ry = randint(-SCREEN_SIZE * 0.5 + SCREEN_PADDING, SCREEN_SIZE * 0.5 - SCREEN_PADDING)
        
        self.setpos(rx, ry)
        