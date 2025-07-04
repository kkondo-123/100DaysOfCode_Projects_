"""
Name: Kana Kondo
Date: 2025-06-02-Wed - 2025-06-03-Thu
Course: 100 Days of Code Day 20, 21
Description: Snake Game - Food class
"""

import random
from turtle import Turtle

# TODO 5: Modify Food class so that it inherits from Turtle
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
