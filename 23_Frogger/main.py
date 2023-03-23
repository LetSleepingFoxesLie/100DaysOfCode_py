import time
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
    screen.title("2-digit budget Frogger clone")
    screen.tracer(0)
    
    # Setting up the car movements
    car_manager = CarManager()

    # Setting up the player
    player = Player()
    
    # Setting up the scoreboard
    scoreboard = Scoreboard()
    scoreboard.draw_scoreboard()
    
    # Listening for events
    screen.listen()
    screen.onkey(fun = player.move_backward, key = "s")
    screen.onkey(fun = player.move_forward, key = "w")
    
    while True:
        time.sleep(0.016)
        car_manager.generate_car()
        car_manager.process_car_movement()
        screen.update()
        
        # Lastly, check for collisions
        if player.has_been_hit(car_manager.car_list):
            break
    
    screen.exitonclick()
    
main()