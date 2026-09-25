import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from alert import PriceAlert


def test_below_alert():
    alert = PriceAlert(
        symbol="AAPL",
        condition="below",
        value=250
    )

    assert alert.check(240) is True
    assert alert.check(260) is False


def test_above_alert():
    alert = PriceAlert(
        symbol="MSFT",
        condition="above",
        value=500
    )

    assert alert.check(510) is True
    assert alert.check(490) is False


def test_alert_state_change():
    alert = PriceAlert(
        symbol="AAPL",
        condition="below",
        value=250
    )

    triggered, changed = alert.update(240)

    assert triggered is True
    assert changed is True

    triggered, changed = alert.update(240)

    assert triggered is True
    assert changed is False


def test_alert_cleared():
    alert = PriceAlert(
        symbol="AAPL",
        condition="below",
        value=250
    )

    alert.update(240)

    triggered, changed = alert.update(260)

    assert triggered is False
    assert changed is True