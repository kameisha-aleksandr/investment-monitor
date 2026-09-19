import time

from logger import get_logger


logger = get_logger(__name__)


class Scheduler:

    def __init__(self, task, interval):
        self.task = task
        self.interval = interval

    def start(self):
        logger.info(
            f"Scheduler started. Interval: {self.interval} seconds"
        )

        while True:
            try:
                self.task()

            except Exception:
                logger.exception("Task execution failed")

            logger.info(
                f"Waiting {self.interval} seconds until next run"
            )

            time.sleep(self.interval)