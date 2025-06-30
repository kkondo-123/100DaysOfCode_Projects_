"""
Name: Kana Kondo
Date: 2025-06-30-Mon
Course: 100 Days of Code Day 17
Description: Quiz Project - Data
"""

# Link: https://opentdb.com/api_config.php
# URL: https://opentdb.com/api.php?amount=10&category=31&difficulty=easy&type=boolean
    # Number of Questions: 10
    # Category: Entertainment: Japanese Anime & Manga
    # Difficulty: Easy, 
    # Type: True / False, 
    # Encoding: Default Encoding
# Replaced '&quot;' with ' (single quote)
# Replaced '&amp;' with & (ampersand), Reference: https://stackoverflow.com/questions/9084237/what-is-amp-used-for

# To format code: PyCharm = Highlight JSON and press 'Reformat Code' x2
# I used: https://jsonformatter.org/

question_data = [
    {
      "type": "boolean",
      "difficulty": "easy",
      "category": "Entertainment: Japanese Anime & Manga",
      "question": "In the 1988 film 'Akira', Tetsuo ends up destroying Tokyo.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "type": "boolean",
      "difficulty": "easy",
      "category": "Entertainment: Japanese Anime & Manga",
      "question": "In Chobits, Hideki found Chii in his apartment.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "type": "boolean",
      "difficulty": "easy",
      "category": "Entertainment: Japanese Anime & Manga",
      "question": "In the 'To Love-Ru' series, Golden Darkness is sent to kill Lala Deviluke.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "type": "boolean",
      "difficulty": "easy",
      "category": "Entertainment: Japanese Anime & Manga",
      "question": "In the 'Toaru Kagaku no Railgun' anime,  espers can only reach a maximum of level 6 in their abilities.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "type": "boolean",
      "difficulty": "easy",
      "category": "Entertainment: Japanese Anime & Manga",
      "question": "No Game No Life first aired in 2014.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "type": "boolean",
      "difficulty": "easy",
      "category": "Entertainment: Japanese Anime & Manga",
      "question": "In Kill La Kill, the weapon of the main protagonist is a katana. ",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "type": "boolean",
      "difficulty": "easy",
      "category": "Entertainment: Japanese Anime & Manga",
      "question": "Studio Ghibli is a Japanese animation studio responsible for the films 'Wolf Children' and 'The Boy and the Beast'.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "type": "boolean",
      "difficulty": "easy",
      "category": "Entertainment: Japanese Anime & Manga",
      "question": "In the 'Melancholy of Haruhi Suzumiya' series, the narrator goes by the nickname Kyon.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "type": "boolean",
      "difficulty": "easy",
      "category": "Entertainment: Japanese Anime & Manga",
      "question": "The name of the attack 'Kamehameha' in Dragon Ball Z was named after a famous king of Hawaii.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "type": "boolean",
      "difficulty": "easy",
      "category": "Entertainment: Japanese Anime & Manga",
      "question": "Clefairy was intended to be Ash&#039;s starting Pok&eacute;mon in the pilot episode of the cartoon.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    }
]


