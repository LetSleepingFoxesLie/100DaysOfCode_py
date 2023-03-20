from turtle import Turtle, Screen
from time import sleep

from paddle import Paddle

WINDOW_WIDTH = 960
WINDOW_HEIGHT = 640

def main():
    screen = Screen()
    setup_screen(screen)
    
    # Create paddles
    paddle_player_a = Paddle()
    screen.update()
    
    # Add listeners
    screen.listen()
    screen.onkey(fun = paddle_player_a.move_paddle_down, key = "s")
    screen.onkey(fun = paddle_player_a.move_paddle_up, key = "w")
    
    is_game_running = True
    while is_game_running:
        screen.update()
        sleep(0.1)
    
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