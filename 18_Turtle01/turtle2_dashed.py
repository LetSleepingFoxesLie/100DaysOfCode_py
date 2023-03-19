from turtle import Turtle, Screen

def main():
    turtle = Turtle()
    screen = Screen()

    turtle.color("chartreuse")
    turtle.pensize(3)
    
    dashed_line(turtle, screen, 10)
    
    screen.exitonclick()
    return

def dashed_line(turtle: Turtle, screen: Screen, length: int) -> None:
    turtle.penup()
    turtle.setpos(-400, 000)
    turtle.setheading(0)
    
    index = 0
    
    while(turtle.xcor() + float(length) < screen.window_width()):
        turtle.penup() if index % 2 == 0 else turtle.pendown()
        turtle.forward(length)
        index += 1
        
    return

main()