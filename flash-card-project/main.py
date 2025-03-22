import random
from tkinter import *

import pandas
from pandas import *

BACKGROUND_COLOR = "#B1DDC6"


window = Tk()
window.title("flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


def generate():
    french = pandas.read_csv("data/french_words.csv")
    words = {value.French: value.English for (key, value) in french.iterrows()}
    choice = (random.choice(list(words.items())))
    canvas.itemconfig(the_word, text=choice[0])


canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 256, image=card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
the_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=generate)
known_button.grid(column=1, row=1)


window.mainloop()