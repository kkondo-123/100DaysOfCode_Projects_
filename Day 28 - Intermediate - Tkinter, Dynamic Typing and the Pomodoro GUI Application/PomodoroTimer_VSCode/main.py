"""
Name: Kana Kondo
Date: 2025-07-09-Wed to 2025-07-10-Thu
Course: 100 Days of Code Day 28
Description: Pomodoro Timer Project
"""

from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
# https://colorhunt.co/
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"

reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 

# Using recursion to loop through start_timer() and count_down()

def start_timer():
    global reps
    reps += 1

    work_sec = 2 # WORK_MIN * 60
    short_break_sec = 5 # SHORT_BREAK_MIN * 60
    long_break_sec = 3 # LONG_BREAK_MIN * 60

    print(f"reps = {reps}")
    if reps == 8:  # Rep 8: Long break
        timer_label.config(text="Long Break", fg=RED)
        count_down(long_break_sec)
    elif reps > 8:  # Timer done and reset (Termination of recursion)
        reps = 0
    elif reps % 2 == 0:  # Rep 2, 4, 6: Short break
        timer_label.config(text="Short Break", fg=PINK)
        count_down(short_break_sec)
    else: # Rep 1, 3, 5, 7: Work
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)


    # Issue with overlapping times -> Solved by calling start_timer() from count_down() and adding recursion terminator

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global timer

    count_min = math.floor(count / 60)  # Round down to smallest integer
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    time = f"{count_min}:{count_sec}"
    canvas.itemconfig(timer_text, text=time)

    if count == 0:  # Else statement after "if count > 0:" would have worked as well
        start_timer()
        check_label.config(text=f"{(reps // 2) * CHECK_MARK}")  # Instead of // could use math.floor()
    elif count > 0:
        timer = window.after(1000, count_down, count - 1)
    



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Tomato Picture and Timer
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
# canvas.pack()
canvas.grid(column=1, row=1)

# Lablels
timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 45, "normal"), bg=YELLOW)
timer_label.grid(column=1, row=0)

check_label = Label(fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)

# Buttons
start_button = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(column=2, row=2)



window.mainloop()
