from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    web = web_entry.get()
    email = user_entry.get()
    pass_w = pass_entry.get()
    print(len(web))
    if len(web) == 0 or len(pass_w) == 0:
        print(web, pass_w)
        messagebox.showinfo(title="Oops", message=f"Please dont leave any fields empty!")

    else:

        is_ok = messagebox.askokcancel(title=web, message=f"These are the details entered: \nEmail: {email} "                   
                                                f"\nPassword: {pass_w} \nIs it ok to save?")\

        if is_ok:
            with open("data.tx", mode="a") as file:
                file.write(f"{web} | {email} | {pass_w} \n")

            web_entry.delete(0, 'end')
            pass_entry.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

# website section
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)
web_entry = Entry(width=35)
web_entry.focus()
web_entry.grid(column=1, row=1, columnspan=2, sticky="EW")

# email/username section
user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)
user_entry = Entry(width=35)
# insert string at the very begging of the entry
user_entry.insert(0, "otienor986@gmail.com")
user_entry.grid(column=1, row=2, columnspan=2, sticky="EW")

# password section
pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)
pass_entry = Entry(width=21)
pass_entry.grid(column=1, row=3, sticky="EW")
pass_button = Button(text="Generate Password")
pass_button.grid(column=2, row=3, sticky="EW")

# Add button
# When combined as "EW", it means the widget will stretch horizontally to fill the entire width of the grid cell
# from the left (West) to the right (East). This is commonly used to make buttons or other widgets expand to fill
# the available horizontal space.
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()