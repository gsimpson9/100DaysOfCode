# ---------------------------- CONSTANTS ------------------------------- #
from tkinter import *
import time

sec = 9506

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
reps = 0
stage = ''
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global stage
    global reps
    global timer_text
    reps = 0
    stage = ''
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    my_label.config(text='Timer')
    checkmarks.config(text='')


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        countdown(long_break_sec)
        my_label.config(text='Long Break', fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        my_label.config(text='Short Break', fg=PINK)
    else:
        countdown(work_sec)
        my_label.config(text='Work', fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global reps
    global stage
    convert = time.strftime("%M:%S", time.gmtime(count))
    canvas.itemconfig(timer_text, text=convert)
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            stage += '✔'
            checkmarks.config(text=stage)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Label
my_label = Label(text="Timer", font=(FONT_NAME, 28), fg=GREEN, bg=YELLOW)
my_label.grid(column=1, row=0)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 30, 'bold'))
canvas.grid(column=1, row=1)

# Start Button
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# Reset Button
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# Check Marks
checkmarks = Label(text="", font=(FONT_NAME, 12), fg=GREEN, bg=YELLOW)
checkmarks.grid(column=1, row=3)

window.mainloop()
