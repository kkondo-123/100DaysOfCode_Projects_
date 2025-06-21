"""
Name: Kana Kondo
Date: 2021/10/27 - 2022/08/23
Course: 100 Days of Code Day 4
Description: Rock Paper Scissors Project
"""

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

#Write your code below this line 👇
import random

print("Welcome to the Rock Sissor Paper Player VS CP! ")
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user > 2 or user < 0:
  print("Invalid Answer. Try Again.")

else:
  rps = [rock, paper, scissors]
  print(rps[user])
  
  computer_player = random.randint(0, 2)
  print(f"Computer Chose: \n{rps[computer_player]}")
  
  #1 beats 0, 2 beats 1, 0 beats 2
  if user == computer_player:
    print("It's a tie. Try again.")
  elif user - computer_player == 1 or user - computer_player == -2:
    print("You win! Congratulations!")
  else:
    print("You lose! Try again.")
