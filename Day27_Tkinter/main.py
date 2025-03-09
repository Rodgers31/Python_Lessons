from tkinter import *
# import tkinter

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()
# my_label.pack(side="left")

my_label["text"] = "New text"
my_label.config(text="New text2")

# Button


def button_clicked():
    # my_label["text"] = "Button got clicked"
    new_text = input.get()
    my_label.config(text=new_text)
    print("I got clicked")


button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry

input = Entry(width=10)
input.pack()


window.mainloop()
