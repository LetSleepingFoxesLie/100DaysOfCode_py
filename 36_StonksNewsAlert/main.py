STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
THRESHOLD = 0.2 # Should be 5, but I'm just testing it out

from api_reader import API_Reader
from email_account import Email_Account

import requests as rq
import smtplib
from datetime import datetime, timedelta

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

def main():
    data = get_stock_price()
    percentage = analyse_last_two_days(data)
    
    if abs(percentage) >= THRESHOLD:
        print("Difference is over the selected threshold!")
        article_list = get_news()
        receiver = Email_Account(r"36_StonksNewsAlert\e_receiver.lsfl")
        send_email(receiver, article_list, percentage)
    else:
        print("Difference is below the selected threshold! Exiting program...")

# Literally gets the prices of relevant stocks
def get_stock_price() -> dict:
    endpoint = "https://www.alphavantage.co/query"
    
    reader = API_Reader("alpha_vantage.lsfl")
    # print(reader.key)
    
    parameters = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": STOCK,
        "apikey": reader.key
    }
    
    response = rq.get(url = endpoint, params = parameters)
    print("Fetching stonk prices...")
    return response.json()

def analyse_last_two_days(data: dict):
    
    # Fetch strings that will be used as keys
    dt_closest_day = get_last_refreshed(data)
    str_closest_day = dt_closest_day.strftime("%Y-%m-%d")
    while True:
        try:
            str_day_before = get_yesterday(dt_closest_day)
            close_before_yesterday = float(data["Time Series (Daily)"][str_day_before]["4. close"])
            break
        except KeyError:
            continue
        
    # Fetch the information within said keys -- specifically their closing values
    close_yesterday = float(data["Time Series (Daily)"][str_closest_day]["4. close"])
    
    
    print("Analysing differences from the last two days...")
    
    # Now analyse and see whether there was a big enough difference (in %)
    return get_percentage_change(
        starting = close_before_yesterday,
        final = close_yesterday
        )

# Parsing and working with different datetime structures and Python strings
# This is the part that took me over an hour, everything else was somewhat a breeze
def get_last_refreshed(data: dict) -> datetime:
    day_string = data["Meta Data"]["3. Last Refreshed"]
    return datetime.strptime(day_string, "%Y-%m-%d")

def get_yesterday(day: datetime) -> str:
    yesterday = day - timedelta(days = 1)
    return yesterday.strftime("%Y-%m-%d")

# y stands for "yesterday", by stands for "before yesterday"
def get_percentage_change(starting: float, final: float) -> float:
    return 100 * ((final - starting) / starting)

# -----------------------------------------------
# Step 2: getting the news

# 2-step function: let's get the news and already clean them up for convenience and conciseness
def get_news() -> list:
    endpoint = "https://newsapi.org/v2/everything"
    
    a = API_Reader("newsapi.lsfl")
    
    parameters = {
        "language": "en",
        "apiKey": a.key,
        "q": COMPANY_NAME,
        "sortBy": "publishedAt" # Default value, but putting it in here anyway
    }
    
    response = rq.get(url = endpoint, params = parameters)
    response.raise_for_status()
    response = response.json()
    
    print("Fetching latest news...")
    
    # Actually fetching the latest three articles:
    article_list = list()
    for article in response["articles"][:3]:
        article_list.append(article)

    return article_list

# -----------------------------------------------
# Step 3: sending the email

def send_email(receiver: str, article_list: list, percentage_change: float) -> None:
    GMAIL_SMTP = "smtp.gmail.com"
    sender = Email_Account(r"36_StonksNewsAlert\e_sender.lsfl")
    
    # Generate message string
    message_string: str
    
    if percentage_change >= THRESHOLD:
        message_string = f"Subject:[StonksNewsAlert] {STOCK} is stonking by {percentage_change:.2f}%! 📈🚀\n\n"
    else:
        message_string = f"Subject:[StonksNewsAlert] {STOCK} is stinking by {percentage_change:.2f}%! 📉\n\n"
    
    message_string += f"Stay up to date with the LATEST news for {STOCK}!\n\n"
    
    for article in article_list:
        message_string += f"Title: \"{article['title']}\"\n"
        message_string += f"Description: \"{article['description']}\"\n"
        message_string += f"Read more: \"{article['url']}\"\n\n"

    print("Sending email...")
    
    # Actually sending the email
    with smtplib.SMTP(GMAIL_SMTP, port = 587) as connection:
        connection.starttls()
        
        connection.login(
            user = sender.username,
            password = sender.password
        )
        
        connection.sendmail(
            from_addr = sender.username,
            to_addrs = receiver.username,
            msg = message_string.encode("utf-8")
        )
    
    print("Email sent!")

if __name__ == "__main__":
    main()