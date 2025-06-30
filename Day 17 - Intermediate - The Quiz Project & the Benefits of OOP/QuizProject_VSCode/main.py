"""
Name: Kana Kondo
Date: 2025-06-30-Mon
Course: 100 Days of Code Day 17
Description: Quiz Project - Main Class
"""


from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

QUESTION = 'question'
ANSWER = 'correct_answer'
question = []

# TODO 2: Write a for loop to iterate over the question_data.
for datum in question_data:
    # TODO 3: Create a Question object from each entry in question_data. 
    # TODO 4: Append each Question object to the question_bank. 
    question.append(Question(datum[QUESTION], datum[ANSWER]))


quiz = QuizBrain(question)

print("\n\n")

# TODO 13: Use the while loop to show the next question until the end
while quiz.still_has_questions(): # if quiz still has questions remaining
    quiz.next_question()
    print("\n")

# TODO 15: Add a message to display at end of quiz and show the user's final score. 
print("You've completed the quiz! ")
print(f"Your final score was: {quiz.score}/{quiz.question_number}\n")
