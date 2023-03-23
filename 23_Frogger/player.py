from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        
        # Turtle's variables
        self.speed = 0
        
        # Setup the turtle's visuals!
        self.penup()
        self.seth(90)
        self.shape("turtle")
        self.color("black")
        self.setpos(STARTING_POSITION)
        
    def move_forward(self) -> None:
        self.sety(self.ycor() + MOVE_DISTANCE)
    
    def move_backward(self) -> None:
        if self.ycor() <= -280:
            return
        self.sety(self.ycor() - MOVE_DISTANCE)
    
    def has_been_hit(self, car_list: list) -> bool:
        for car in car_list:
            if abs(self.xcor() - car.xcor()) <= 40 and abs(self.ycor() - car.ycor()) <= 20:
                print("A")
                return True
        return False
    
    
    pass
