"""
Name: Kana Kondo
Date: 2025-07-10-Thu
Course: 100 Days of Code Day 29
Description: Password Manager
"""

from tkinter import * 
from tkinter import messagebox
import pyperclip

'''
To use the pyperclip module: https://pypi.org/project/pyperclip/
1) Ensure Python version is Python 3.8.10 (Like Day 25 where Python Pandas was installed)
2) Typed 'python3 -m venv env'
3) Typed 'source env/bin/activate'
4) Typed 'pip3 install pyperclip' as mentioned in the link above (https://pypi.org/project/pyperclip/)
5) Saw the error dissapear (yellow line/linter gone from pyperclip in code)
'''

DATA_FILENAME = "data.txt"

WINDOW_TITLE = "Password Manager"
WINDOW_PADX = 50
WINDOW_PADY = 50

PICTURE_FILENAME = "logo.png"
CANVAS_POSITIONING = 100
CANVAS_DIMENSION = 200

WEBSITE_LABEL_TEXT = "Website:"
EMAIL_USERNAME_LABEL_TEXT = "Email/Username:"
PASSWORD_LABEL_TEXT = "Password:"
FONT = ("Arial", 14, "normal")

GENERATE_PASSWORD_TEXT = "Generate Password"
ADD_BUTTON_TEXT = "Add"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# DAY 5 Password Generator Project + Day 26 list comprehension

import random

def create_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(1, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password = [random.choice(letters) for l in range(nr_letters)]
    password += [random.choice(symbols) for l in range(nr_symbols)]
    password += [random.choice(numbers) for l in range(nr_numbers)]

    random.shuffle(password)
    password = ''.join(password)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    password = password_entry.get()
    email_username = email_username_entry.get()

    # messagebox.showinfo(title="Title", message="Message")
        
    if website == "" or website == None or password == "" or password == None or email_username == "" or email_username == None:
        # Could check if len(website) == 0 (length of string is 0)
        messagebox.askokcancel(title="Oops", message="Please don't leave any fields empty! \nEnter and fill all entries.")

    else:
        input_is_ok = f"These are the details entered: \nEmail/User: {email_username} \nPassword: {password}\nIs it okay to save? "
        messagebox.askokcancel(title=website, message=input_is_ok)

        if input_is_ok:
            new_datum = f"{website} | {email_username} | {password}\n"

            with open(DATA_FILENAME, "a") as file:
                # Append file mode: https://www.geeksforgeeks.org/python/python-append-to-a-file/
                file.write(new_datum)
            
            # https://stackoverflow.com/questions/27966626/how-to-clear-delete-the-contents-of-a-tkinter-text-widget
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title(WINDOW_TITLE)
window.config(padx=WINDOW_PADX, pady=WINDOW_PADY)

# MyPass Picture
canvas = Canvas(width=CANVAS_DIMENSION, height=CANVAS_DIMENSION, highlightthickness=0)
logo_img = PhotoImage(file=PICTURE_FILENAME)
canvas.create_image(CANVAS_POSITIONING, CANVAS_POSITIONING, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text=WEBSITE_LABEL_TEXT, font=FONT)
website_label.grid(column=0, row=1)

email_username_label = Label(text=EMAIL_USERNAME_LABEL_TEXT, font=FONT)
email_username_label.grid(column=0, row=2)

password_label = Label(text=PASSWORD_LABEL_TEXT, font=FONT)
password_label.grid(column=0, row=3)

# Entry
website_entry = Entry(width=37)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_username_entry = Entry(width=37)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0, "myEmail@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Button
generate_password_button = Button(text=GENERATE_PASSWORD_TEXT, width=13, font=FONT, command=create_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text=ADD_BUTTON_TEXT, font=FONT, width=39, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
