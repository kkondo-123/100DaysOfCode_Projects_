"""
Name: Kana Kondo
Date: 2025-07-14-Mon - 2025-07-16-Wed
Course: 100 Days of Code Day 31 (Revised, Mandarin Words)
Description: Flash Card Project - Main Code
 - Before runnig code in this file, run the japanese_data.py file to create the japanese_words.csv
"""

from tkinter import * 
import pandas
import random
from japanese_data import TARGET_LANGUAGE, ORIGIN_LANGUAGE, NEW_JAPNESE_WORDS_FILEPATH

WINDOW_PADDING = 50
WINDOW_TITLE = "Flashy"

BACKGROUND_COLOR = "#B1DDC6"
TIMER_FONT = ("Ariel", 20, "bold") 
LANGUAGE_LABEL_POSITION = (400, 150)
LANGUAGE_LABEL_FONT = ("Ariel", 40, "italic")  # https://www.tutorialspoint.com/python/tk_fonts.htm
TERM_LABEL_POSITION = (400, 263)
TERM_LABEL_FONT = ("Ariel", 60, "bold")

WRONG_IMG_FILENAME = "./images/wrong.png"
RIGHT_IMG_FILENAME = "./images/right.png"
FRONT_CARD_FILENAME = "./images/card_front.png"
BACK_CARD_FILENAME = "images/card_back.png"
MANDARIN_WORDS_FILENAME = NEW_JAPNESE_WORDS_FILEPATH
WORDS_LEARN_FILENAME = "words_to_learn.csv"

timer = None
term_list = None
term_set = None
count = 0
data = None

# ------------------------------------ DATA ------------------------------------ # 

def learned_word():
    global term_list
    
    get_term()
    term_list.remove(term_set) # https://www.w3schools.com/python/python_lists_remove.asp

    new_data = pandas.DataFrame(term_list)
    new_data.to_csv(WORDS_LEARN_FILENAME, mode='w', index=False)  # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_dict.html

def load_files():  # Run this at the beginning of the program
    global data, term_list

    try: 
        data = pandas.read_csv(WORDS_LEARN_FILENAME)
        # print("\nNO ERROR")
    except FileNotFoundError:
        data = pandas.read_csv(MANDARIN_WORDS_FILENAME)
        # print("\nERROR")
    finally:
        term_list = pandas.DataFrame.to_dict(data, orient="records")  

# ------------------------------------ CARD ------------------------------------ # 

def get_term():
    global timer, term_set

    if timer is not None:
        window.after_cancel(timer)

    term_set = random.choice(term_list)
    # print(term_set)

    canvas.itemconfig(flashcard, image=front_flashcard_img)
    canvas.itemconfig(term_text, text=term_set[TARGET_LANGUAGE])
    canvas.itemconfig(language_text, text=TARGET_LANGUAGE)

    count_down(3)

def flip_card():
    global term_set
    canvas.itemconfig(flashcard, image=back_flashcard_img)
    canvas.itemconfig(term_text, text=term_set[ORIGIN_LANGUAGE])
    canvas.itemconfig(language_text, text=ORIGIN_LANGUAGE)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
# From Day 28 

def count_down(count):
    global timer

    timer_label.config(text=f"Timer: {count}")

    if count == 0: 
        flip_card()

    elif count > 0: 
        timer = window.after(1000, count_down, count - 1)


# ----------------------------------- UI SETUP ----------------------------------- # 

load_files()

window = Tk()
window.minsize(width=800, height=700)  # https://www.geeksforgeeks.org/python/how-to-set-a-tkinter-window-with-a-constant-size/
window.title(WINDOW_TITLE)
window.config(padx=WINDOW_PADDING, pady=WINDOW_PADDING, bg=BACKGROUND_COLOR)

# Flashcard Picture -> Refer to Day 28
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
back_flashcard_img = PhotoImage(file=BACK_CARD_FILENAME)
front_flashcard_img =  PhotoImage(file=FRONT_CARD_FILENAME)
flashcard = canvas.create_image(400, 263, image=front_flashcard_img)
language_text = canvas.create_text(LANGUAGE_LABEL_POSITION, text="Title", font=LANGUAGE_LABEL_FONT, fill="black")  # https://stackoverflow.com/questions/64290131/how-to-change-the-text-color-using-tkinter-label
term_text = canvas.create_text(TERM_LABEL_POSITION, text="word", font=TERM_LABEL_FONT, fill="black")
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
x_img = PhotoImage(file=WRONG_IMG_FILENAME)
# https://stackoverflow.com/questions/1529847/how-to-change-the-foreground-or-background-colour-of-a-tkinter-button-on-mac-os
x_button = Button(image=x_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=get_term)
x_button.grid(column=0, row=1)

check_img = PhotoImage(file=RIGHT_IMG_FILENAME)
check_button = Button(image=check_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=learned_word)
check_button.grid(column=1, row=1)

# Label
timer_label = Label(text=f"Timer: {count}", font=TIMER_FONT, bg=BACKGROUND_COLOR, fg="black")
timer_label.place(x=370, y=-40)

window.mainloop()
