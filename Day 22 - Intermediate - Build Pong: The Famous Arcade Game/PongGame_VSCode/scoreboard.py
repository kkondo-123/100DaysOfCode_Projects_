"""
Name: Kana Kondo
Date: 2025-07-07-Mon
Course: 100 Days of Code Day 22
Description: Pong Game - Scoreboard Class
"""

from turtle import Turtle

SCOREBOARD_COLOR = "white"
LEFT_SCORE_POS = (-100, 200)
RIGHT_SCORE_POS = (100, 200)
ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color(SCOREBOARD_COLOR)
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(LEFT_SCORE_POS)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(RIGHT_SCORE_POS)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
    
    def r_point(self):
        self.r_score += 1
