from turtle import Turtle, Screen
from prettytable import PrettyTable
# Alternative: import Turtle

def main():
    
    # Constructing an object
    tartas = Turtle()
    tartas.shape("arrow")
    tartas.color("black")
    my_screen = Screen()
    # Alternative: tartas = turtle;Turtle()
    
#    draw_polygon(tartas, 8)
    pretty_table()
    
    my_screen.exitonclick()

def draw_polygon(turtle: Turtle, sides: int) -> None:
    for i in range(sides):
        turtle.forward(40)
        turtle.left(360 / sides)
        turtle.dot(4, "red")

def pretty_table():
    table = PrettyTable(["Pokémon Name", "Type"])
    table.add_row(["Pikachu", "Electric"])
    table.add_row(["Squrtle", "Water"])
    table.add_row(["Charmander", "Fire"])
    
    table.align = "l"
    print(table)

main()