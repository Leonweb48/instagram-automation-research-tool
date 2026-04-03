import json
from pathlib import Path
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

class Account(BaseModel):
    username: str
    password: str | None = None

class Config(BaseModel):
    accounts: list[Account] = []
    max_actions_per_hour: int = 60
    max_actions_per_day: int = 300
    proxy: str | None = None  # e.g. http://user:pass@ip:port
    dry_run: bool = False
    headless: bool = False
    log_file: str = "actions.log"

    @classmethod
    def load(cls) -> "Config":
        config_path = Path("config.json")
        if config_path.exists():
            with open(config_path) as f:
                data = json.load(f)
            return cls.model_validate(data)
        
        username = os.getenv("INSTAGRAM_USERNAME")
        password = os.getenv("INSTAGRAM_PASSWORD")
        if username:
            return cls(accounts=[Account(username=username, password=password)])
        return cls()

config = Config.load()
