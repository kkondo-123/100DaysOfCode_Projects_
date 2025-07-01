"""
Name: Kana Kondo
Date: 2025-06-30-Mon
Course: 100 Days of Code Day 19
Description: Turtle Race Project
"""

from turtle import Turtle, Screen
import random

is_race_on = False

# Setup screen
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')
# print(user_bet)

COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtles = []

# Setup turtle
TURTLE_SPACING = 30

# TODO 1: Create 6 turtles, each a color from COLORS
for index in range(0, len(COLORS)):
    new_turtle = Turtle(shape="turtle")  # Angela avoided using 'tim' as each appended turtle will be distinct/individual
    new_turtle.penup()
    new_turtle.speed("fast")
    new_turtle.goto(x=-230, y=-100 + TURTLE_SPACING * index)
    new_turtle.color(COLORS[index])
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for racer in turtles:

        if racer.xcor() > 230:
            is_race_on = False
            winning_color = racer.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner! ")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner! ")

        rand_distance = random.randint(0, 10)
        racer.forward(rand_distance)
    
screen.exitonclick()

# https://www.asciiart.eu/animals/reptiles/turtles
print("""
                    __
         .,-;-;-,. /'_\\
       _/_/_/_|_\_\) /
     '-<_><_><_><_>=/\\
jgs    `/_/====/_/-'\_\\
        ""     ""    ""
""")
