import requests

from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
from logger import get_logger


logger = get_logger(__name__)


class NotificationService:

    def __init__(self):
        self.url = (
            f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        )

    def _send_message(self, text):
        data = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": text
        }

        try:
            response = requests.post(
                self.url,
                data=data,
                timeout=10
            )

            response.raise_for_status()

            logger.info("Telegram notification sent")

        except requests.RequestException as error:
            logger.error(
                f"Failed to send Telegram notification: {error}"
            )

    def send_alert(self, symbol, price, condition, value):
        message = (
            f"🚨 PRICE ALERT\n\n"
            f"{symbol}\n"
            f"Price: ${price}\n"
            f"Condition: {condition} ${value}"
        )

        self._send_message(message)

    def send_alert_cleared(self, symbol, price):
        message = (
            f"✅ ALERT CLEARED\n\n"
            f"{symbol}\n"
            f"Price: ${price}"
        )

        self._send_message(message)