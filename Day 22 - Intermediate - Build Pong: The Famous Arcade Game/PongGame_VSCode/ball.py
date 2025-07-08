"""
Name: Kana Kondo
Date: 2025-07-07-Mon
Course: 100 Days of Code
Description: Pong Game - Ball Class
"""

from turtle import Turtle

STARTING_POS = (0, 0)
# STARTING_HEADING = 37
BALL_COLOR = "white"
BALL_SHAPE = "circle"
MOVE_BY = 10  # I set it to 5 to reduce speed of ball but Angela used time module (main class) and moved by 10

# TODO 4: Create ball

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(STARTING_POS)
        self.shape(BALL_SHAPE)
        self.color(BALL_COLOR)
        self.y_dir_factor = 1
        self.x_dir_factor = 1
        self.move_speed = 0.1  # Angela uses move_speed variable to keep track
        # self.setheading(STARTING_HEADING)  # Angela used .goto()
    
    def move(self):
        # TODO 5: The screen is 600px tall. Detect collisions with the top and bottom walls. 
        #  Change the ball's movement direction upon collision

        if not -285 < self.ycor() < 285:  # If collide with top or bottom wall then bounce
            self.y_dir_factor *= -1

        new_x = self.xcor() + MOVE_BY * self.x_dir_factor
        new_y = self.ycor() + MOVE_BY * self.y_dir_factor
        self.goto(new_x, new_y)

        # We detect collision separately
        # if -385 < current_pos[0] < 385 and -285 < current_pos[1] < 285:
            # self.forward(MOVE_BY)
    
    # TODO 7: Increase speed as ball bounces on paddle

    def paddle_bounce(self):  # Bounce in the x direction
        self.x_dir_factor *= -1.5
        self.move_speed *= 0.9

        # .speed() did not work
        # self.speed(self.speed() + 1)
        # print(self.speed())

    def reset_ball(self):
        self.goto(STARTING_POS)
        # self.speed("normal")
        self.move_speed = 0.1

        new_x_direction = -1
        if self.x_dir_factor < 0:
            new_x_direction = 1
        
        self.x_dir_factor = new_x_direction
