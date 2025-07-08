"""
Name: Kana Kondo
Date: 2025-07-07-Mon
Course: 100 Days of Code Day 23
Description: Turtle Crossing Game - Scoreboard Class
"""

# TODO 5: Create scoreboard class that keeps track of which level the user is on. 
# Every time the turtle player does a successful crossing, the level should increase. 
# When the turtle hits a car, GAME OVER should be displayed in the centre. 
# (Solution = Step 7 Video)

from turtle import Turtle

FONT = ("Courier", 24, "normal")
COLOR = "black"
ALIGNMENT = "center"
SCORE_POS = (-225, 260)
GAME_OVER_POS = (0, 0)

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color(COLOR)
        self.penup()
        self.hideturtle()
        self.level = 0  # Angela starts from level 1
        self.goto(SCORE_POS)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(GAME_OVER_POS)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
