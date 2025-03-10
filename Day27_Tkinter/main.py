from tkinter import *
# import tkinter


def button_clicked():
    # my_label["text"] = "Button got clicked"
    new_text = input.get()
    my_label.config(text=new_text)
    print("I got clicked")


window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
# my_label.pack()
my_label["text"] = "New text"
my_label.config(text="New text2")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)
# my_label.place(x=100, y=200)
# my_label.pack(side="left")

# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)
# button.pack(side="left")

# Button
new_button = Button(text="Click Me2", command=button_clicked)
new_button.grid(column=2, row=0)
# button.pack(side="left")

# Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)
# input.pack(side="left")




window.mainloop()
