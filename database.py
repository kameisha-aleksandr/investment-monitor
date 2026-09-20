import sqlite3

from logger import get_logger


logger = get_logger(__name__)


class Database:

    def __init__(self, database_name="monitoring.db"):
        self.database_name = database_name
        self._create_tables()

    def _connect(self):
        return sqlite3.connect(self.database_name)

    def _create_tables(self):
        with self._connect() as connection:
            cursor = connection.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS prices (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    symbol TEXT NOT NULL,
                    price REAL NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS alerts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    symbol TEXT NOT NULL,
                    price REAL NOT NULL,
                    condition TEXT NOT NULL,
                    threshold REAL NOT NULL,
                    event TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)

            connection.commit()

        logger.info("Database initialized")

    def save_price(self, symbol, price):
        with self._connect() as connection:
            connection.execute(
                """
                INSERT INTO prices (symbol, price)
                VALUES (?, ?)
                """,
                (symbol, price)
            )

            connection.commit()

    def save_alert(
        self,
        symbol,
        price,
        condition,
        threshold,
        event
    ):
        with self._connect() as connection:
            connection.execute(
                """
                INSERT INTO alerts (
                    symbol,
                    price,
                    condition,
                    threshold,
                    event
                )
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    symbol,
                    price,
                    condition,
                    threshold,
                    event
                )
            )

            connection.commit()

    def get_prices(self, symbol, limit=10):
        with self._connect() as connection:
            cursor = connection.execute(
                """
                SELECT symbol, price, created_at
                FROM prices
                WHERE symbol = ?
                ORDER BY created_at DESC
                LIMIT ?
                """,
                (symbol, limit)
            )

            return cursor.fetchall()

    def get_alerts(self, symbol, limit=10):
        with self._connect() as connection:
            cursor = connection.execute(
                """
                SELECT symbol, price, condition,
                       threshold, event, created_at
                FROM alerts
                WHERE symbol = ?
                ORDER BY created_at DESC
                LIMIT ?
                """,
                (symbol, limit)
            )

            return cursor.fetchall()