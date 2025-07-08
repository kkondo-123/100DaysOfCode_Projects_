"""
Name: Kana Kondo
Date: 2025-07-04-Fri - 2025-07-07-Mon
Course: 100 Days of Code Day 22
Description: Pong Game - Main Class
"""

from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
PADDLE_RIGHT_POS = (350, 0)
PADDLE_LEFT_POS = (-350, 0)
BALL_PADDLE_DISTANCE = 50
BOUNCE_X_POS = 320
OUT_OF_BOUNDS_X_POS = 380

# TODO 1: Create the screen
screen = Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)

# TODO 3: Make a Paddle Class and create paddle object, features and functions 
r_paddle = Paddle(PADDLE_RIGHT_POS)
l_paddle = Paddle(PADDLE_LEFT_POS)

screen.listen()
'''
Why can't I use go_up(paddle_right) in the screen.onkey()? 
 https://stackoverflow.com/questions/69474979/using-the-turtle-package-is-it-possible-to-create-a-function-asking-for-an-argu
 "The onkeypress method doesn't allow to pass a function with arguments, however you can use functools.partial for this kind of situations."
'''
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')

# TODO 3: l_paddle needs to move up and down with 'w' and 's' keys
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

# TODO 4: Create ball
ball = Ball()

scoreboard = Scoreboard()

# screen.tracer(1)  # Angela used screen.update()
game_is_on = True
while game_is_on:
    time.sleep(0.1)  # Angela delayed time  
    # time.sleep(ball.move_speed)  # Angela delays using time module

    screen.update()
    scoreboard.update_score()
    ball.move()  # Angela detected collision separately

    # Detect collision with r_paddle
    if (ball.distance(r_paddle) < BALL_PADDLE_DISTANCE and ball.xcor() > BOUNCE_X_POS) or (ball.distance(l_paddle) < BALL_PADDLE_DISTANCE and ball.xcor() < -(BOUNCE_X_POS)):
        ball.paddle_bounce()

        # print("Made contact! ")

    # TODO 6: Detect if ball goes out of bounds at the edge of the screen.  If yes, reset the ball's position to the center of the screen.
    #  The ball should then start moving towards the other player
    
    # Angela put in separate statements because we need to distinct the left and right side missing the ball
    # if ball.xcor() < -(OUT_OF_BOUNDS_X_POS) or ball.xcor() > OUT_OF_BOUNDS_X_POS:
    #     ball.reset_ball()

    if ball.xcor() < -(OUT_OF_BOUNDS_X_POS):  # Left side misses
        ball.reset_ball()
        scoreboard.r_point()

    if ball.xcor() > OUT_OF_BOUNDS_X_POS:  # Right side misses
        ball.reset_ball()
        scoreboard.l_point()

screen.exitonclick()
