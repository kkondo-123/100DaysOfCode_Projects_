"""
Name: Kana Kondo
Date: 2025-07-04-Fri - 2025-07-07-Mon
Course: 100 Days of Code Day 22
Description: Pong Game - Paddle Class
"""

from turtle import Turtle

STRETCH_PADDLE_WID = 5
STRETCH_PADDLE_LEN = 1
PADDLE_COLOR = "white"
PADDLE_SHAPE = "square"

# TODO 3: Refactor the code. Create a paddle.py file for the Paddle class.
#  Paddle class must inherit from Turtle.
#  Paddle objects must be initialised with tuple for X and Y coordinates.

class Paddle(Turtle):

    def __init__(self, coordinates):
        super().__init__()
        self.penup()
        self.shape(PADDLE_SHAPE)
        self.color(PADDLE_COLOR)
        self.shapesize(stretch_wid=STRETCH_PADDLE_WID, stretch_len=STRETCH_PADDLE_LEN)  # Default square size is 20 x 20, Paddle should be 20 x 100, Width = y axis and length = x axis 
        self.goto(coordinates)

    # Should change function names to go_up and go_down since up and down are already turtle methods
    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 20)
        # print("Go up!")

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 20)
        # print("Go down!")

# Original Code From Main Class That Went Into Paddle Class
'''
    # TODO 2: Create and move a paddle (right side)
    paddle_right = Turtle()
    paddle_right.penup()
    paddle_right.shape(PADDLE_SHAPE)
    paddle_right.color(PADDLE_COLOR)
    paddle_right.shapesize(stretch_wid=5, stretch_len=1)  # Default square size is 20 x 20, Paddle should be 20 x 100, Width = y axis and length = x axis 
    paddle_right.goto(PADDLE_RIGHT_POS)
    # screen.update()

    def go_up():
        # paddle.(x=paddle.xcor(), y=(round(paddle.ycor()) + 20))
        # paddle.teleport(paddle.xcor(), paddle.ycor() + 20)
        paddle_right.goto(paddle_right.xcor(), paddle_right.ycor() + 20)
        # print("Go up!")

    def go_down():
        # paddle.goto(x=paddle.xcor(), y=(round(paddle.ycor()) - 20))
        # paddle.teleport(paddle.xcor(), paddle.ycor() - 20)    
        paddle_right.goto(paddle_right.xcor(), paddle_right.ycor() - 20)
        # print("Go down!")
'''
