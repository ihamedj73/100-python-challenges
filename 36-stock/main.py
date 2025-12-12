from email import message
from email.mime.text import MIMEText

import smtplib

import requests
from datetime import datetime, timedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "YOURKEYHERE"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "YOURKEYHERE"


EMAIL = "YOUREMAILHERE"
PASSWORD = "YOURPASSWORDHERE"


now = datetime.now()
yesterday = now - timedelta(days=1)
yesterday = datetime.strftime(yesterday, "%Y-%m-%d")
day_before_yesterday = now - timedelta(days=2)  # days must be 2
day_before_yesterday = datetime.strftime(day_before_yesterday, "%Y-%m-%d")


def get_prices():
    price_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": STOCK_API_KEY,
    }
    res = requests.get(
        url=STOCK_ENDPOINT, params=price_params)
    res.raise_for_status()

    return res.json()


def get_price_change_percentage():
    data = get_prices()
    prices = data['Time Series (Daily)']
    yesterday_prices = prices[yesterday]
    day_before_yesterday_prices = prices[day_before_yesterday]

    yesterday_close_price = float(yesterday_prices["4. close"])
    day_before_yesterday_close_price = float(
        day_before_yesterday_prices["4. close"])

    return ((yesterday_close_price - day_before_yesterday_close_price) /
            day_before_yesterday_close_price) * 100


def get_recent_news():
    news_params = {
        "q": COMPANY_NAME,
        "from": day_before_yesterday,
        "sortBy": "popularity",
        "apiKey": NEWS_API_KEY
    }
    res = requests.get(
        url=NEWS_ENDPOINT, params=news_params)
    data = res.json()
    articles = data['articles']

    recent_news = [{"headline": article['title'],
                    "brief": article['description']} for article in articles[:3]]
    return recent_news


# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
price_change_pr = get_price_change_percentage()
if abs(price_change_pr) >= 5:
    recent_news = get_recent_news()
    message = ''
    for news in recent_news:
        message += f"Headline: {news['headline']:}\nBrief: {news['brief']}\n\n"
    format_subject = f"🔺 {price_change_pr}" if price_change_pr > 0 else f"🔻 {price_change_pr}"

    print("*********************** SENDING EMAIL ***********************")
    # Create MIMEText object for UTF-8 encoding
    mime_message = MIMEText(message, "plain", "utf-8")
    mime_message["From"] = EMAIL
    mime_message["To"] = EMAIL
    mime_message["Subject"] = format_subject

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=mime_message.as_string()
        )
    print("*********************** EMAIL SENDED ***********************")


# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.


# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
