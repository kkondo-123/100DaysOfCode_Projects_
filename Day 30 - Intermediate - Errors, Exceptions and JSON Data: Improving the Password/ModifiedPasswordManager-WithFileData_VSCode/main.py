"""
Name: Kana Kondo
Date: 2025-07-11-Fri
Course: 100 Days of Code Day 30
Description: MODIFIED Password Manager (from day 29)
"""

from tkinter import * 
from tkinter import messagebox
import pyperclip  # Like day 29, used Python 3.8.10 Python version
import json

DATA_FILENAME = "data.json"

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
SEARCH_BUTTON_TEXT = "Search"

JSON_EMAIL_USERNAME = "email/username"
JSON_PASSWORD = "password"

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
    new_data = {
        website: {
            JSON_EMAIL_USERNAME: email_username,
            JSON_PASSWORD: password,
        }
    }

    if website == "" or password == "" or email_username == "":
        messagebox.askokcancel(title="Oops", message="Please don't leave any fields empty! \nEnter and fill all entries.")

    else:
        try: 
            with open(DATA_FILENAME, 'r') as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            data = new_data
        finally: 
            with open(DATA_FILENAME, 'w') as file:
                json.dump(data, file, indent=4)

        website_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #

def find_password():
    website = website_entry.get()

    pop_up_title = website
    pop_up_message = ''

    try: 
        with open(DATA_FILENAME, 'r') as file:
            data = json.load(file)
            if website in data:
                website_data = data[website]
                pop_up_message = f"Email/User: {website_data[JSON_EMAIL_USERNAME]}\nPassword: {website_data[JSON_PASSWORD]}"
            else:
                pop_up_message = f"No details for the website, {website} exists"
    except FileNotFoundError:
        pop_up_title = 'Error'
        pop_up_message = 'No Data File Found'
    finally:
        messagebox.showinfo(title=pop_up_title, message=pop_up_message)

        


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
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
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

search_button = Button(text=SEARCH_BUTTON_TEXT, width=13, font=FONT, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()
