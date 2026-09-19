import time

from market import MarketClient
from alert import PriceAlert
from config import ASSETS
from logger import get_logger


logger = get_logger(__name__)


client = MarketClient()


for asset in ASSETS:
    symbol = asset["symbol"]
    condition = asset["condition"]
    value = asset["value"]

    logger.info(
        f"Checking {symbol}: {condition} {value}"
    )

    price = client.get_price(symbol)

    alert = PriceAlert(symbol, condition, value)

    if alert.check(price):
        logger.warning(
            f"ALERT: {symbol} price is ${price} "
            f"({condition} {value})"
        )
    else:
        logger.info(
            f"OK: {symbol} price is ${price} "
            f"({condition} {value})"
        )
    time.sleep(1.5)
