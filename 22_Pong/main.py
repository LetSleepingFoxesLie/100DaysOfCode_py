from turtle import Turtle, Screen
from time import sleep

from paddle import Paddle
from ball import Ball

WINDOW_WIDTH = 960
WINDOW_HEIGHT = 640

WINDOW_WIDTH = 960
WINDOW_HEIGHT = 640
OFFSET = 20
MOVE_STEP = 12

def main():
    
    # Screen initialization
    screen = Screen()
    setup_screen(screen)
    
    # Create paddles
    paddle_player_a = Paddle(-WINDOW_WIDTH * 0.5 + OFFSET, 0)
    paddle_player_b = Paddle(WINDOW_WIDTH * 0.5 - OFFSET, 0)
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
    
    # Paddle B
    screen.onkeypress(fun = paddle_player_b.press_paddle_down, key = "Down")
    screen.onkeypress(fun = paddle_player_b.press_paddle_up, key = "Up")
    
    screen.onkeyrelease(fun = paddle_player_b.release_paddle_down, key = "Down")
    screen.onkeyrelease(fun = paddle_player_b.release_paddle_up, key = "Up")
    
    is_game_running = True
    while is_game_running:
        screen.update()
        
        # Test for balls
        ball.bounce_top_bottom()
        ball.bounce_paddle(paddle_player_a)
        ball.bounce_paddle(paddle_player_b)
        
        # Loop ball movement
        ball.ball_movement()
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