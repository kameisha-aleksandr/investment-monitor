from market import MarketClient
from alert import PriceAlert
from logger import get_logger


logger = get_logger(__name__)


class MonitoringService:

    def __init__(self, assets):
        self.assets = assets
        self.market_client = MarketClient()
        self.alerts = {}

        self._create_alerts()

    def _create_alerts(self):
        for asset in self.assets:
            symbol = asset["symbol"]

            self.alerts[symbol] = PriceAlert(
                symbol=symbol,
                condition=asset["condition"],
                value=asset["value"]
            )

    def check_assets(self):
        for asset in self.assets:
            symbol = asset["symbol"]

            logger.info(
                f"Checking {symbol}: "
                f"{asset['condition']} {asset['value']}"
            )

            price = self.market_client.get_price(symbol)

            alert = self.alerts[symbol]

            is_triggered, state_changed = alert.update(price)

            if state_changed:
                if is_triggered:
                    logger.warning(
                        f"ALERT STARTED: {symbol} "
                        f"price is ${price}"
                    )
                else:
                    logger.info(
                        f"ALERT CLEARED: {symbol} "
                        f"price is ${price}"
                    )

            else:
                logger.info(
                    f"No state change for {symbol}"
                )