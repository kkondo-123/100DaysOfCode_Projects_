"""
Name: Kana Kondo
Date: 2025-06-28-Sat
Course: 100 Days of Code Day 10
Description: Calculator
"""

from art import logo

# TODO: Write out the other 3 functions - subtract, multiply and divide.
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"
keys = {'+': add, '-': subtract, '*': multiply, '/': divide}

# TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.
def calculate(operator, n1, n2):
    result = 0.0

    if operator in keys:
        result = keys[operator](n1, n2)
        print(f"{n1} {operator} {n2} = {result}")

    else:
        print(f"{n1} undefined {n2} = {result}")

    return result

def calculator_options():
    print("\n\nCalculator options: ")
    print("  - 'n' to start a new calculation")
    print("  - 'e' to exit the calculator program")
    print("  - Any other key to continue calculating")

calculating = True

while calculating:

    continue_calc = ''
    operator = ''
    num2 = 0
    result = 0

    print('\n' * 30)
    print(logo)
    num1 = int(input("What's the first number?: "))

    while continue_calc != 'n' or 'e':
        for key in keys:
            print(key)
        operator = input("Pick an operator: ")
        num2 = int(input("What's the next number?: "))
        result = calculate(operator, num1, num2)

        print(f"Result = {result}")
        calculator_options()
        continue_calc = input("Type your option: ")

    if continue_calc == 'e':
        calculating = False

print("Bye Bye!")
