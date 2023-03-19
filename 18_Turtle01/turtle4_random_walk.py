from turtle import Turtle, Screen
from random import randint

def main():
    turtle = Turtle()
    screen = Screen()
    
    turtle.pensize(5)
    turtle.speed(10)
    screen.colormode(255)
    
    random_walk(turtle, screen)
    
    screen.exitonclick()
    return

def random_walk(turtle: Turtle, screen: Screen) -> None:
    for i in range(500):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        
        turtle.color(r, g, b)
        
        direction = randint(0, 3)
        turtle.forward(12)
        turtle.left(direction * 90)
main()