import smtplib
import datetime as dt
from random import choice
from LSFL_account import LSFL_Account

MONDAY = 0
TUESDAY = 1
WEDNESDAY = 2
THURSDAY = 3
FRIDAY = 4
SATURDAY = 5
SUNDAY = 6

MOTIVATIONAL_QUOTES_FILE = r"32_AutomatedBirthdayWisher/quotes.txt"
GMAIL_SMTP = "smtp.gmail.com"

sender_account = LSFL_Account(r"32_AutomatedBirthdayWisher/data.lsfl")
receiver_account = LSFL_Account(r"32_AutomatedBirthdayWisher/receiver.lsfl")

def send_email(sender: LSFL_Account, receiver: LSFL_Account, message: str) -> None:
    with smtplib.SMTP(GMAIL_SMTP, port = 587) as connection:
        connection.starttls()

        connection.login(
            user = sender.username,
            password = sender.password
        )

        connection.sendmail(
            from_addr = sender.username,
            to_addrs = receiver.username,
            msg = message.encode("utf-8")
        )
    
def send_motivational_message(email: str) -> None:
    today_date = dt.datetime.now()
    messages = list()
    try:
        with open(MOTIVATIONAL_QUOTES_FILE, "r") as f:
            messages = f.readlines()
    except FileNotFoundError:
        messages = ["There are no quotes, get fucked."]
    
    if today_date.weekday() == THURSDAY:
        send_email(
            sender = sender_account,
            receiver = receiver_account,
            message = "Subject:Motivational message!\n\n" + choice(messages)
        )
        
send_motivational_message(receiver_account.username)
    
    