from prometheus_client import Counter


ASSET_CHECKS = Counter(
    "asset_checks_total",
    "Total number of asset checks"
)

ALERTS_STARTED = Counter(
    "alerts_started_total",
    "Total number of alerts started"
)

ALERTS_CLEARED = Counter(
    "alerts_cleared_total",
    "Total number of alerts cleared"
)

MARKET_API_ERRORS = Counter(
    "market_api_errors_total",
    "Total number of market API errors"
)

TELEGRAM_NOTIFICATIONS = Counter(
    "telegram_notifications_total",
    "Total number of Telegram notifications sent"
)