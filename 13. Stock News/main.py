import requests
from twilio.rest import Client
import os

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newapi.org/v2/everything"
STOCK_API_KEY = "FLONEDE27PWYROO7"
NEWS_API_KEY = "56e17194b7704a0f86983bc0682dde4b"
my_phone = "+11111111"

stock_param = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

# Get yesterday's closing stock price
stock_res = requests.get(url=STOCK_ENDPOINT, params=stock_param)
data = stock_res.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

# Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

# Calculate the difference
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "📈"
else:
    up_down = "📉"

diff_percent = round((difference / float(yesterday_closing_price)) * 100)

if diff_percent < 1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_res = requests.get(url=NEWS_ENDPOINT, params=news_params)
    articles = news_res.json()["articles"]
    three_articles = articles[:3]
    
    # Create a new list of the first 3 articles's headline and description
    formatted_articles = [f"{COMPANY_NAME}: {up_down}{diff_percent}\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    # Send each article as a separate message via Twilio
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    for article in formatted_articles:
        message = client.messages \
                        .create(
                            body=article,
                            from_='+15017122661',
                            to=my_phone
                        )

