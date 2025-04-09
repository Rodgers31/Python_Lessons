import datetime

import requests
import os
from dotenv import load_dotenv
import datetime as dt

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
load_dotenv("project_config.env")
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price.

# def formatter(my_year, my_month, my_day):
#     return f"{my_year}-{my_month:02d}-{my_day:02d}"
#
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day = now.day
# day_of_week = now.weekday()
# yesterday = ''
# day_yesterday = ''
# if day_of_week == 0:
#     yesterday = formatter(year, month, day - 3)
#     day_yesterday = formatter(year, month, day - 4)
# elif day_of_week == 1:
#     yesterday = formatter(year, month, day - 1)
#     day_yesterday = formatter(year, month, day - 4)
# elif day_of_week == 6:
#     yesterday = formatter(year, month, day - 2)
#     day_yesterday = formatter(year, month, day - 3)
# else:
#     yesterday = formatter(year, month, day - 1)
#     day_yesterday = formatter(year, month, day - 2)
#
#
# parameters = {
# "function": "TIME_SERIES_DAILY",
# "symbol": STOCK,
# "interval": "5min",
# "apikey": os.getenv("alpha_vantage")
#
# }
#
# response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
# response.raise_for_status()
# stock_data = response.json()
# print(stock_data)
# tesla_yesterday = stock_data['Time Series (Daily)'][yesterday]
# tesla_two_yesterday = stock_data['Time Series (Daily)'][day_yesterday]
#
# y_close = tesla_yesterday['4. close']
#
# close_percent = (5 * float(y_close) / 100)
#
# yy_close = tesla_two_yesterday['4. close']
#
# difference = float(y_close) - float(yy_close)
#
# if difference > close_percent:
#     print("Get news")
# print(close_percent)
## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



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

