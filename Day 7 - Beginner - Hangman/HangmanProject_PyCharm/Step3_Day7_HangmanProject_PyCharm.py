"""
Name: Kana Kondo
Date: 2025/06/13
Course: 100 Days of Code Day 7
Description: Hangman Project
"""

import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

guess_display = placeholder

# TODO-1: - Use a while loop to let the user guess again.
while "_" in guess_display:  # Guess until the user guesses correctly

    guess = input("Guess a letter: ").lower()

    display = ""

    # TODO-2: Change the for loop so that you keep the previous correct letters in display.

    #     if chosen_word[index] == guess[index]:
    #         display[index] = guess[index]  # TypeError: 'str' object does not support item assignment

    # for letter in chosen_word:
    #     if letter == guess:
    #         display += letter
    #     else:
    #         display += "_"

    for index in range(0, len(chosen_word)):  # Length of chosen_word, display and placeholder are same
        letter = chosen_word[index]
        if letter == guess:
            display += letter
        else:
            display += guess_display[index]

    guess_display = display

    print(display)

print("You Win!")