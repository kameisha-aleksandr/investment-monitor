from config import ASSETS, MONITORING_INTERVAL
from monitoring import MonitoringService
from scheduler import Scheduler


service = MonitoringService(ASSETS)

scheduler = Scheduler(
    task=service.check_assets,
    interval=MONITORING_INTERVAL
)

scheduler.start()