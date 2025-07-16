"""
Name: Kana Kondo
Date: 2025-07-16-Wed
Course: 100 Days of Code Day 31 (Revised, Mandarin Words)
Description: Flash Card Project - Code to get data (mandarin words to translate)
"""

import pandas
from googletrans import Translator

# https://stackoverflow.com/questions/68694037/python-googletrans-module-not-translating
import asyncio

translated_txt = None

async def TranslateText(text_to_translate, src_lang, dest_lang):
  global translated_txt
  async with Translator() as translator:
    result = await translator.translate(text_to_translate, src=src_lang, dest=dest_lang)
    translated_txt = result
# asyncio.run(TranslateText())

'''
Install Translation (google translate) in VSCode: https://www.youtube.com/watch?v=P1uHDPpe_04&t=172s
(Assuming that pip is already installed, covered in Day 18)
 1. Open 'zsh' terminal and type 'python3' -> Press tab and look at see the Python versions. 
    Continue to type 'python3 -m venv env' and press enter.
 2. A file called 'env' should appear.  Type 'source env/bin/activate'. 
    (env/bin/activate is the file directory to the file called 'activate')
 3. Type 'pip3 install googletrans' -> A bunch of commands/lines should run in terminal.
    Bottom line should mention: 'Successfully installed .... googletrans...'
    (The module error for pandas should dissapear here)
Link to details: https://pypi.org/project/googletrans/
'''

TARGET_LANGUAGE = "Mandarin"
ORIGIN_LANGUAGE = "English"

MANDARIN_LIST_FILEPATH = "data/hsk_words.csv"
SIMPLIFIED_MANDARIN_HEADER = "word_simplified"
PINYIN_HEADER = "pinyin"

NEW_MANDARIN_WORDS_FILEPATH = "data/mandarin_words.csv"  # File Error dissapeared when individually opened "Mandarin" File

# https://py-googletrans.readthedocs.io/en/latest/
KEYWORD_ENGLISH = "en"
KEYWORD_MANDARIN = "zh-cn"  

translator = Translator()

# https://github.com/alyssabedard/chinese-hsk-and-frequency-lists/blob/master/hsk%203.0%20%20-%20words.csv

data = pandas.read_csv(MANDARIN_LIST_FILEPATH)
hsk_words_list = pandas.DataFrame.to_dict(data, orient="records")
mandarin_words_list = []

for index in range(0, 102):
    # Need to make sure new_word dictionary is reset so that it doesn't append 101 of {'Mandarin': '放学 (fàng xué)', 'English': ''} to mandarin_word_list 
    new_word = {}

    dictionary_set = hsk_words_list[index]
    new_word[TARGET_LANGUAGE] = f"{dictionary_set[SIMPLIFIED_MANDARIN_HEADER]} ({dictionary_set[PINYIN_HEADER]})" 
    asyncio.run(TranslateText(text_to_translate=dictionary_set[SIMPLIFIED_MANDARIN_HEADER], src_lang=KEYWORD_MANDARIN, dest_lang=KEYWORD_ENGLISH))
    new_word[ORIGIN_LANGUAGE] = f"{translated_txt.text}"  # Tap into the text attribute to get the translation: https://stackoverflow.com/questions/68983760/attributeerror-coroutine-object-has-no-attribute-text

    mandarin_words_list.append(new_word)

new_data = pandas.DataFrame(mandarin_words_list)
new_data.to_csv(NEW_MANDARIN_WORDS_FILEPATH, mode='w', index=False)
