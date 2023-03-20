from turtle import Turtle, Screen

from paddle import Paddle

WINDOW_WIDTH = 960
WINDOW_HEIGHT = 640

def main():
    screen = Screen()
    setup_screen(screen)
    
    paddle_player_a = Paddle()
    screen.update()
    
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