"""
Name: Kana Kondo
Date: 2025-07-08-Tue
Course: 100 Days of Code Day 25
Description: US States Game
"""

import turtle as t
import pandas
'''
Install pandas in VSCode: https://www.youtube.com/watch?v=q-beq0bo4Cw
(Assuming that pip is already installed, covered in Day 18)
 1. Open 'zsh' terminal and type 'python3' -> Press tab and look at see the Python versions. 
    Continue to type 'python3 -m venv env' and press enter.
 2. A file called 'env' should appear.  Type 'source env/bin/activate'. 
    (env/bin/activate is the file directory to the file called 'activate')
 3. Type 'pip3 install pandas' -> A bunch of commands/lines should run in terminal.
    Bottom line should mention: 'Successfully installed .... pandas...'
    (The module error for pandas should dissapear here)
    Got error in terminal: 
        'WARNING: The scripts f2py, f2py3 and f2py3.8 are installed in '/Users/subkana/Library/Python/3.8/bin' which is not on PATH. Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.'
 4. When switched to Python version to 3.8.10 and not the Python 
    'env (3.8.10)' the video used, it worked. -> Ran using 'run button' instead of 
    command. 
'''

IMAGE = "blank_states_img.gif"
START_SCREEN_TITLE = "U.S. States Game"
START_TEXT_TITLE = "Guess the State"
START_TEXT_PROMPT = "What's another state's name?"
GAME_SCREEN_TITLE = "Name the States"
STATES_CSV_FILENAME = "50_states.csv"
STATE_COLUMN = "state"
TEXT_FONT = ("Arial", 8, "normal")
TEXT_ALIGNMENT = "center"
X_COLUMN = 'x'
Y_COLUMN = 'y'
TERMINATE_KEYWORD = 'Exit'
RECORD_FILENAME = "states_to_learn.csv"

screen = t.Screen()
screen.title(START_SCREEN_TITLE)
screen.addshape(IMAGE)
t.shape(IMAGE)

# https://stackoverflow.com/questions/42878641/get-mouse-click-coordinates-in-python-turtle
#  To get the coordinates of each state

# Get data from csv file
data = pandas.read_csv(STATES_CSV_FILENAME)
data_dict = data.to_dict('list')
fifty_states = data_dict[STATE_COLUMN]  # Angela used: data.state.to_list()
# https://saturncloud.io/blog/how-to-convert-dataframe-to-dictionary-in-pandas-without-index/#:~:text=Converting%20DataFrame%20to%20Dictionary%20Without,arguments%20to%20the%20orient%20parameter.

input_title = START_TEXT_TITLE

# TODO 5: Record the correct guesses in a list
correct_guesses = []

# TODO 3: Write correct guesses onto the map
def write_correct_guesses():
    # Get index of state to get x and y coordinates
    index = fifty_states.index(guess)
    coordinates = (data_dict[X_COLUMN][index], data_dict[Y_COLUMN][index])  # Angela uses (data)
    
    new_state = t.Turtle()
    new_state.penup()
    new_state.hideturtle()
    new_state.goto(coordinates)
    new_state.write(arg=guess, align=TEXT_ALIGNMENT, font=TEXT_FONT)

    '''
    Angela used:
    state_data = data[data.state == answer_state]  
    # Where it will get the row of data where the user's guess equals the U.S. 
    #   state (correct guess)
    new_state.goto(state_data.x, state_data.y)
    '''

def get_guess(t, p):
    # TODO 1: Convert the guess to Title case
    #  https://www.w3schools.com/python/ref_string_title.asp
    return screen.textinput(title=t, prompt=p).title()

new_data = ''

# TODO 4: Use a while loop to allow the user to keep guessing
keep_guessing = True
while keep_guessing:
    
    screen.title(GAME_SCREEN_TITLE)
    guess = get_guess(input_title, START_TEXT_PROMPT)
    
    if guess == TERMINATE_KEYWORD:
        # Use Pandas data frame to record missing states
        missing_states = []
        for state in fifty_states:
            if state not in correct_guesses:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)

        break

    # TODO 2: Chck if the guess is among the 50 states
    if guess in fifty_states and guess not in correct_guesses:  # Make sure the state was not already guessed
        write_correct_guesses()    
        correct_guesses.append(guess)
    
    # TODO 6: Keep track of the score (score = length of correct_guesses)
    input_title = f"{len(correct_guesses)}/50 States Correct"

    if len(correct_guesses) == 50:
        keep_guessing = False
    
# screen.exitonclick()  # Since we use the 'break' keyword above, we don't need this line of code

# TODO 7: Save the msising states to a .csv file called 'states_to_learn.csv'
new_data.to_csv(RECORD_FILENAME)
