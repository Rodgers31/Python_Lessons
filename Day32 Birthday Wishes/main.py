import smtplib

my_email = "rodgerdoger003@gmail.com"
password = "xxxxxxx"
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)