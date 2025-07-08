"""
Name: Kana Kondo
Date: 2025-06-02-Wed - 2025-06-03-Thu
Course: 100 Days of Code Day 20, 21
Description: Snake Game - Snake Class
"""

from turtle import Turtle

MOVE_DISTANCE = 20
DIRECTIONS = [0, 90, 180, 270]  # Right = 0 degrees, Up = 90 degrees, Left = 180 degrees, Down = 270 degrees
RIGHT = DIRECTIONS[0]
UP = DIRECTIONS[1]
LEFT = DIRECTIONS[2]
DOWN = DIRECTIONS[3]
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

# TODO 2: Put snake_body and new_segment (snake related) into snake.py
class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            # print(position)
            self.add_segment(position)

        # When extending snake (score goes up, snake eats food), will create add_segment method that will modified the code below
        # new_segment = ''
        # for snake_num in range(3):
        #     new_segment = Turtle(shape="square")
        #     new_segment.color("white")
        #     new_segment.penup()
        #     new_segment.teleport(0 - 20 * snake_num, 0)
        #     self.snake_body.append(new_segment)
    
    def add_segment(self, pos): 
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()

        # https://docs.python.org/3/library/turtle.html
        # new_segment.goto(pos)  # This is what Angela used -> No error because .goto() has only takes 2 arguments
        # new_segment.teleport(pos)  # This gives an error because .teleport() has/takes 3 positional arguments and having a tuple with 2 arguments does not fulfill 3 arguments 
        new_segment.teleport(pos[0], pos[1])
        self.snake_body.append(new_segment)

    def extend(self):
        self.add_segment(self.snake_body[-1].position())

    def move(self):
        for seg_num in range(len(self.snake_body) - 1, 0, -1):  # Range function does not take any keyword arguments since Python came from C Language0
            new_x = self.snake_body[seg_num - 1].xcor()
            new_y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # TODO 3: Implement up, down, left and right moving keys as functions into Snake class.
    def right(self):
        if self.head.heading() != LEFT:  # In snake game rules, you cannot go the opposite direction of where you are heading ('bounce back')
            self.head.setheading(RIGHT)  

    # TODO 4: Implement not-being-able-to-bounce-back feature in other directions (up, left, down)
    def up(self):
        if self.head.heading() != DOWN: 
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT: 
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP: 
            self.head.setheading(DOWN)

