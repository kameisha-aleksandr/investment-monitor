import os

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")

ASSETS = [
    {
        "symbol": "AAPL",
        "condition": "below",
        "value": 250
    },
    {
        "symbol": "MSFT",
        "condition": "above",
        "value": 500
    },
    {
        "symbol": "NVDA",
        "condition": "below",
        "value": 150
    }
]