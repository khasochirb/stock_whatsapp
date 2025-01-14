import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

# Constants for the stock and company name
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# Load environment variables from the .env file
load_dotenv(".env")

# Parameters for the Alpha Vantage API request
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": os.environ['API_KEY'],
    "output_size": "compact",
}

# Fetch stock data from Alpha Vantage API
response = requests.get("https://www.alphavantage.co/query", params=parameters)
response.raise_for_status()

# Parse the JSON response to get daily stock data
data = response.json()['Time Series (Daily)']

# Get the closing price for yesterday
yesterday_date = list(data.keys())[1]
yesterday_entry = data[yesterday_date]
yesterday_price = float(yesterday_entry['4. close'])
print(yesterday_price)

# Get the closing price for the day before yesterday
day_before_yesterday_date = list(data.keys())[2]
day_before_yesterday_entry = data[day_before_yesterday_date]
day_before_yesterday_price = float(day_before_yesterday_entry['4. close'])
print(type(day_before_yesterday_price))

# Calculate the percentage change in stock price
change = round((yesterday_price - day_before_yesterday_price) / day_before_yesterday_price * 100, 2)
print(f"change: {change}")

# Parameters for the News API request
parameters = {
    "qInTitle": COMPANY_NAME,
    "apiKey": os.environ['NEWS_API'],
}

# Fetch news articles related to the company
response = requests.get('https://newsapi.org/v2/everything', params=parameters)
response.raise_for_status()
news_data = response.json()['articles']
print(len(news_data))

# Twilio client setup for sending messages

client = Client(os.environ['SID'], os.environ['AUTH_TOKEN'])

# Send a WhatsApp message if the stock price change is significant
if change > 0.5 or change < -0.5:
    for i in range(3):
        message = client.messages.create(
            body=f"{STOCK} {os.environ['SID']}: {'🔺' if change > 1 else '🔻'}{change} \n Headline: {news_data[i]['title']}\nBrief:{news_data[i]['description']}",
            from_="whatsapp:+14155238886",
            to="whatsapp:+14156700598",
        )
        print(message.status)
