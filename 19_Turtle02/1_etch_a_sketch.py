from turtle import Turtle, Screen

TURN_ANGLE = 15
WALK_INCREMENT = 20

def main():
    
    turtle = Turtle()
    screen = Screen()
    turtle.pensize(5)
        
    def key_turn_left() -> None:
        turtle.left(TURN_ANGLE)
        return

    def key_turn_right() -> None:
        turtle.right(TURN_ANGLE)
        return

    def key_move_forward() -> None:
        turtle.forward(WALK_INCREMENT)
        return

    def key_move_backward() -> None:
        turtle.backward(WALK_INCREMENT)
        return

    def key_wipe_canvas() -> None:
        turtle.clear()
        turtle.reset()
        return

    
    screen.onkey(key="Left", fun=key_turn_left)
    screen.onkey(key="Right", fun=key_turn_right)
    screen.onkey(key="Up", fun=key_move_forward)
    screen.onkey(key="Down", fun=key_move_backward)
    screen.onkey(key="space", fun=key_wipe_canvas)
    
    screen.listen()
    
    screen.exitonclick()
    return
    

main()