from turtle import Screen
from time import sleep

from snek import Snek
from food import Food
from scoreboard import Scoreboard

APP_WIDTH = 600
APP_HEIGHT = 600

def main():
    
    # Initializing the game's main components
    screen = Screen()
    setup_screen(screen)
    
    snek = Snek()
    food = Food()
    scoreboard = Scoreboard()
    
    # TurtleScreen listener. Hooks 
    screen.listen()
    screen.onkey(fun=snek.snek_move_up, key="Up")
    screen.onkey(fun=snek.snek_move_left, key="Left")
    screen.onkey(fun=snek.snek_move_down, key="Down")
    screen.onkey(fun=snek.snek_move_right, key="Right")
    
    # Game loop
    is_game_on = True
    while is_game_on:
        
        # Update the screen every game tick
        screen.update()
        
        # Move the snake's body
        snek.move_snek_body(snek.segments_list)
        
        # Checks for food
        if is_food_in_contact_with_snek(snek, food):
            scoreboard.update_score()
            #print("Bazinga")
        
        # Checks for "game over" conditions
        if is_snek_out_of_bounds(snek) or has_snek_collided_with_tail(snek):
            #print("You died!")
            scoreboard.game_over()
            is_game_on = False
            
        sleep(0.1)
        
    screen.exitonclick()

# Checks whether the snake if out of bounds
def is_snek_out_of_bounds(snek: Snek) -> bool:    
    return snek.head.xcor() > 280 or snek.head.xcor() < -280 or snek.head.ycor() > 280 or snek.head.ycor() < -280

# Checks whether the snake has collided with its tail
def has_snek_collided_with_tail(snek: Snek) -> bool:
    for segment in snek.segments_list[1:]:
        return snek.head.distance(segment) < 10

# Checks whether the food was eaten by 
def is_food_in_contact_with_snek(snek: Snek, food: Food) -> bool:
    if snek.head.distance(food) < 18:
        food.generate_food()
        snek.extend_snek()
        return True
    else:
        return False

# Sets up the game screen
def setup_screen(screen: Screen) -> None:
    screen.setup(width=APP_WIDTH, height=APP_HEIGHT)
    screen.bgcolor("black")
    screen.title("Snek game! This sucks")
    screen.tracer(0)
    return

main()