"""
Name: Kana Kondo
Date: 2025-07-08-Tue
Course: 100 Days of Code Day 26
Description: NATO Phonetic Alphabet Project
"""

import pandas

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_alphabet = {}
for (index, row) in data.iterrows():
    phonetic_alphabet[row.letter] = row.code
# Angela coded: {row.letter: row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = list(input("Enter a word: ").upper())  # https://www.naukri.com/code360/library/how-to-convert-string-into-a-list-in-python#:~:text=To%20convert%20a%20string%20back,l'%2C%20'o'%5D.
# I didn't have to convert the string, word to a list

phonetic_list = [phonetic_alphabet[letter] for letter in word if letter in phonetic_alphabet]
print(phonetic_list)

'''
student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    if row.student == "Angela":
        print(row.score)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
'''
