from turtle import Turtle, Screen
from random import randint

def main():
    turtle = Turtle()
    screen = Screen()
    
    turtle.pensize(5)
    turtle.speed(0)
    screen.colormode(255)
    
    turtle.penup()
    turtle.goto(0, -200)
    turtle.pendown()
    
    draw_fake_spirograph(turtle, screen, 30, 50)
    
    screen.exitonclick()
    return

def draw_fake_spirograph(turtle: Turtle, screen: Screen, circles: int, inner_radius: int) -> None:
    turtle.tilt(0)
    for i in range(circles):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        
        turtle.color(r, g, b)
        turtle.circle(150)
        
        turtle.forward(inner_radius)
        turtle.left(360 / circles)
        # turtle.settiltangle(i * (360 / circles))
        
main()