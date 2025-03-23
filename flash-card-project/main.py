import random
from tkinter import *

import pandas

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
# the type of the key-value pairs can be customized with the parameters
# ‘records’ : list like [{column -> value}, … , {column -> value}]
to_learn = data.to_dict(orient="records")
current_card = {}


def generate():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    choice = (random.choice(to_learn))
    print(choice)
    canvas.itemconfig(the_word, text=choice["French"], fill="black")
    canvas.itemconfig(the_title, text="French", fill="black")
    canvas.itemconfig(card, image=card_front_image)
    current_card = choice
    flip_timer = window.after(3000, func=flip)


def flip():
    global current_card
    canvas.itemconfig(card, image=card_back_img)
    canvas.itemconfig(the_word, text=current_card["English"], fill="white")
    canvas.itemconfig(the_title, text="English", fill="white")
    current_card = {}


window = Tk()
window.title("flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip)


canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card = canvas.create_image(400, 256, image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
the_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
the_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=generate)
unknown_button.grid(row=1, column=0)


check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=generate)
known_button.grid(column=1, row=1)

generate()
window.mainloop()