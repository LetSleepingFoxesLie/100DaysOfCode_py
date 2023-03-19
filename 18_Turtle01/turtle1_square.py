from turtle import Turtle, Screen

def main():
    turtle = Turtle()
    screen = Screen()
    turtle.color("chartreuse")
    turtle.pensize(3)
    
    make_square(turtle, screen, 100)
    
    screen.exitonclick()
    return

def make_square(turtle: Turtle, screen: Screen, length: int) -> None:
    for i in range(4):
        turtle.forward(length)
        turtle.left(90)
    return

main()