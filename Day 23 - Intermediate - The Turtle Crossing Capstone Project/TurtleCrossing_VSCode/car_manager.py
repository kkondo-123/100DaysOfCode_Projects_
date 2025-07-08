"""
Name: Kana Kondo
Date: 2025-07-07-Mon
Course: 100 Days of Code Day 23
Description: Turtle Crossing Game - Car Manager Class
"""

from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
ANGELA_MOVE_INCREMENT = 10
MY_MOVE_INCREMENT = 7
CAR_SHAPE = "square"
STRETCH_LEN = 2
STRETCH_WID = 1
STARTING_X_POS = 300
STARTING_Y_RANGE = (-240, 240)

class CarManager:
    
    # TODO 2: Create cars that are 20px high by 40px wide that are randomly generated along 
    #   the y-axis and move to the left edge of the screen. No cars should be generated 
    #   in the top and bottom 50px of the screen (think of it as a safe zone for our 
    #   little turtle). Hint: generate a new car only every 6th time the game loop runs. 
    #   (Solution = Step 4 Video)

    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
            
    def create_car(self):
        # Angela used random.randint(0, 6) and created car with 1/6 chance -> I think it's a better way to generate cars since it's at random which is better for a game
        if random.randint(0, 6) == 0:
            new_car = Turtle(shape=CAR_SHAPE)
            new_car.penup()
            new_car.shapesize(stretch_len=STRETCH_LEN, stretch_wid=STRETCH_WID)  # length = x axis, width = y axis
            new_car.color(random.choice(COLORS))
            new_car.goto(STARTING_X_POS, random.randint(STARTING_Y_RANGE[0], STARTING_Y_RANGE[1]))  # +/- 10 from 50px safe zone on top and bottom of screen
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.goto(car.xcor() - self.car_speed, car.ycor())
    
    # TODO 3: Detect when the turtle player collides with a car and stop the game 
    # if this happens. (Solution = Step 5 Video)
    def collide_with_player(self, player):
        close_distance = True
        x_collide = True
        y_collide = True

        for car in self.cars:
            close_distance = car.distance(player) < 20
            # Angela did not include x_collide and y_collide.  x_collide and y_collide is accounted for in .distance()
            x_collide = abs(player.xcor() - car.xcor()) < 30  # Player radius = 10px, Car x length from centre = 20px
            y_collide = abs(player.ycor() - car.ycor()) < 20  # Player radius = 10px, Car y width from centre = 10 px
            if close_distance and (x_collide or y_collide):
                return True
            
        return False

    # TODO 4: Increase speed of cars when player reaches top of screen.
    #    Hint: think about creating an attribute and using the MOVE_INCREMENT to 
    #   increase the car speed. 
    def increase_speed(self):
        self.car_speed += MY_MOVE_INCREMENT

