"""
Name: Kana Kondo
Date: 2025-06-30-Mon
Course: 100 Days of Code Day 17
Description: Quiz Project - Quiz Brain Class
"""

# TODO 5: Create a class called QuizBrain
class QuizBrain:

    # TODO 6: Create an __init__() method
    def __init__(self, q_list):

        # TODO 7: Initialise the question_number to 0.
        self.question_number = 0

        # TODO 8: Initialise the question_list to an input.
        self.question_list = q_list

        self.score = 0


    # TODO 9: Create a method called next_question(). Retrieve the item at the current question_number from the question_list.
    def next_question(self):

        # TODO 10: Use the input() function to show the user the Question text and ask for the user's answer.
        # WHY?: current_quesiton instead of self.current_question?
        # self.current_question = self.question_list[self.question_number]

        current_question = self.question_list[self.question_number]

        self.question_number += 1  

        # Instead of increasing inside input function, increase it to actual variable
        # input(f"Q.{self.question_number + 1}: {self.current_question.text} (True/False)?: ")

        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")

        # No return statement. 

        self.check_answer(user_answer, current_question.answer)


    # TODO 11: Create method called still_has_questions()
    def still_has_questions(self):

        # TODO 12: Return a boolean depending on the value of question_number.
        return self.question_number < len(self.question_list)

    # TODO 14: Add the score feature to the check_answer() method
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right! ")
            self.score += 1
        else:
            print("That's wrong. ")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
