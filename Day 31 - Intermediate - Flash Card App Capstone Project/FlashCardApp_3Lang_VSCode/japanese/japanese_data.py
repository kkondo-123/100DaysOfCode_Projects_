"""
Name: Kana Kondo
Date: 2025-07-16-Wed
Course: 100 Days of Code Day 31 (Revised, Japanese Words)
Description: Flash Card Project - Code to get data (japanese words to translate)
"""

# Got data from: https://github.com/JackShannon/1000-most-common-words/blob/master/1000-most-common-japanese-words.txt

from googletrans import Translator
import pandas
import asyncio

translator = Translator()

translated_txt = None

WORD_LIST_FILEPATH = "data/1000-most-common-japanese-words.txt"

TARGET_LANGUAGE = "Japanese"
ORIGIN_LANGUAGE = "English"

# https://py-googletrans.readthedocs.io/en/latest/
KEYWORD_ENGLISH = "en"
KEYOWRD_JAPANESE = "ja"  

NEW_JAPNESE_WORDS_FILEPATH = "data/japanese_words.csv"

async def TranslateText(text_to_translate, src_lang, dest_lang):
  global translated_txt
  async with Translator() as translator:
    result = await translator.translate(text_to_translate, src=src_lang, dest=dest_lang)
    translated_txt = result

japanese_words_list = []

with open(WORD_LIST_FILEPATH, "r") as file:
    index = 0
    while index < 102:
      line = file.readline()
      new_word = {}

      new_word[TARGET_LANGUAGE] = line.strip()
      asyncio.run(TranslateText(text_to_translate=new_word[TARGET_LANGUAGE], src_lang=KEYOWRD_JAPANESE, dest_lang=KEYWORD_ENGLISH))
      new_word[ORIGIN_LANGUAGE] = f"{translated_txt.text}"

      japanese_words_list.append(new_word)

      index += 1

print("LOADED DATA")

new_data = pandas.DataFrame(japanese_words_list)
new_data.to_csv(NEW_JAPNESE_WORDS_FILEPATH, mode='w', index=False)