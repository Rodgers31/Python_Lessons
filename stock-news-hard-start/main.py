import datetime

import requests
import os
from dotenv import load_dotenv
import datetime as dt
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
load_dotenv("project_config.env")
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


def news_message(one_yesterday_close, two_yesterday_close, price_def):
    news_parameters = {
        "q": STOCK,
        "apiKey": os.getenv("news_api")

    }

    if one_yesterday_close > two_yesterday_close:
        direct = '🔺'
    else:
        direct = '🔻'

    news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
    news_response.raise_for_status()
    tesla_news = news_response.json()
    for article in tesla_news['articles'][:3]:
        headline = article['title']
        description = article['description']
        account_sid = os.getenv("account_sid")
        auth_token = os.getenv("auth_token")

        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f"TSLA: {direct}{round(price_def)}%\n Headline: {headline}.\n Brief: {description}",
            from_="whatsapp:+14155238886",
            to="whatsapp:+14147797306",
        )

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price.


def formatter(my_year, my_month, my_day):
    return f"{my_year}-{my_month:02d}-{my_day:02d}"


now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
day_of_week = now.weekday()
yesterday = ''
day_yesterday = ''
if day_of_week == 0:
    yesterday = formatter(year, month, day - 3)
    day_yesterday = formatter(year, month, day - 4)
elif day_of_week == 1:
    yesterday = formatter(year, month, day - 1)
    day_yesterday = formatter(year, month, day - 4)
elif day_of_week == 6:
    yesterday = formatter(year, month, day - 2)
    day_yesterday = formatter(year, month, day - 3)
else:
    yesterday = formatter(year, month, day - 1)
    day_yesterday = formatter(year, month, day - 2)


parameters = {
"function": "TIME_SERIES_DAILY",
"symbol": STOCK,
"interval": "5min",
"apikey": os.getenv("alpha_vantage")

}

response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
response.raise_for_status()
stock_data = response.json()

tesla_yesterday = stock_data['Time Series (Daily)'][yesterday]
tesla_two_yesterday = stock_data['Time Series (Daily)'][day_yesterday]

y_close = tesla_yesterday['4. close']

close_percent = (5 * float(y_close) / 100)

yy_close = tesla_two_yesterday['4. close']

difference = float(y_close) - float(yy_close)
if close_percent > difference:
    news_message(y_close, yy_close, difference)
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

