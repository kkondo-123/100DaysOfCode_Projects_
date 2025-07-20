"""
Name: Kana Kondo
Date: 2025-07-19-Sat
Course: 100 Days of Code Day 34
Description: Modified Quizzler Project - Data Class (From Day 17)
  - Using Open Trivia Database API
* Python 3.8.10 * 
"""

import requests


# https://opentdb.com/api_config.php

# https://opentdb.com/api.php?amount=10&category=31&type=boolean

AMOUNT_QUESTIONS = 10
ANIME_CATEGORY_NUM = 31
QUESTION_TYPE = 'boolean'
TRIVIA_API_URL = 'https://opentdb.com/api.php?'

SINGLEQUOTE_PLACEHOLDER = '&#039;'
DOUBLEQUOTE_PLACEHOLDER = '&quot;'
AMPERSAND_PLACEHOLDER = '&amp;'

PLACEHOLDERS = {
    SINGLEQUOTE_PLACEHOLDER: "'",
    DOUBLEQUOTE_PLACEHOLDER: '"',
    AMPERSAND_PLACEHOLDER: '&',
}


JSON_CATEOGORY_HEADER = 'category'
JSON_QUESTION_HEADER = 'question'

parameters = {
    'amount': AMOUNT_QUESTIONS,
    'type': QUESTION_TYPE,
    # 'category': ANIME_CATEGORY_NUM,
}

response = requests.get(url=TRIVIA_API_URL, params=parameters)
response.raise_for_status()
data = response.json()['results']

# In quiz_brain.py, Angela uses html.unescape() 
# for question in data:
#     for placeholder in PLACEHOLDERS:
#         question[JSON_CATEOGORY_HEADER] = question[JSON_CATEOGORY_HEADER].replace(placeholder, PLACEHOLDERS[placeholder])
#         question[JSON_QUESTION_HEADER] = question[JSON_QUESTION_HEADER].replace(placeholder, PLACEHOLDERS[placeholder])

question_data = data
