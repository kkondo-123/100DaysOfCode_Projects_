"""
Name: Kana Kondo
Date: 2025-06-29-Sun
Course: 100 Days of Code Day 16
Description: Coffee Machine OOP version (Similar to Day 15 Project)
"""
# from menu import Menu, MenuItem  # File did not include ', MenuItem' at the end of this line like it did in Angela's video
# Should not edit imports section -> Can work code without adding 'MenuItem'

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# # Constants
# INGREDIENTS = 'ingredients'
# WATER = 'water'
# COFFEE = 'coffee'
# MILK = 'milk'
# COST = 'cost'
OFF = 'off'

# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "milk": 0,  # Modified to make it easier to access
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }


# # Initialize classes
# menu_items = []
# for key, value in MENU.items():
#     menu_items.append(MenuItem(name=key, water=value[INGREDIENTS][WATER], 
#                                milk=value[INGREDIENTS][MILK], 
#                                coffee=value[INGREDIENTS][COFFEE], cost=value[COST]))

# Initialize classes
coffee_menu = Menu()
machine = CoffeeMaker()
bank_atm = MoneyMachine()


# Methods
def enter_to_cont():
    input("\nPress any key to continue...")

def get_choice(menu_of_coffees):
    user = ''

    while True:
        user = input(f"What would you like? ({menu_of_coffees.get_items()}): ").lower()  # Don't forget to use .get_items() method from Menu Class!

        if user in menu_of_coffees.get_items() or user == OFF:
            return user
        else:
            print("Please enter valid input.")


# Initialize variables
using_machine = True

choice = ''
drink = ''

sufficient_resources = False
paid_money = 0.0
money_report = 0.0


# Testing
# print(coffee_menu.get_items())
# print(coffee_menu.find_drink('latte').cost)


while using_machine:
    enter_to_cont()

    print("Turn off the Coffee Machine by entering 'off'")

    choice = get_choice(coffee_menu)
    if choice == OFF:
        print("Thank you for using Coffee Machine ☕")
        using_machine = False

    else:
        drink = coffee_menu.find_drink(choice)
        print(f"You have ordered a: {choice}")

        if machine.is_resource_sufficient(drink):

            if bank_atm.make_payment(drink.cost):

                enter_to_cont()

                machine.make_coffee(drink)

                enter_to_cont()

                bank_atm.report()
                machine.report()
