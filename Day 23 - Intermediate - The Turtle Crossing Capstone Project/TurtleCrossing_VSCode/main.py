"""
Name: Kana Kondo
Date: 2025-07-07-Mon
Course: 100 Days of Code Day 23
Description: Turtle Crossing Game - Main Class
 1. A turtle moves forwards when you press the "Up" key. 
    It can only move forwards, not back, left or right.
 2. Cars are randomly generated along the y-axis and will move from the 
    right edge of the screen to the left edge.
 3. When the turtle hits the top edge of the screen, it moves back to the original 
    position and the player levels up. On the next level, the car speed increases.
 4. When the turtle collides with a car, it's game over and everything stops.
"""

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

# TODO 1: Create player and listen or the "Up" keypress to move the turtle. 
player = Player()

screen.onkey(player.move, 'Up')

# TODO 2: Create cars using the CarManager class 
cars = CarManager()

# loop_num = 0

# TODO 5: Create scoreboard class to keep track of score. 
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_cars()

    # TODO 3: When the player collides with car, stop the game. 
    if cars.collide_with_player(player):
        game_is_on = False
        score.game_over()

    # TODO 4: When the turtle player reached the top of screen, increase the car speed. 
    #  (Solution = Step 6 Video)
    if player.is_at_goal():
        cars.increase_speed()

        # TODO 5: Increase level when the player makes the goal.
        score.increase_level()

    # if loop_num % 6 == 0:
    #     cars.create_car()
    # loop_num += 1

screen.exitonclick()
