"""
Name: Kana Kondo
Date: 2025-06-30-Mon
Course: 100 Days of Code Day 17
Description: Quiz Project - Question Class
"""

# TODO 1: Create a Question class with an __init()__ method with two attributes: text and answer attribute

class Question:
    
    def __init__(self, q_text, q_answer):
        
        self.text = q_text
        self.answer = q_answer

# new_q = Question('You are a human', 'True')
# print(f"text = {new_q.text}\nanswer = {new_q.answer}")
