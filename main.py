from prometheus_client import start_http_server

from config import ASSETS, MONITORING_INTERVAL
from monitoring import MonitoringService
from scheduler import Scheduler


start_http_server(8001)

service = MonitoringService(ASSETS)

scheduler = Scheduler(
    task=service.check_assets,
    interval=MONITORING_INTERVAL
)

scheduler.start()