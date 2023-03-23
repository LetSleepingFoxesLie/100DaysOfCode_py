import time
from random import randint

from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


def main():
    
    # Setting up the screen
    screen = Screen()
    screen.setup(width = 600, height = 600)
    screen.colormode(255)
    screen.bgcolor("white")
    screen.title("1-digit budget Frogger clone")
    screen.tracer(0)
    
    # Setting up the player
    player = Player()
    
    # Setting up the scoreboard
    scoreboard = Scoreboard()
    scoreboard.draw_scoreboard()
    
    # Setting up the car movements
    car_manager = CarManager()
    car_manager.generate_car(level = scoreboard.score)

    # Listening for events
    screen.listen()
    screen.onkey(fun = player.move_backward, key = "s")
    screen.onkey(fun = player.move_backward, key = "Down")
    screen.onkey(fun = player.move_forward, key = "w")
    screen.onkey(fun = player.move_forward, key = "Up")
    
    while True:
        time.sleep(0.016)
        
        # Adding some in-loop randpm generation of cars.
        # All in all, it spawns cars much faster the higher level you go, up to a cap
        # of around 15 cars per second. That's still a lot.
        if randint(0, max(3, int(9 - 0.6 * scoreboard.score))) == 0:
            car_manager.generate_car(level = scoreboard.score)
            
        # Moves the cars with every game tick
        car_manager.process_car_movement(level = scoreboard.score)
        
        # After all calculations have been done, update the screen
        screen.update()
        
        # It's important to only check for collision and other in-game conditions
        # only after the game screen has been updated. This guarantees the user
        # won't get flabbergasted out of the blue.
        
        # Check for collisions
        if player.has_been_hit(car_manager.car_list):
            break
        
        # Check for level advancement
        # Originally, everything would be in this if, but I decided to move everything
        # to player.py and handle everything in there.
        if player.is_player_next_level(scoreboard, car_manager):
            continue
    
    screen.exitonclick()
    
main()