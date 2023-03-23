from turtle import Turtle
from scoreboard import Scoreboard
from car_manager import CarManager

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280

class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        
        # Turtle's variables
        self.speed = 0
        
        # Setup the turtle's visuals!
        self.penup()
        self.seth(90)
        self.shape("square") # Decided to make it a square
        self.color("black")
        self.setpos(STARTING_POSITION)
    
    # Keyboard controls
    def move_forward(self) -> None:
        self.sety(self.ycor() + MOVE_DISTANCE)
    
    def move_backward(self) -> None:
        if self.ycor() <= -280:
            return
        self.sety(self.ycor() - MOVE_DISTANCE)
    
    # Detects whether the player has been hit or not.
    def has_been_hit(self, car_list: list) -> bool:
        for car in car_list:
            
            # As we're dealing with purely square elements, it should be far more performant
            # to use the absolute value of sums and differences than use turtle.distance(),
            # which likely uses a sqrt() to calculate the distance between the two centers.
            if abs(self.xcor() - car.xcor()) <= 36 and abs(self.ycor() - car.ycor()) < 20:
                print(f"{self.pos()} -> {car.pos()}")
                return True
        return False
    
    # Checks whether the player has reached the next level
    def is_player_next_level(self, scoreboard: Scoreboard, car_manager: CarManager) -> bool:
        if self.ycor() >= FINISH_LINE_Y:
            scoreboard.add_score()
            self.setpos(STARTING_POSITION)
            return True
        return False
