from turtle import Turtle, Screen
# Alternative: import Turtle

def main():
    
    # Constructing an object
    tartas = Turtle()
    tartas.shape("arrow")
    tartas.color("black")
    
    tartas.penup()
    tartas.speed(0)
    tartas.setpos(0, -150)
    tartas.pendown()
    tartas.pensize(2)
    tartas.speed(8)
    
    my_screen = Screen()
    my_screen.colormode(255)
    
    # Alternative: tartas = turtle;Turtle()
    
    for i in range(27):
        tartas.color(160 - 5 * i, 60 + 6 * i, 30 + 8 * i)

        draw_polygon(tartas, 3 + i)

    my_screen.exitonclick()

def draw_polygon(turtle: Turtle, sides: int) -> None:
    for i in range(sides):
        turtle.forward(50)
        turtle.left(360 / sides)
        turtle.dot(5, "purple")
        
main()