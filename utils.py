import random
import time
import logging
from datetime import datetime
from rich.console import Console

console = Console()

logging.basicConfig(
    filename="actions.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def log_action(action: str, details: str, account: str):
    msg = f"ACCOUNT:{account} | ACTION:{action} | {details}"
    logging.info(msg)
    console.print(f"[bold green]✓[/] {msg}")

def human_delay(min_sec: float = 8.0, max_sec: float = 35.0):
    """Gaussian random delay mimicking human behavior"""
    delay = random.gauss((min_sec + max_sec) / 2, (max_sec - min_sec) / 4)
    time.sleep(max(min_sec, min(delay, max_sec)))

class RateLimiter:
    def __init__(self, max_per_hour: int, max_per_day: int):
        self.max_per_hour = max_per_hour
        self.max_per_day = max_per_day
        self.actions = []

    def can_perform(self) -> bool:
        now = datetime.now()
        self.actions = [t for t in self.actions if (now - t).total_seconds() < 86400]
        hour_ago = now.replace(minute=0, second=0, microsecond=0)
        if len([t for t in self.actions if t > hour_ago]) >= self.max_per_hour:
            return False
        if len(self.actions) >= self.max_per_day:
            return False
        self.actions.append(now)
        return True
