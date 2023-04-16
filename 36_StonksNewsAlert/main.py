STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

from api_reader import API_Reader
import requests as rq
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
    # print(get_stock_price())
    data = get_stock_price()
    analyse_last_two_days(data)
    pass

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
    return response.json()

def analyse_last_two_days(data: dict):
    
    # Fetch strings that will be used as keys
    dt_closest_day = get_last_refreshed(data)
    str_closest_day = dt_closest_day.strftime("%Y-%m-%d")
    str_day_before = get_yesterday(dt_closest_day)
    
    # Fetch the information within said keys -- specifically their closing values
    close_yesterday = float(data["Time Series (Daily)"][str_closest_day]["4. close"])
    close_before_yesterday = float(data["Time Series (Daily)"][str_day_before]["4. close"])
    
    # Now analyse and see whether there was a big enough difference (in %)
    THRESHOLD = 5.0 # In float
    
    # print(close_yesterday)
    # print(close_before_yesterday)
    
    print(get_percentage_change(
        starting = close_before_yesterday,
        final = close_yesterday
        ))
    print("Get news!")
    pass

def get_last_refreshed(data: dict) -> datetime:
    day_string = data["Meta Data"]["3. Last Refreshed"]
    return datetime.strptime(day_string, "%Y-%m-%d")

def get_yesterday(day: datetime) -> str:
    yesterday = day - timedelta(days = 1)
    return yesterday.strftime("%Y-%m-%d")

# y stands for "yesterday", by stands for "before yesterday"
def get_percentage_change(starting: float, final: float) -> float:
    return 100 * ((final - starting) / starting)

if __name__ == "__main__":
    main()