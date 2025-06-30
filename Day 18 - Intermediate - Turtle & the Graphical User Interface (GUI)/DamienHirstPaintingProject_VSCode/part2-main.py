"""
Name: Kana Kondo
Date: 2025-06-30-Mon
Course: 100 Days of Code Day 18
Description: Hirst Painting Project Part 2
"""

'''
Instructions:
  - 10 x 10 rows x columns of spots 
  - 20 size dots spaced apart by 50
  - Use documentation: https://docs.python.org/3/library/turtle.html

Used previous lessons/projects (within day 18) to create project:
  - https://replit.com/@appbrewery/day-18-4-end#main.py
  - https://replit.com/@appbrewery/day-18-5-end#main.py
'''

import random
import turtle as t

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
SCREEN_XCOR = 0
SCREEN_YCOR = 0
DIRECTIONS = [0, 90, 180, 270]
PENSIZE = 20  # Diameter/width of 20, radius of 10
SPEED = "fastest"
START_XCOR = -400
START_YCOR = -250
# DISTANCE = 70  # Since radius of dot is 10 and need to consider two dots: 50 + 10 (radius) * 2 (number of dots) = 70
DISTANCE = 50

tim = t.Turtle()
screen = t.Screen()
t.colormode(255) # https://stackoverflow.com/questions/16778324/what-does-bad-color-sequence-mean-in-python-turtle
# t.screensize(1000, 10000)
screen.setup (width=SCREEN_WIDTH, height=SCREEN_HEIGHT, startx=SCREEN_XCOR, starty=SCREEN_YCOR)

# Color palette generated from part 1
color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

# NOTE: I was not supposed to know how to use coordinates (learn/use in Day 19)
# I should use the directions and move forward methods

# Set tim attributes
tim.pensize(PENSIZE)  
tim.speed(SPEED)
tim.penup()  # penup() to not leave a trace behind (line)
tim.teleport(START_XCOR, START_YCOR)
# Hide turtle for faster results and visuals
tim.hideturtle()

def row_of_dots(dot_num):
    for _ in range(dot_num):

        # Angela used the "size" attribute in .dot().  The pensize doesn't affect the size of the dot
        # tim.dot(random.choice(color_list))
        tim.dot(PENSIZE, random.choice(color_list))

        tim.forward(DISTANCE)


for _ in range(10):
    row_of_dots(10)
    tim.teleport(START_XCOR, tim.ycor() + DISTANCE)

# Angela used this
screen.exitonclick()

