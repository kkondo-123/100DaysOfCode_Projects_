"""
Name: Kana Kondo
Date: 2025-06-02-Wed - 2025-06-03-Thu
Course: 100 Days of Code Day 20, 21
Description: Snake Game - Main Class
"""

# TODO 2: Modify imports.  Need to import snake class. Only need to import Screen.  Will use Turtle in snake.py
from turtle import Screen  #, Turtle
from snake import Snake
import time
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# TODO 2: main.py -> snake.py Replace the code below with 1 line of code: snake = Snake()
'''
# TODO 1: Create a snake body with 3 turtles. Each turtle should be white square (20x20)
#  Each turtle should be next to each other.  First turtle is at (0, 0) and next one is 20 pixels left.
snake_body = []
new_segment = ''
for snake_num in range(3):
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.teleport(0 - 20 * snake_num, 0)
    snake_body.append(new_segment)
'''
snake = Snake()

food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    # for seg in snake_body:
    #     seg.forward(20)

    # TODO 2: main.py -> snake.py Replace the code below with 1 line of code: snake.move()
    '''
    for seg_num in range(len(snake_body) - 1, 0, -1):  # Range function does not take any keyword arguments since Python came from C Language0
        new_x = snake_body[seg_num - 1].xcor()
        new_y = snake_body[seg_num - 1].ycor()
        snake_body[seg_num].goto(new_x, new_y)
    ''' 
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        # print("Nom Nom Nom")

        snake.extend()

        # TODO 6: Keep track of score using Scoreboard class
        score.add_score()
    
    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        score.game_over()

    # Detect collision with tail
    for segment in snake.snake_body:
        if segment == snake.head:  
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
