# Stock-notification through Whatsapp

The Stock Notification project is a Python application that monitors stock price changes and sends notifications via WhatsApp using the Twilio API. It fetches stock data from the Alpha Vantage API and news articles from the News API to provide context for significant stock price changes.

## Features

- Fetch daily stock prices for a specified company.
- Calculate the percentage change in stock price.
- Retrieve news articles related to the company.
- Send WhatsApp notifications for significant stock price changes.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/chinguun101/stock-notification.git
   cd stock-notification
   ```

2. **Install the required packages:**

   Make sure you have Python installed, then run:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**

   Create a `.env` file in the root directory and add the following environment variables:

   ```plaintext
   API_KEY=your_alpha_vantage_api_key
   NEWS_API=your_news_api_key
   TWILIO_SID=your_twilio_sid
   TWILIO_AUTH_TOKEN=your_twilio_auth_token
   ```

## Usage

1. **Run the main script:**

   Execute the main script to start monitoring stock prices:

   ```bash
   python stock_notification/main.py
   ```

2. **Check the console output:**

   The script will print the stock price change and any notifications sent.

## Project Structure

- `stock_notification/main.py`: The main script that fetches stock data, calculates price changes, retrieves news, and sends notifications.
- `requirements.txt`: Lists the Python packages required for the project.

## Acknowledgments

- [Alpha Vantage API](https://www.alphavantage.co/) for stock data.
- [News API](https://newsapi.org/) for news articles.
- [Twilio](https://www.twilio.com/) for WhatsApp notifications.
