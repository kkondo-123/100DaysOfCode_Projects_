"""
Name: Kana Kondo
Date: 2020/02/13 - 2022/08/24
Course: 100 Days of Code Day 5
Description: Random Password Generator
"""

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

choose_between_sequence_and_random = input("Would you like your password in a sequence or random order? Type S for sequence and R for random order.")

All = [letters, symbols, numbers]
Input = [nr_letters, nr_symbols, nr_numbers]

if choose_between_sequence_and_random == "S":
  chosen = ""
  for alternate in range (0, 3):
    for three in range (0, Input[alternate]):
      randompicker = random.randint(0, len(All[alternate]) - 1)
      chosen += All[alternate][randompicker]
  print(f"Here is your password: {chosen}")
elif choose_between_sequence_and_random == "R":
  chosen = []
  
  for alternate in range (0, 3):
    for three in range (0, Input[alternate]):
      randompicker = random.randint(0, len(All[alternate]) - 1)
      chosen.extend(All[alternate][randompicker])
  
  chooser = random.sample(chosen, nr_letters + nr_symbols + nr_numbers)
  
  print(f"Here is your password: {''.join(chosen)}")
else:
  print("Invalid Answer. Please Try Again.")

# #Eazy Level - Order not randomised:
# #e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# All = [letters, symbols, numbers]
# Input = [nr_letters, nr_symbols, nr_numbers]

# chosen = ""
# for alternate in range (0, 3):
#   for three in range (0, Input[alternate]):
#     randompicker = random.randint(0, len(All[alternate]) - 1)
#     chosen += All[alternate][randompicker]
# print(f"Here is your password: {chosen}")

# #Hard Level - Order of characters randomised:
# #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# All = [letters, symbols, numbers]
# Input = [nr_letters, nr_symbols, nr_numbers]

# chosen = []

# for alternate in range (0, 3):
#   for three in range (0, Input[alternate]):
#     randompicker = random.randint(0, len(All[alternate]) - 1)
#     chosen.extend(All[alternate][randompicker])

# chooser = random.sample(chosen, nr_letters + nr_symbols + nr_numbers)

# print(f"Here is your password: {''.join(chosen)}")

