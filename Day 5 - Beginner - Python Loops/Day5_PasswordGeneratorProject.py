"""
Name: Kana Kondo
Date: 2025/06/03
Course: 100 Days of Code Day 5
Description: Random Password Generator
"""

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []

for l in range(nr_letters):
    password.append(letters[random.randint(0, len(letters) - 1)])
for s in range(nr_symbols):
    password.append(symbols[random.randint(0, len(symbols) - 1)])
for n in range(nr_numbers):
    password.append(numbers[random.randint(0, len(numbers) - 1)])

# print(password)
random.shuffle(password)
print(f"Here is your password: {''.join(password)}")
