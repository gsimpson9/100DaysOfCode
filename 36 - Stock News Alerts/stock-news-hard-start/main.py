import datetime
import requests
from datetime import date
from twilio.rest import Client
import constants

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
NUMBER_OF_ARTICLES = 2
yesterdays_date = str(date.today() - datetime.timedelta(days=1))
two_days_ago_date = str(date.today() - datetime.timedelta(days=2))

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = constants.STOCK_API_KEY
NEWS_ENDPOINT = "https://api.newscatcherapi.com/v2/search"
NEWS_API_KEY = constants.NEWS_API_KEY

# Stock API request
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}
response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()

# News API request
news_params = {
    "q": "\"Tesla\"",
    "lang": "en",
}
headers = {
    "x-api-key": NEWS_API_KEY
}
response2 = requests.get(url=NEWS_ENDPOINT, params=news_params, headers=headers)
response2.raise_for_status()

# Program logic
yesterday_close = float(response.json()["Time Series (Daily)"][yesterdays_date]["4. close"])
two_days_ago_close = float(response.json()["Time Series (Daily)"][two_days_ago_date]["4. close"])
prctg_difference = round((yesterday_close - two_days_ago_close) / yesterday_close * 100, 4)
up_down = None
if prctg_difference >0:
    up_down = "⬆️"
else:
    up_down = "⬇️"

if prctg_difference > 5 or prctg_difference < -5:
    top_articles = response2.json()['articles'][:NUMBER_OF_ARTICLES]
    for article in top_articles:
        account_sid = constants.account_sid
        auth_token = constants.auth_token
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
                body=f"TSLA: {prctg_difference}% {up_down}️\n\n{article['title']}\n\n\n{article['summary']}",
                from_='+17196243584',
                to='+447889193212'
            )
