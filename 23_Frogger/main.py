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

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        car_manager.generate_car()
        car_manager.process_car_movement()
        screen.update()
    
    screen.exitonclick()
    
main()