import requests

from config import FINNHUB_API_KEY
from logger import get_logger


logger = get_logger(__name__)


class MarketClient:

    def get_price(self, symbol):
        logger.info(f"Getting price for {symbol}")

        url = "https://finnhub.io/api/v1/quote"

        params = {
            "symbol": symbol,
            "token": FINNHUB_API_KEY
        }

        try:
            response = requests.get(url, params=params)

            response.raise_for_status()

            data = response.json()

            price = float(data["c"])

            logger.info(f"{symbol} price: ${price}")

            return price

        except requests.RequestException as error:
            logger.error(
                f"Failed to get price for {symbol}: {error}"
            )
            raise