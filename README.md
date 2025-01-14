# Stock Notification via WhatsApp  

This Stock Notification project is a Python-based application that tracks stock price changes and sends WhatsApp alerts using the Twilio API. It integrates the Alpha Vantage API for stock data and the News API for providing context about significant price movements.  

## Features  

- Monitor daily stock prices for a specified company.  
- Calculate percentage changes in stock prices.  
- Fetch related news articles for additional context.  
- Send WhatsApp notifications for notable stock price fluctuations.  

## Installation  

1. **Clone the repository:**  

   ```bash  
   git clone https://github.com/khasochirb/stock_whatsapp.git  
   cd stock-notification  
   ```  

2. **Install dependencies:**  

   Ensure Python is installed, then run:  

   ```bash  
   pip install -r requirements.txt  
   ```  

3. **Configure environment variables:**  

   Create a `.env` file in the root directory and include the following keys:  

   ```plaintext  
   API_KEY=your_alpha_vantage_api_key  
   NEWS_API=your_news_api_key  
   TWILIO_SID=your_twilio_sid  
   TWILIO_AUTH_TOKEN=your_twilio_auth_token  
   ```  

## Usage  

1. **Start the application:**  

   Run the main script to begin stock price monitoring:  

   ```bash  
   python stock_notification/main.py  
   ```  

2. **View the results:**  

   The console output will display price changes and details of sent notifications.  

## Project Structure  

- `stock_notification/main.py`: Core script for fetching data, calculating changes, retrieving news, and sending alerts.  
- `requirements.txt`: File listing the required Python libraries.  

## Acknowledgments  

- [Alpha Vantage API](https://www.alphavantage.co/) for stock data.  
- [News API](https://newsapi.org/) for fetching relevant articles.  
- [Twilio](https://www.twilio.com/) for enabling WhatsApp notifications.  
