from turtle import Turtle
from random import choice, randint

COLORS = ["firebrick", "sienna", "goldenrod", "green", "steel blue", "dark slate blue"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 4

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600
SPAWNABLE_AREA_DIFFERENCE = 80

class CarManager:
    
    def __init__(self):
        
        self.car_list = list()
        
        
    def generate_car(self) -> None:
        
        car = Turtle()
        
        # Car visuals
        car.penup()
        car.shape("square")
        car.shapesize(stretch_len = 3.0, stretch_wid = 1.0)
        car.color(choice(COLORS))
        car.speed(0)
        
        # Car settings (mechanics)
        car.setheading(180)
        car.setpos(360, randint(
            - WINDOW_HEIGHT / 2 + SPAWNABLE_AREA_DIFFERENCE,
            WINDOW_HEIGHT / 2 - SPAWNABLE_AREA_DIFFERENCE)
        )
        
        self.car_list.append(car)
        
    def process_car_movement(self, level: int) -> None:
        for car in self.car_list:
            car.setx(car.xcor() - (MOVE_INCREMENT + level))

            # Detect when out of bounds
            if car.xcor() >= 360 or car.xcor() <= -360:
                car.clear()
                car.hideturtle()
                self.car_list.remove(car)