"""
Name: Kana Kondo
Date: 2025-07-16-Wed
Course: 100 Days of Code Day 32
Description: Birthday Wisher
"""

##################### Normal Starting Project ######################

import datetime as dt
import pandas
import random
import smtplib

BIRTHDAY_DATA_FILENAME = "birthdays.csv"
NAME_HEADING = 'name'
EMAIL_HEADING = 'email'
YEAR_HEADING = 'year'
MONTH_HEADING = 'month'
DAY_HEADING = 'day'

NAME_PLACEHOLDER = "[NAME]"

SENDER_EMAIL = 'YOUREMAIL'
APP_PASSWORD = 'YOURAPPPASSWORD'

LETTERS_FILE = [
    "letter_templates/letter_1.txt", 
    "letter_templates/letter_2.txt",
    "letter_templates/letter_3.txt"
]

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. e.g.
#name,email,year,month,day
#YourName,your_own@email.com,today_year,today_month,today_day

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Create a tuple from today's month and day using datetime. e.g.
# today = (today_month, today_day)

now = dt.datetime.now()
month = now.month
day = now.day

today = (month, day)

# HINT 2: Use pandas to read the birthdays.csv

data = pandas.read_csv(BIRTHDAY_DATA_FILENAME)
# people_list = pandas.DataFrame.to_dict(data, orient="records") 

# HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:
# birthdays_dict = {
#     (birthday_month, birthday_day): data_row
# }
#Dictionary comprehension template for pandas DataFrame looks like this:
# new_dict = {new_key: new_value for (index, data_row) in data.iterrows()}
#e.g. if the birthdays.csv looked like this:
# name,email,year,month,day
# Angela,angela@email.com,1995,12,24
#Then the birthdays_dict should look like this:
# birthdays_dict = {
#     (12, 24): Angela,angela@email.com,1995,12,24
# }

birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows() if (data_row.month, data_row.day) == today}  
# I got an error because I put f"{data_row}" instead of data_row in the line above, which turned it into a string

#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT 1: Think about the relative file path to open each letter. 
# HINT 2: Use the random module to get a number between 1-3 to pick a randome letter.
# HINT 3: Use the replace() method to replace [NAME] with the actual name. https://www.w3schools.com/python/ref_string_replace.asp
if today in birthdays_dict:
    letter = []
    birthday_person = birthdays_dict[today]  # Assuming only 1 birthday per day

    letter_filepath = random.choice(LETTERS_FILE)
    with open(letter_filepath, "r") as file:
        for line in file:
            new_line_letter = line.replace(NAME_PLACEHOLDER, birthday_person[NAME_HEADING])
            letter.append(new_line_letter)

    # 4. Send the letter generated in step 3 to that person's email address.
    # HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
    # HINT 2: Remember to call .starttls()
    # HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
    # HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.

    receiver_email = birthday_person[EMAIL_HEADING]
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:  # The email here is: smpt.gmail.com and not my actual email!
        # Did not include 'port=587', https://stackoverflow.com/questions/50624003/python-freezes-on-smtplib-smtpsmtp-gmail-com-587
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=APP_PASSWORD)
        connection.sendmail(
            from_addr=SENDER_EMAIL,
            to_addrs=receiver_email,
            msg=f"Subject: Happy Birthday\n\n{''.join(letter)}"  # https://www.datacamp.com/tutorial/how-to-convert-a-list-to-a-string-in-python
        )

