"""
Name: Kana Kondo
Date: 06-29-2024-Sun
Course: 100 Days of Code Day 15
Description:
    The goal is to build the program for a coffee machine.
    Program Requirements
        Download the PDF for the program requirements here:
        https://drive.google.com/uc?export=download&id=1eIZt2TeFGVrk4nXkx8E_5Slw2coEcOUo
"""

from art import coffee, machine

INGREDIENTS = 'ingredients'
WATER = 'water'
COFFEE = 'coffee'
MILK = 'milk'
COST = 'cost'
OFF = 'off'

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

cad_coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01,
}

def get_choice():
    user = ''

    while True:
        user = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if user in MENU or user == OFF:
            return user
        else:
            print("Please enter valid input.")

def check_resources(resource, ingredients):
    for r in resource:
        if r in ingredients:  # Check if ingredient is needed to make drink
            if resource[r] >= ingredients[r]:  # If sufficient amount
                # print(f"Current amt of {r}: {resource[r]}")
                # print(f"Required amt of {r}: {ingredients[r]}")
                print(f"Sufficient {r}. ")
            else:
                print(f"Sorry, there's not enough {r}.")
                return False
    return True

def enter_coins(coins):
    print("Please insert coins. ")
    sum = 0.0
    num_coins = 0

    for name, value in coins.items():
        num_coins = int(input(f"How many {name} (${value})?: "))
        sum += num_coins * value

    print(f"You've entered a total of ${sum}. ")
    return sum

def enough_money(paid, cost):
    if paid >= cost:
        print(f"Here is ${round(paid - cost, 2)} in change. ")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded")
        return False

def use_coffee_resources(resource, ingredients):
    for r in resource:
        if r in ingredients:  # Check if ingredient is needed to make drink
            resource[r] -= ingredients[r]  # Deducts amount of resources used

def resource_report(resource, money):
    print("\n-------------------RESOURCES-------------------")
    print(f"{WATER}: {resource[WATER]}ml")
    print(f"{MILK}: {resource[MILK]}ml")
    print(f"{COFFEE}: {resource[COFFEE]}g")
    print(f"Money: ${money}")

def enter_to_cont():
    input("\nPress any key to continue...")

def view_drink(coffee_drink, drink_choice):
    print(f"\n-------------------{drink_choice}-------------------")
    if WATER in coffee_drink[INGREDIENTS]:
        print(f"{WATER}: {coffee_drink[INGREDIENTS][WATER]}ml")
    if MILK in coffee_drink[INGREDIENTS]:
        print(f"{MILK}: {coffee_drink[INGREDIENTS][MILK]}ml")
    if COFFEE in coffee_drink[INGREDIENTS]:
        print(f"{COFFEE}: {coffee_drink[INGREDIENTS][COFFEE]}g")
    print(f"{COST}: ${coffee_drink[COST]}")


using_machine = True

choice = ''
drink = ''
ingredient = ''

sufficient_resources = False
paid_money = 0.0
money_report = 0.0

while using_machine:
    print(f"\n\n{machine}")
    resource_report(resources, money_report)

    print("Turn off the Coffee Machine by entering 'off'")

    choice = get_choice()
    if choice == 'off':
        print("Thank you for using Coffee Machine ☕")
        using_machine = False

    else:
        drink = MENU[choice]
        ingredient = drink[INGREDIENTS]
        cost = drink[COST]
        print(f"You have ordered a: {choice}")

        enter_to_cont()
        view_drink(drink, choice)
        enter_to_cont()

        sufficient_resources = check_resources(resources, ingredient)
        if sufficient_resources:
            enter_to_cont()

            paid_money = enter_coins(cad_coins)

            enter_to_cont()

            if enough_money(paid_money, cost):
                use_coffee_resources(resources, ingredient)
                money_report += cost
                resource_report(resources, money_report)

                enter_to_cont()

                print(coffee)

                print(f"Here's your {choice}. Enjoy! ")

                enter_to_cont()
