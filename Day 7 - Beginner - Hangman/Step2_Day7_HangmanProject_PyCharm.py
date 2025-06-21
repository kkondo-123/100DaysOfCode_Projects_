"""
Name: 
Date: 2025/06/13
Course: 100 Days of Code Day 7
Description: Hangman Project
"""

import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word
placeholder = ""
for i in chosen_word:
    placeholder += "_"
print(placeholder)

guess = input("Guess a letter: ").lower()

# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.
display_letters = ""

for letter in chosen_word:
    if letter == guess:
        # print("Right")
        display_letters += guess
    else:
        # print("Wrong")
        display_letters += "_"

print(display_letters)