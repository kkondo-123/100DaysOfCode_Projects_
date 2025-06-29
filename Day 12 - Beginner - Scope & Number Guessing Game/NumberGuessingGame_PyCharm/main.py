"""
Name: Kana Kondo
Date: 2025-06-23
Course: 100 Days of Code Day 12
Description: Guess the Number Game
"""

import random
from art import logo

# logo = """
#   ___  _  _  ____  ____  ____    ____  _  _  ____    __ _  _  _  _  _  ____  ____  ____
#  / __)/ )( \(  __)/ ___)/ ___)  (_  _)/ )( \(  __)  (  ( \/ )( \( \/ )(  _ \(  __)(  _ \
# ( (_ \) \/ ( ) _) \___ \\___ \    )(  ) __ ( ) _)   /    /) \/ (/ \/ \ ) _ ( ) _)  )   /
#  \___/\____/(____)(____/(____/   (__) \_)(_/(____)  \_)__)\____/\_)(_/(____/(____)(__\_)"""
print(logo)

range_min = 1
range_max = 100
EASY = 'easy'
HARD = 'hard'

print("Welcome to the Number Guessing Game!")
print(f"Guess a number between {range_min} - {range_max}")
difficulty = input(f"Difficulty. Type '{EASY}' or '{HARD}': ").lower()

lives = 0
if difficulty == EASY:
    lives = 10
elif difficulty == HARD:
    lives = 5
else:
    print("Standard difficulty is easy.")
    lives = 10

correct_num = random.randint(range_min, range_max)
guess = 0

continue_game = True
while continue_game:
    print(f"Correct answer is: {correct_num}")

    print(f"You have {lives} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    lives -= 1

    if lives > 0:
        if guess > correct_num:
            print("Too high. ")
        elif guess < correct_num:
            print("Too low. ")
        elif guess == correct_num:
            print("You've guessed the correct number! ")
            continue_game = False
    elif lives <= 0:
        print("You've run out of guesses.")
        print(f"The correct number was: {correct_num}")
        continue_game = False

