import time

from market import MarketClient
from alert import PriceAlert
from config import ASSETS


client = MarketClient()


for asset in ASSETS:
    symbol = asset["symbol"]
    condition = asset["condition"]
    value = asset["value"]

    price = client.get_price(symbol)

    alert = PriceAlert(symbol, condition, value)

    if alert.check(price):
        print(
            f"⚠ ALERT: {symbol} price is ${price} "
            f"({condition} {value})"
        )
    else:
        print(
            f"OK: {symbol} price is ${price} "
            f"({condition} {value})"
        )

    print()
    time.sleep(1.5)
