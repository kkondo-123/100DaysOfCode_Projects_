"""
Name: Kana Kondo
Date: 2025-06-29-Sun
Course: 100 Days of Code Day 14
Description:
    The goal is to build a game that asks the user to guess who has more followers on Instagram.
    Original Higher Lower Game
    https://www.higherlowergame.com/
    Demo of Final Project
    https://appbrewery.github.io/python-day14-demo/
"""

from game_data import data
from art import logo, vs
import random

NAME = 'name'
FOLLOWER = 'follower_count'
DESCRIPTION = 'description'
COUNTRY = 'country'

def get_data():
    return random.choice(data)

def display_instagram(datum):
    print()

def correct_ans(a, b):
    if a[FOLLOWER] > b[FOLLOWER]:
        return 'a'
    return 'b'

def user_ans(a, b):  # Compare
    user_answer = ''
    while True:
        print(f"Compare A: {a[NAME]}, a {a[DESCRIPTION]}, from {a[COUNTRY]}. ")
        print(vs)
        print(f"Against B: {b[NAME]}, a {b[DESCRIPTION]}, from {b[COUNTRY]}. ")

        user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        if user_answer == 'a' or user_answer == 'b':
            return user_answer
        else:
            print("Please type a valid answer. \n")

play_game = True
score = 0
person_a = get_data()

print(logo)

while play_game:
    person_b = get_data()
    person_temp = person_b  # The next person_a will be person_b.  This is a placeholder.

    user = user_ans(a=person_a, b=person_b)
    correct = correct_ans(a=person_a, b=person_b)

    print(logo)

    if user == correct:
        score += 1
        print(f"You're right! Current score: {score}")

        person_a = person_temp

    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        play_game = False
