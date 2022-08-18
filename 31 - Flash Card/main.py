from tkinter import *

import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pd.read_csv('data/french_words.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')
finally:
    current_card = {}


# ------------------------ Randomise word ------------------------ #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(card_background, image=front_img)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=current_card['French'], fill='black')
    flip_timer = window.after(4000, flip_card)


# --------------------------- Flip card -------------------------- #
def flip_card():
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')
    canvas.itemconfig(card_background, image=back_img)


# -------------------- Remove 1 card if known -------------------- #
def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv', index=False)
    next_card()


# ------------------------------ UI ------------------------------ #
# Window
window = Tk()
window.title("Flash card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(4000, flip_card)

# Canvas2
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(410, 263, image=front_img)
canvas.grid(column=0, row=0, columnspan=2)
card_title = canvas.create_text(400, 150, text='', font=('Ariel', 30, 'italic'))
card_word = canvas.create_text(400, 263, text='', font=('Ariel', 50, 'italic'))

# Buttons
cross = PhotoImage(file='images/wrong.png')
tick = PhotoImage(file='images/right.png')
wrong = Button(image=cross, highlightthickness=0, command=next_card)
wrong.grid(column=0, row=1)
right = Button(image=tick, highlightthickness=0, command=is_known)
right.grid(column=1, row=1)

next_card()

window.mainloop()
