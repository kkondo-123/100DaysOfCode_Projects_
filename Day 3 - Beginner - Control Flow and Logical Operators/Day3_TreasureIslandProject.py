print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# First choice event
choice = input('You\'re at a cross road. Where do you want to go?\n\tType "left" or "right"\n').lower()
if choice == 'left': # Move on to second event

    # Second choice event
    choice = input('You\'ve come to a lake. There is an island in the middle of he lake. \n\tType "wait" to wait for a '
                   'boat. Type "swim" to swim across. \n').lower()

    if choice == 'wait': # Move onto third event.

        # Third choice event
        choice = input('You arrive at the island unharmed. There is a house with 3 doors. \n\tOne red, one yellow and '
                       'one blue. Which colour do you choose?\n').lower()

        if choice == 'red':
            print("You were burned by fire. Game Over! ")
        elif choice == 'blue':
            print("You were eaten by beasts. Game Over! ")
        elif choice == 'yellow':
            print("You've found the treasure. YOU WIN! ")
        else:
            print("You tried to escape and failed. Game Over. ")

    else: # Game over
        print("You were attacked by trout. Game Over. ")

else: # Game over
    print("You fell into a hole. Game Over! ")

# Should use .lower() for user friendliness (match letter casing)
