"""
Name: Kana Kondo
Date: 
Course: 100 Days of Code Day 1
Description: Band Name Generator
"""

#1. Create a greeting for your program.
print ("Hello! Welcome to the Band Name Generator ('U')\nThis generates a band name based on the city that you grew up in and the name of a pet.")

#2. Ask the user for the city that they grew up in.
City = input("What is the city that you grew up in? \n") 
# city_name = input("What's the name of the city you grew up in?\n")

#3. Ask the user for the name of a pet.
Pet = input("What is the name of a pet? \n")  
# pet_name = input("What's your pet's name?\n")

#4. Combine the name of their city and pet and show them their band name.
print("Your band name is...(drumroll) " + City + Pet)
# print("Your band name could be: " + city_name + " " + pet_name)

#5. Make sure the input cursor shows on a new line, see the example at:
#   https://replit.com/@appbrewery/band-name-generator-end

# Line 11 and 14: Bad variable naming convention according to PEP8 (Python coding style)
