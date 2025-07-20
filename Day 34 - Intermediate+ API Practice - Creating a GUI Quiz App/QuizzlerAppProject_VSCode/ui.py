"""
Name: Kana Kondo
Date: 2025-07-19-Sat
Course: 100 Days of Code Day 34
Description: Modified Quizzler Project - UI Class (From Day 17)
  - Using tkinter
* Python 3.8.10 * 
"""

from quiz_brain import QuizBrain
from tkinter import *

THEME_COLOR = "#375362"

TRUE_IMAGE_FILE = "images/true.png"
FALSE_IMAGE_FILE = "images/false.png"

WINDOW_TITLE = "Quizzler"
PADDING = 20
WINDOW_PADY = 50

CANVAS_WIDTH = 300
CANVAS_HEIGHT = 250
CANVAS_QUESTION_WIDTH = 280

BLACK_COLOR = "black"
WHITE_COLOR = "white"

CANVAS_FONT = ("Arial", 20, "italic")

class QuizInterface():

    def __init__(self, quiz_brain: QuizBrain):  # Expects a QuizBrain datatype to be passed in
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title(WINDOW_TITLE)
        self.window.config(padx=PADDING, pady=PADDING, bg=THEME_COLOR)

        # Add padding around each element (buttons, label): https://stackoverflow.com/questions/70383014/how-can-i-add-space-between-buton-and-label-in-tkinter
        self.create_canvas()
        self.create_buttons()
        self.create_labels()

        self.get_next_question()

        self.window.mainloop()

    def check_button_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def x_button_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)

    def get_next_question(self):
        if self.quiz.still_has_questions(): 
            self.canvas.config(bg=WHITE_COLOR)
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.config(bg=WHITE_COLOR)
            self.canvas.itemconfig(self.question, text="You've reached the end of the quiz.")
            self.check_button.config(state="disabled")
            self.x_button.config(state="disabled")

    def create_buttons(self):
        # Need to put 'self.' in front of image variables or else image won't show.  
        # This is why: https://web.archive.org/web/20201111190625id_/http://effbot.org/pyfaq/why-do-my-tkinter-images-not-appear.htm 
        #   Link from: https://stackoverflow.com/questions/16424091/why-does-tkinter-image-not-show-up-if-created-in-a-function
        self.check_img = PhotoImage(file=TRUE_IMAGE_FILE)
        self.x_img = PhotoImage(file=FALSE_IMAGE_FILE)

        self.check_button = Button(image=self.check_img, highlightthickness=0, padx=PADDING, pady=PADDING, command=self.check_button_pressed)
        self.x_button = Button(image=self.x_img, highlightthickness=0, padx=PADDING, pady=PADDING, command=self.x_button_pressed)

        self.check_button.grid(column=0, row=2)
        self.x_button.grid(column=1, row=2)

    def create_labels(self):
        self.score_label = Label(text="Score: 0", fg=WHITE_COLOR, bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

    def create_canvas(self):
        self.canvas = Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, highlightthickness=0, bg=WHITE_COLOR)
        self.question = self.canvas.create_text(
            int(CANVAS_WIDTH/2), 
            int(CANVAS_HEIGHT/2), 
            width=CANVAS_QUESTION_WIDTH,
            text="TEXT", 
            fill=BLACK_COLOR, 
            font=CANVAS_FONT
            ) 

        # Add padding to canvas: https://stackoverflow.com/questions/4174575/adding-padding-to-a-tkinter-widget-only-on-one-side
        self.canvas.grid(column=0, row=1, columnspan=2, padx=PADDING, pady=WINDOW_PADY)