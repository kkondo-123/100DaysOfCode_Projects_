"""
Name:
Date: 2020/05/22 - 2022/08/26
Course: 100 Days of Code Day 7
Description: Hangman Project
"""

#Step 1 
import random

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

chosen_word = word_list[random.randint(0, 2)]
user_input = input("Guess a letter: ").lower()

for letter in chosen_word:
  if user_input == letter:
    print("Right")
  else:
    print("Wrong")
