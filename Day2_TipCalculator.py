print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
each_person = bill * (1 + tip * 0.01) / people
rounded_num = round(each_person, ndigits=2)
print(f"Each person should pay: $ {rounded_num}")
