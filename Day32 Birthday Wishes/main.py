import smtplib

my_email = "rodgerdoger003@gmail.com"
password = "qyovfibexhjqoris"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="rodgersotieno@myyahoo.com",
                        msg="Subject:Hello\n\nThis is the body of my email")

