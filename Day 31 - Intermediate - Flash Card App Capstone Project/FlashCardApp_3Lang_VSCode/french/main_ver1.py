'''

'''

from tkinter import * 
import pandas
import random

WINDOW_PADDING = 50
WINDOW_TITLE = "Flashy"

TARGET_LANGUAGE = "French"
ORIGIN_LANGUAGE = "English"

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
FRENCH_WORDS_FILENAME = "data/french_words.csv"
WORDS_LEARN_FILENAME = "words_to_learn.csv"

timer = None
term = None 
answer = None
term_list = None
set_index = None

# ------------------------------------ DATA ------------------------------------ # 
# def fill_data():
#     global term_list

#     try:
#         with open(WORDS_LEARN_FILENAME, "r") as file:

  


def learned_words():
    global term_list
    
    get_term()
    term_list.pop(set_index)  # https://www.w3schools.com/python/python_lists_remove.asp

    new_data = pandas.DataFrame(term_list)
    new_data.to_csv(WORDS_LEARN_FILENAME, mode='w')

    # with open(WORDS_LEARN_FILENAME, "w") as file:


# ------------------------------------ CARD ------------------------------------ # 

data = pandas.read_csv(FRENCH_WORDS_FILENAME)
# term_list = [{row.French: row.English} for (index, row) in data.iterrows()]  # From Day 26
term_list = pandas.DataFrame.to_dict(data, orient="records")
# Angela uses: DataFrame.to_dict(orient="records")  # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_dict.html
print(term_list)


def get_term():
    global term, answer, timer, term_list  # Need "answer" to import as global variable so that answer is "modified" and not recognized as a local variable

    if timer is not None:
        window.after_cancel(timer)

    print(term_list)
    term_set = term_list.choice()
    term = term_set[TARGET_LANGUAGE]
    answer = term_set[ORIGIN_LANGUAGE]

    # set_index = random.randint(0, len(term_list) - 1)
    # term_set = term_list[set_index]
    # term = list(term_set.keys())[0]  # Since Angela used the DataFrame.to_dict(), she used the titles ("French", "English") to get the term and answer
    # answer = term_set[term]

    canvas.itemconfig(flashcard, image=front_flashcard_img)
    canvas.itemconfig(term_text, text=term)
    canvas.itemconfig(language_text, text=TARGET_LANGUAGE)

    count_down(3)

    # For some reason, when I use the code below, it flips card before 3 seconds is over
    # flip_card()

def flip_card():
    global answer

    canvas.itemconfig(flashcard, image=back_flashcard_img)
    canvas.itemconfig(term_text, text=answer)
    canvas.itemconfig(language_text, text=ORIGIN_LANGUAGE)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
# From Day 28 

def count_down(count):  # Angela used  window.after(3000, func=flip_card())
    global timer, answer

    timer_label.config(text=f"Timer: {count}")

    if count == 0: 
        flip_card()

    elif count > 0: 
        timer = window.after(1000, count_down, count - 1)


# ----------------------------------- UI SETUP ----------------------------------- # 

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

""" 
Instead of creating labels use the .create_text() of canvas since we will be putting it on the flashcard image
# Labels
language_label = Label(text="French", font=LANGUAGE_LABEL_FONT, bg="white", fg="black")  # https://stackoverflow.com/questions/64290131/how-to-change-the-text-color-using-tkinter-label
language_label.place(x=LANGUAGE_LABEL_POSITION[0], y=LANGUAGE_LABEL_POSITION[1])  # https://stackoverflow.com/questions/36921362/setting-the-position-of-tkinter-labels
term_label = Label(text="trouve", font=TERM_LABEL_FONT, bg="white", fg="black")
term_label.place(x=TERM_LABEL_POSITION[0], y=TERM_LABEL_POSITION[1])
"""

# Buttons
x_img = PhotoImage(file=WRONG_IMG_FILENAME)
# https://stackoverflow.com/questions/1529847/how-to-change-the-foreground-or-background-colour-of-a-tkinter-button-on-mac-os
x_button = Button(image=x_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=get_term)
x_button.grid(column=0, row=1)

check_img = PhotoImage(file=RIGHT_IMG_FILENAME)
check_button = Button(image=check_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=learned_words)
check_button.grid(column=1, row=1)

# Label
timer_label = Label(text="Timer: 0", font=TIMER_FONT, bg=BACKGROUND_COLOR, fg="black")
timer_label.place(x=370, y=-40)

window.mainloop()
