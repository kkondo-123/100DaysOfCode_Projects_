"""
Name: Kana Kondo
Date: 2025-07-07-Mon
Course: 100 Days of Code Day 23
Description: Turtle Crossing Game - Player Class
"""

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
PLAYER_SHAPE = "turtle"
HEADING_DIRECTION = 90  # North

from turtle import Turtle

class Player(Turtle):
    
    # TODO 1: Create a turtle player that starts at the bottom of the screen and listen 
    #   for the "Up" keypress to move the turtle north. (Solution = Step 3 Video)

    def __init__(self):
        super().__init__()
        self.shape(PLAYER_SHAPE)
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(HEADING_DIRECTION)

    def move(self):
        self.forward(MOVE_DISTANCE)
        
    # TODO 4: Detect when the turtle player has reached the top edge of the screen 
    # (i.e., reached the FINISH_LINE_Y). Return the turtle to the starting position.
    def is_at_goal(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True
