# Investment Monitoring Service

A small monitoring service for tracking financial assets, detecting price threshold alerts, storing price history, and sending notifications via Telegram.

The project was built as a portfolio project to demonstrate Python development, automation, Docker, REST API, monitoring, testing, and CI/CD practices.

## Features

* Fetches current asset prices from Finnhub API
* Monitors multiple financial assets
* Supports `above` and `below` price conditions
* Detects alert state changes
* Sends Telegram notifications when an alert starts or is cleared
* Stores price history in SQLite
* Stores alert history in SQLite
* Provides REST API with FastAPI
* Exposes Prometheus metrics
* Provides monitoring dashboards with Grafana
* Runs services using Docker Compose
* Includes automated tests with pytest
* Runs CI through GitHub Actions
* Builds and publishes Docker images to GitHub Container Registry

## Technologies

* Python 3.14
* FastAPI
* SQLite
* Finnhub API
* Telegram Bot API
* Docker
* Docker Compose
* Prometheus
* Grafana
* pytest
* GitHub Actions
* GitHub Container Registry

## Configuration

Create a `.env` file in the project root:

```env
FINNHUB_API_KEY=your_api_key_here
TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
```

An example configuration is provided in:

```text
.env.example
```

The `.env` file is excluded from Git using `.gitignore`.

## Running Locally

### Start the application

Build and start the containers:

```bash
docker compose up --build -d
```

Check running containers:

```bash
docker compose ps
```

View monitor logs:

```bash
docker compose logs -f monitor
```

View API logs:

```bash
docker compose logs -f api
```

### Stop the application

```bash
docker compose down
```

SQLite data is stored in a Docker volume and persists between container restarts.

## REST API

The FastAPI service runs on:

```text
http://localhost:8000
```

### Health check

```http
GET /health
```

Example response:

```json
{
  "status": "ok"
}
```

### Price history

```http
GET /prices/{symbol}
```

Example:

```text
GET /prices/AAPL
```

Optional parameter:

```text
/prices/AAPL?limit=20
```

### Alert history

```http
GET /alerts/{symbol}
```

Example:

```text
GET /alerts/AAPL
```

Optional parameter:

```text
/alerts/AAPL?limit=20
```

### API documentation

FastAPI automatically provides interactive API documentation:

```text
http://localhost:8000/docs
```

## Monitoring

The application exposes Prometheus metrics.

The monitor exposes its metrics on port `8001`.

The API exposes metrics through:

```text
/metrics
```

Examples of custom metrics:

```text
asset_checks_total
alerts_started_total
alerts_cleared_total
market_api_errors_total
telegram_notifications_total
```

The project uses Prometheus to collect these metrics and Grafana to visualize them.

### Prometheus

Prometheus runs on:

```text
http://localhost:9090
```

### Grafana

Grafana runs on:

```text
http://localhost:3000
```

Prometheus is configured as a Grafana data source.

Example dashboard metrics:

* Asset checks rate
* Market API errors
* Started alerts
* Cleared alerts
* Telegram notifications

## Alerts

The monitoring service supports two conditions:

```text
above
below
```

Example configuration:

```python
ASSETS = [
    {
        "symbol": "AAPL",
        "condition": "below",
        "value": 250
    },
    {
        "symbol": "MSFT",
        "condition": "above",
        "value": 500
    }
]
```

The service tracks the alert state to avoid sending repeated notifications.

For example:

```text
OK → ALERT
```

sends an alert notification.

Repeated checks while the condition remains true:

```text
ALERT → ALERT
```

do not send another notification.

When the condition is no longer true:

```text
ALERT → OK
```

a notification about the cleared alert is sent.

## Testing

Tests are written using pytest.

Run locally:

```bash
pytest
```

Or run inside Docker:

```bash
docker compose run --rm monitor pytest
```

Current tests cover:

* `below` price condition
* `above` price condition
* alert state changes
* alert clearing

## CI/CD

GitHub Actions automatically runs when changes are pushed to the repository or a pull request is created.

The CI pipeline:

```text
Git push
    │
    ▼
GitHub Actions
    │
    ├── Checkout repository
    │
    ├── Install Python
    │
    ├── Install dependencies
    │
    ├── Run pytest
    │
    └── Build Docker image
```

For pushes to the `main` branch, the Docker image is also published to GitHub Container Registry:

```text
Git push
    │
    ▼
Tests
    │
    ▼
Docker build
    │
    ▼
GitHub Container Registry
```

The image can then be used by a production Docker Compose configuration without rebuilding it from source.

## What This Project Demonstrates

This project demonstrates practical experience with:

* Python application development
* REST API development
* External API integration
* Automation and scheduling
* Event/alert state management
* Telegram notifications
* SQLite and SQL
* Docker and Docker Compose
* Environment variables and secret management
* Prometheus metrics
* Grafana dashboards
* Automated testing
* Git and GitHub
* GitHub Actions
* Docker image build and publishing
* Basic CI/CD concepts

## Future Improvements

Possible future improvements:

* PostgreSQL instead of SQLite
* Authentication for the API
* More advanced alert rules
* More detailed Grafana dashboards
* Automated deployment to a Linux VPS
* HTTPS with Nginx
* Backup strategy
* More comprehensive test coverage
* Docker image versioning
* Separate development and production environments

## Disclaimer

This project is intended for educational and portfolio purposes.
