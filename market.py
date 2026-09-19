import requests

from config import API_KEY


class MarketClient:

    def get_price(self, symbol):
        url = "https://www.alphavantage.co/query"

        params = {
            "function": "GLOBAL_QUOTE",
            "symbol": symbol,
            "apikey": API_KEY
        }

        response = requests.get(url, params=params)

        response.raise_for_status()

        data = response.json()
        # print(data)

        return float(data["Global Quote"]["05. price"])