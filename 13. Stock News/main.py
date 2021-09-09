import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newapi.org/v2/everything"
STOCK_API_KEY = "FLONEDE27PWYROO7"

stock_param = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

stock_data = requests.get(url=STOCK_ENDPOINT, params=stock_param).json()
yesterday = stock_data["Meta Data"]["3. Last Refreshed"]
last_close_price = stock_data["Time Series (Daily)"][yesterday]["4. close"]
print(last_close_price)