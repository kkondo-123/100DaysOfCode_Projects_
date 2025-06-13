"""
Name: 
Date: 2025/05/
Course: 100 Days of Code Day 4
Description: Rock Paper Scissors Project
"""

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

hand = [rock, paper, scissors]

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
print(hand[user])
computer = random.randint(0, 2)
print(f"Computer chose: \n{hand[computer]}")

if user == computer:
    print("Tie/Draw! ")
elif (user == 0 and computer == 2) or user > computer: # User win
    print("You win, congrats!")
else: # User lose
    print("You lose. ")

# Solution takes into account if the user does not enter a valid answer.
