import smtplib
import datetime as dt
import pandas as pd
from random import choice, randint
from LSFL_account import LSFL_Account

# Setting up everything
LETTERS_PATH = r"32_AutomatedBirthdayWisher\ActualProject\letter_templates"
GMAIL_SMTP = "smtp.gmail.com"

# Sender account! I should probably
sender_account = LSFL_Account(r"32_AutomatedBirthdayWisher\ActualProject\data.lsfl")

##################### Extra Hard Starting Project ######################
# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.

# CSV reader, except the .csv is actually a .lsfl

def read_data() -> dict:
    try:
        with open(r"32_AutomatedBirthdayWisher\ActualProject\birthdays.lsfl", "r") as f:
            data = pd.read_csv(f).to_dict(orient = "records")
            print(data)
            return data
    except FileNotFoundError:
        print("Fuck!")

def replace_name(lines: list, name: str) -> str:
    s = str()
    for line in lines:
        if "[NAME]" in line:
            s += line.replace("[NAME]", name)
        else:
            s += line
    return s

def check_birthdays(data: dict) -> list:
    birthdays = list()
    today = dt.datetime.now()
    try:
        for person in data:
            if today.day == person["day"] and today.month == person["month"]:
                birthday_message = f"32_AutomatedBirthdayWisher\ActualProject\letter_templates\letter_{randint(1, 3)}.txt"
                s = list()
                with open(birthday_message, "r", encoding = "utf-8") as f:
                    s = f.readlines()
                formatted_message = replace_name(s, person["name"])
                send_email(sender_account, person["email"], formatted_message)
    except KeyError:
        print("No birthdays!")
    
    return birthdays
        

def send_email(sender: LSFL_Account, receiver: str, message: str):
    with smtplib.SMTP(GMAIL_SMTP, port = 587) as connection:
        print("Sending email...")
        connection.starttls()
        connection.login(
            user = sender.username,
            password = sender.password
        )
        connection.sendmail(
            from_addr = sender.username,
            to_addrs = receiver,
            msg = ("Subject:Happy birthday!\n\n" + message).encode("utf-8")
        )

check_birthdays(read_data())