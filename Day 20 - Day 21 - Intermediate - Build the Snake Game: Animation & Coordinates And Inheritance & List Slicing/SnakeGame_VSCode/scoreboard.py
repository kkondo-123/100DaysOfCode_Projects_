"""
Name: Kana Kondo
Date: 2025-06-02-Wed - 2025-06-03-Thu
Course: 100 Days of Code Day 20, 21
Description: Snake Game - Scoreboard Class
"""

from turtle import Turtle

SCORE_LOCATION = (0, 270)
FONT = ("Courier New", 20, "normal")  #https://codehs.com/documentation/new/python-turtle
ALIGNMENT = "center"
COLOR = "white"
END_LOCATION = (0, 0)

# TODO 6: Create Scoreboard class inheriting from turtle class to keep track of score using turtle.write()
class Score(Turtle): 

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(SCORE_LOCATION)
        self.color(COLOR)
        self.update_score()

    def add_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(END_LOCATION)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
