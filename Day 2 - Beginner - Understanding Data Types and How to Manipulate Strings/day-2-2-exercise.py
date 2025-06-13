# 🚨 Don't change the code below 👇
weight = input("Enter your weight in kg: ")
height = input("Enter your height in m: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
result = int(weight) / float(height) ** 2
calculation = "The calculation is " + weight + " divided by ( " + height + " to the power of 2 ) which equals " + str(result)

print(calculation)
print("Your body mass index is ")
print(int(result))
