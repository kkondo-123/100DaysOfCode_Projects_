"""
Name: 
Date: 2025/06/13
Course: 100 Days of Code Day 7
Description: Hangman Project
"""

import random

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
chosen_word = word_list[random.randint(0, len(word_list) - 1)]  # Or random.choice()
print(chosen_word)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.
if guess in chosen_word:  # Angela uses for loop and compares each letter in chosen_word to guess
    print("Right")
else:
    print("Wrong")
