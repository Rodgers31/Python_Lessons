##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas
import datetime as dt
import smtplib
import random

data = pandas.read_csv("birthdays.csv")
now = dt.datetime.now()
day = now.day
month = now.month

MY_EMAIL = "rodgerdoger003@gmail.com"
PASSWORD = "qyovfibexhjqoris"

# iterate through all the birthdays and store the name and email of the person whose birthday is today
is_birthday = {value["name"]: value.email for (key, value) in data.iterrows()
               if value.month == month and value.day == day}

# Open all 3 letters
with open("letter_templates/letter_1.txt") as data_letter:
    letter_1 = data_letter.readlines()

with open("letter_templates/letter_2.txt") as data_letter:
    letter_2 = data_letter.readlines()

with open("letter_templates/letter_3.txt") as data_letter:
    letter_3 = data_letter.readlines()

# select a random letter from the 3 and store it in variable selected_letter
all_letters = (letter_1, letter_2, letter_3)

selected_letter = random.choice(all_letters)

# iterate through all the birthdays, and replace the NAME with the birthday persons name, and send the letter
for name in is_birthday:
    letter = [words.replace('[NAME]', f'{name}') for words in selected_letter]
    # turn array into string that can be sent as email message
    new_letter = "".join(letter)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=is_birthday[name],
                            msg=f"Subject:Happy Birthday!\n\n{new_letter}")
