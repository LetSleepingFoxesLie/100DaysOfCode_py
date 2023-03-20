from turtle import Turtle, Screen
from random import randint

def main():
    #turtle = Turtle()
    screen = Screen()
    
    screen.colormode(255)
    screen.setup(width=500, height=400)
    # user_amount = int(screen.textinput("Turtle Crap Race", "How many turtles should compete? "))
    user_bet = int(screen.textinput("Turtle Crap Race", "Who will win this shit race? "))
    turtle_list = generate_and_prime_turtles(7)
    
    winner_turtle = simulate_turtle_race(turtle_list=turtle_list, max_step=20) + 1
    if winner_turtle == user_bet:
        print(f"You won! Turtle #{winner_turtle} was the winning one.")
    else:
        print(f"You lost! Turtle #{winner_turtle} was the winning one.")
        
    screen.exitonclick()
    
def generate_and_prime_turtles(amount: int) -> list:
    l = list()
    for i in range(amount):
        l.append(Turtle(shape="turtle"))
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        t = (r, g, b)
        
        l[i].color(t)
        l[i].pencolor(t)
        l[i].pensize(5)
    
    turtle_separation = int(300 / amount)
    
    for i in range(amount):
        l[i].goto(-230, 150 - 50 * i)
        
    return l

def simulate_turtle_race(turtle_list: list, max_step: int) -> int:
    index = 0
    
    while True:
        index = 0
        for turtle in turtle_list:
            turtle.clear()
            if turtle.xcor() >= 230:
                return index
            else:
                turtle.forward(randint(0, max_step))
            index += 1


main()