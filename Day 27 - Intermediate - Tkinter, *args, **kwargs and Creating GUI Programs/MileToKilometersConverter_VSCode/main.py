"""
Name: Kana Kondo
Date: 2025-07-09-Wed
Course: 100 Days of Code Day 27
Description: Mile to Kilemeters Converter Project
"""

from tkinter import *

TITLE_NAME = "Mile to Km Converter"
MILES_LABEL_TEXT = "Miles"
EQUAL_LABEL_TEXT = "is equal to"
KM_LABEL_TEXT = "Km"
CONVERTED_VAL_TEXT = 0
CALCULATE_BUTTON_TEXT = "Calculate"

FONT = ("Arial", 12, "normal")

window = Tk()
window.title(TITLE_NAME)
window.minsize(width=100, height=100)
window.config(padx=50, pady=50)

# Labels
miles_label = Label(text=MILES_LABEL_TEXT, font=FONT)
miles_label.grid(column=2, row=0)

equal_to_label = Label(text=EQUAL_LABEL_TEXT, font=FONT)
equal_to_label.grid(column=0, row=1)

kilometer_label = Label(text=KM_LABEL_TEXT, font=FONT)
kilometer_label.grid(column=2, row=1)

converted_val_label = Label(text=CONVERTED_VAL_TEXT, font=FONT)
converted_val_label.grid(column=1, row=1)

# Entry 
input = Entry(width=10)
input.insert(0, "0")  # https://stackoverflow.com/questions/16373887/how-to-set-the-text-value-content-of-an-entry-widget-using-a-button-in-tkinter
input.grid(column=1, row=0)

def convert_miles_to_km():
    # 1 mile = 1.609 km
    miles_val = float(input.get())
    km_val = round(miles_val * 1.609)
    converted_val_label.config(text=f"{km_val}")

def calculate_button_click(miles_input, calculated_label):
    miles_input = float(input.get())
    km_val = round(miles_input * 1.609)
    calculated_label.config(text=f"{km_val}")

# Buttons
# Ver #1 does not pass in arguments in the function, takes input directly and directly modifies label
# calculate_button = Button(text=CALCULATE_BUTTON_TEXT, font=FONT, command=convert_miles_to_km)

# Ver #2 passes arguments the input (Entry) and label as arguments in the function
calculate_button = Button(text=CALCULATE_BUTTON_TEXT, font=FONT, command= lambda: calculate_button_click(input, converted_val_label))
# Lambda function:
#   https://stackoverflow.com/questions/6920302/how-to-pass-arguments-to-a-button-command-in-tkinter
#   https://www.w3schools.com/python/python_lambda.asp

calculate_button.grid(column=1, row=2)

window.mainloop()
