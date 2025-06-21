"""
Name: Kana Kondo
Date: 2025/05/23
Course: 100 Days of Code Day 2
Description: Tip Calculator Proejct
"""

# Solution 1
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
each_person = bill * (1 + tip * 0.01) / people
rounded_num = round(each_person, ndigits=2)
print(f"Each person should pay: $ {rounded_num}")

# Solution 2
print("Welcome to the tip calculator!")
total_bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12  or 15? ")
people = input("How many people to split the bill? ")

calculation1 = float(total_bill) + (int(tip) / 100 * float(total_bill))
calculation2 = float(calculation1) / int(people)
result = round(calculation2, 2)

print(f"Each person should pay: ${result}")

