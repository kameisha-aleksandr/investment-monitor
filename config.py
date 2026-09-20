import os

from dotenv import load_dotenv

load_dotenv()

FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY")

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

MONITORING_INTERVAL = 20

ASSETS = [
    {
        "symbol": "AAPL",
        "condition": "below",
        "value": 350
    },
    {
        "symbol": "MSFT",
        "condition": "above",
        "value": 500
    },
    # {
    #     "symbol": "NVDA",
    #     "condition": "below",
    #     "value": 150
    # }
]