"""
Name: Kana Kondo
Date: 2025-07-08-Tue
Course: 100 Days of Code Day 24
Description: Mail Merge Project
"""

# TODO: Create a letter using starting_letter.txt 
#   for each name in invited_names.txt
#   Replace the [name] placeholder with the actual name.
#   The filename for each letter should be 'letter_for_(name).txt' 
#     with (name) replaced with the actual name.
#   Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    # Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        # Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

LETTER_FILEPATH = "./Input/Letters/starting_letter.txt"
NAMES_FILEPATH = "./Input/Names/invited_names.txt"
SEND_LETTER_FILEPATH = "./Output/ReadyToSend"
NAME_PLACEHOLDER = "[name]"

template_letter = []

with open(LETTER_FILEPATH, "r") as file:
    for line in file:
        # print(f"Here: {line}")
        # letter += line  # This adds every character to letter list
        template_letter.append(line)  # Need to include '\n' newline character when writing to file

# print(template_letter)

names = []

with open(NAMES_FILEPATH, "r") as file:
    for line in file:
        # names.append(line.strip("\n"))
        names.append(line.strip())  # Angela doesn't specify '\n' but it does get rid of the newline character.

# print(names)

new_letter = []
for name in names:
    # print(f"{name}'s Letter:\n")
    new_letter = template_letter
    new_letter[0] = new_letter[0].replace(NAME_PLACEHOLDER, name)  # Python strings are immutable so, that means that .replace() won't modify the original string
    # print(new_letter)

    # Angela uses .docx 
    # new_filepath = f"{SEND_LETTER_FILEPATH}/letter_for_{name}.txt"
    new_filepath = f"{SEND_LETTER_FILEPATH}/letter_for_{name}.docx"

    with open(new_filepath, "w") as data:
        for line in new_letter:
            data.write(line)

# https://developers.google.com/edu/python/strings
# Python strings are "immutable" which means they cannot be changed after they are created


