from turtle import Turtle, Screen
from time import sleep

from paddle_left import PaddleLeft
from ball import Ball

WINDOW_WIDTH = 960
WINDOW_HEIGHT = 640

def main():
    
    # Screen initialization
    screen = Screen()
    setup_screen(screen)
    
    # Create paddles
    paddle_player_a = PaddleLeft()
    screen.update()
    
    # Create ball
    ball = Ball()
    
    # Add listeners
    screen.listen()
    
    # Paddle A
    screen.onkeypress(fun = paddle_player_a.press_paddle_down, key = "s")
    screen.onkeypress(fun = paddle_player_a.press_paddle_up, key = "w")
    
    screen.onkeyrelease(fun = paddle_player_a.release_paddle_up, key = "s")
    screen.onkeyrelease(fun = paddle_player_a.release_paddle_up, key = "w")
    
    is_game_running = True
    while is_game_running:
        screen.update()
        sleep(0.02)
    
    screen.exitonclick()
    # game loop
    pass

def setup_screen(screen: Screen) -> None:
    screen.setup(width = WINDOW_WIDTH, height = WINDOW_HEIGHT)
    screen.colormode(255)
    screen.bgcolor("black")
    screen.title("WCAP - Whatever Comes After Ping!")
    screen.tracer(0)
    
main()