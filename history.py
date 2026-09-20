from database import Database


database = Database()


def show_prices(symbol):
    prices = database.get_prices(symbol)

    print(f"\nPrice history: {symbol}")

    for symbol, price, created_at in prices:
        print(
            f"{created_at} | "
            f"{symbol} | "
            f"${price}"
        )


def show_alerts(symbol):
    alerts = database.get_alerts(symbol)

    print(f"\nAlert history: {symbol}")

    for (
        symbol,
        price,
        condition,
        threshold,
        event,
        created_at
    ) in alerts:
        print(
            f"{created_at} | "
            f"{symbol} | "
            f"${price} | "
            f"{condition} ${threshold} | "
            f"{event}"
        )

if __name__ == "__main__":
    show_prices("AAPL")
    show_alerts("AAPL")