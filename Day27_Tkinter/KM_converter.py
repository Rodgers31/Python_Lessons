from tkinter import *

window = Tk()
window.title("Mile to Km converter")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)


# buttons
def calculate():
    miles = (miles_value.get())
    kilometer = round(int(miles) * 1.60934)
    mid_label.config(text=kilometer)


# Left
lef_label = Label(text="is equal to", font=("Arial", 10))
lef_label.grid(column=2, row=2)
lef_label.config(padx=5)

# Middle
miles_value = Entry(width=10)
miles_value.grid(column=3, row=0)

mid_label = Label(text="0", font=("Arial", 10))
mid_label.grid(column=3, row=2)


mid_button = Button(text="Calculate", command=calculate)
mid_button.grid(column=3, row=3)
# Right
right_label_m = Label(text="Miles", font=("Arial", 10))
right_label_m.grid(column=4, row=0)
right_label_m.config(padx=5)

right_label_k = Label(text="Km", font=("Arial", 10))
right_label_k.grid(column=4, row=2)
right_label_k.config(padx=5)

window.mainloop()