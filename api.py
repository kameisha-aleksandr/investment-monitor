from fastapi import FastAPI

from database import Database


app = FastAPI(
    title="Investment Monitoring Service",
    description="API for monitoring financial assets",
    version="1.0.0"
)

database = Database()


@app.get("/health")
def health_check():
    return {
        "status": "ok"
    }


@app.get("/prices/{symbol}")
def get_prices(symbol: str, limit: int = 10):
    prices = database.get_prices(
        symbol=symbol.upper(),
        limit=limit
    )

    return {
        "symbol": symbol.upper(),
        "prices": [
            {
                "symbol": row[0],
                "price": row[1],
                "created_at": row[2]
            }
            for row in prices
        ]
    }


@app.get("/alerts/{symbol}")
def get_alerts(symbol: str, limit: int = 10):
    alerts = database.get_alerts(
        symbol=symbol.upper(),
        limit=limit
    )

    return {
        "symbol": symbol.upper(),
        "alerts": [
            {
                "symbol": row[0],
                "price": row[1],
                "condition": row[2],
                "threshold": row[3],
                "event": row[4],
                "created_at": row[5]
            }
            for row in alerts
        ]
    }