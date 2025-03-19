from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # ****Changed to list comprehension****
    # password_list = []
    #
    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))

    password_list = [random.choice(letters) for _ in range(nr_letters)]

    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]

    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)

    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)
    # used join instead of for loop
    password = "".join(password_list)

    # password = ""
    # for char in password_list:
    #     password += char

    # inserted newly created password in entry
    pass_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def pass_search():
    website = web_entry.get()
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
        print(data)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file Found.")
    else:
        try:
            for _ in data:
                email = data[f"{website}"]["email"]
                password = data[f"{website}"]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")
        except KeyError:
            messagebox.showinfo(title=f"{website}", message=f"{website} not yet stored")


def save_password():
    website = web_entry.get()
    email = user_entry.get()
    pass_w = pass_entry.get()

    new_data = {website: {
        "email": email,
        "password": pass_w
    }
    }
    if len(website) == 0 or len(pass_w) == 0:
        messagebox.showinfo(title="Oops", message=f"Please dont leave any fields empty!")

    else:

        # is_ok = messagebox.askokcancel(title=web, message=f"These are the details entered: \nEmail: {email} "
        # write json data                                                   f"\nPassword: {pass_w} \nIs it ok to save?")
        # read mode
        try:
            with open("data.json", mode="r") as data_file:
                # json.dump(new_data, data_file, indent=4)
                # reading old data
                data = json.load(data_file)
            # write mode
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # saving daya
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # saving daya
                json.dump(data, data_file, indent=4)
        finally:
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
web_entry = Entry(width=21)
web_entry.focus()
web_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
web_button = Button(text="Search", command=pass_search)
web_button.grid(column=2, row=1, sticky="EW")

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
pass_button = Button(text="Generate Password", command=generate_password)
pass_button.grid(column=2, row=3, sticky="EW")

# Add button
# When combined as "EW", it means the widget will stretch horizontally to fill the entire width of the grid cell
# from the left (West) to the right (East). This is commonly used to make buttons or other widgets expand to fill
# the available horizontal space.
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
