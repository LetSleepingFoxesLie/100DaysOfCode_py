import smtplib
import datetime as dt
import pandas as pd
from random import choice
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

def read_data():
    try:
        with open(r"32_AutomatedBirthdayWisher\ActualProject\birthdays.lsfl", "r") as f:
            data = pd.read_csv(f).to_dict(orient = "records")
            for entry in data:
                name = entry["name"]
                email = entry["email"]
                
                print(f"{name} + {email}")
    except FileNotFoundError:
        print("Fuck!")
        
read_data()