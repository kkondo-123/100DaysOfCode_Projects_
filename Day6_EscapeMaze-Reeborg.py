# Link to Reeborg's world: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

# My solution

def turn_right():
    turn_left()
    turn_left()
    turn_left()
 
while not at_goal():
    if front_is_clear():
        move()
    elif right_is_clear():
        turn_right()
        move()
    elif wall_in_front():
        turn_left()

# Angela's solution

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# while front_is_clear():  # Find a wall
#   move()
# turn_left()  # Turn wall onto right side

# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     elif wall_in_front():
#         turn_left()
