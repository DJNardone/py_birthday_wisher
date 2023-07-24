import pandas
import datetime as dt
import smtplib
import random

PLACEHOLDER = "[NAME]"
MY_EMAIL = "djdoesit44@gmail.com"
PASSWORD = ""

now = dt.datetime.now()
today = (now.month, now.day)
# print(today)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(row.month, row.day): row for (index, row) in data.iterrows()}
if today in birthday_dict:
    rand_letter = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(rand_letter) as letter_file:
        ltr = letter_file.read()
        birthday_name = birthday_dict[today]["name"]
        new_ltr = ltr.replace(PLACEHOLDER, birthday_name)
        with open(f"letter_to_{birthday_name}.txt", mode="w") as finished_ltr:
            finished_ltr.write(new_ltr)
        with open(f"letter_to_{birthday_name}.txt") as ltr_to_send:
            letter = ltr_to_send.read()
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()  # secures connection
                connection.login(user=MY_EMAIL, password=PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs="",
                    msg=f"Subject:HAPPY BIRTHDAY!\n\n{letter}"
            )




