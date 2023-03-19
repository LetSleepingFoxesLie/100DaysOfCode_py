import colorgram
from colorgram import Color
from turtle import Turtle, Screen
from random import choice

SCREEN_SIZE = 800

def main():
#    hirst_input = "18_Turtle01\hirst.jpg"
#    print(get_color_palette(hirst_input, 25))
    color_list = [(207, 160, 82), (54, 88, 130), (145, 91, 40), (140, 26, 49), (221, 207, 105), (132, 177, 203), (158, 46, 83), (45, 55, 104), (169, 160, 39), (129, 189, 143), (83, 20, 44), (37, 43, 67), (186, 94, 107), (187, 140, 170), (85, 120, 180), (59, 39, 31), (88, 157, 92), (78, 153, 165), (194, 79, 73), (45, 74, 78), (80, 74, 44)]
    screen = Screen()
    screen.screensize(SCREEN_SIZE, SCREEN_SIZE)
    turtle = Turtle()
    
    screen.colormode(255)
    turtle.speed(0)
    turtle.penup()
    
    hirst_blots(turtle=turtle, number_of_blots=16, padding=30, available_colors=color_list)
    
    screen.exitonclick()
    return

def hirst_blots(turtle: Turtle, number_of_blots: int, padding: int, available_colors: list) -> None:
    
    # Bounds of x
    lbx = -SCREEN_SIZE * 0.5 + padding
    hbx = SCREEN_SIZE * 0.5 - padding
    
    # Bounds of y
    lby = -SCREEN_SIZE * 0.5 + padding
    hby = SCREEN_SIZE * 0.5 - padding
    
    # Setting start position
    turtle.setx(lbx)
    
    # Iterating to create the Hirst blog painting
    for y in range(number_of_blots):
        
        # We need to reset the Turtle every time
        turtle.setx(lbx)
        
        # I'm just dynamically calculating the distance between each blot
        turtle.sety(lby + y * ((hby - lby) / number_of_blots))
        
        # Setting the angle 
        turtle.seth(0)
        
        # We'll do it row by row
        for x in range(number_of_blots):
            turtle.dot(20, choice(available_colors))
            turtle.forward((hbx - lbx) / number_of_blots)
            

def get_color_palette(file_location: str, number_of_colors: int) -> list:
    colors = colorgram.extract(file_location, number_of_colors)
    color_list = []
    
    for c in colors:
        color_list.append((c.rgb.r, c.rgb.g, c.rgb. b))
    return color_list

main()