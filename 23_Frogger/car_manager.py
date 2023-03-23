from turtle import Turtle
from random import choice, randint

COLORS = ["firebrick", "sienna", "goldenrod", "green", "steel blue", "dark slate blue"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 4

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600
SPAWNABLE_AREA_DIFFERENCE = 60

class CarManager:
    
    def __init__(self):
        self.car_list = list()
        
    # Generates a car
    def generate_car(self, level: int) -> None:
        
        car = Turtle()
        
        # Car visuals
        car.penup()
        car.shape("square")
        car.shapesize(stretch_len = 3.0, stretch_wid = 1.0)
        car.color(choice(COLORS))
        car.speed(0)
        
        # Car settings (mechanics)
        # Adding some randomness to the speed
        if level >= 3:
            car.speed = randint(int(3 + 0.334 * level), 4 + level)
        elif level == 2:
            car.speed = randint(4, 5)
        else:
            car.speed = 4
        
        # Adding some randomness!
        if level >= 3 and randint(0, max(4, 10 - level)) == 0:
            car.setheading(0)
            car.setpos(-360, randint(-11, 12) * 20) # This snippet ensures the end result is a multiple of 20.
        else:
            car.setheading(180)
            car.setpos(360, randint(-11, 12) * 20) # It just feels right to do so!
        
        self.car_list.append(car)
    
    # For every frame, we will have to process the movement of each car.
    # This is the function responsible for taking on this task.
    def process_car_movement(self, level: int) -> None:
        
        # The thing actually processing the cars' movements
        for car in self.car_list:
            if car.heading() == 180:
                car.setx(car.xcor() - car.speed)
            else:
                car.setx(car.xcor() + car.speed)

            # For each car, detect when out of bounds.
            # Using abs() saves me from writing two conditions.
            # I hope this helps with performance.
            if abs(car.xcor()) >= 370:
                car.clear()
                car.hideturtle()
                self.car_list.remove(car)