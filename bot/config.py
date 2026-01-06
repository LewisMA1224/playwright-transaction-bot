import os
from dataclasses import dataclass

from dotenv import load_dotenv

# Decide which .env file to load based on APP_ENV
# APP_ENV comes from main.py (via CLI), or defaults to "default"
APP_ENV = os.getenv("APP_ENV", "default")

ENV_FILE_MAP = {
    "default": ".env",        # python main.py
    "demo": ".env.demo",      # python main.py --env demo
    "local": ".env.local",    # python main.py --env local (optional)
}

env_file = ENV_FILE_MAP.get(APP_ENV, ".env")

# Load the chosen env file (falls back gracefully if missing)
load_dotenv(env_file)


@dataclass(frozen=True)
class Settings:
    base_url: str = os.getenv("BASE_URL", "https://example.com")
    login_url: str = os.getenv("LOGIN_URL", "https://example.com/login")
    username: str = os.getenv("BOT_USERNAME", "")
    password: str = os.getenv("BOT_PASSWORD", "")

    headless: bool = os.getenv("HEADLESS", "true").lower() == "true"
    slow_mo_ms: int = int(os.getenv("SLOW_MO_MS", "0"))
    timeout_ms: int = int(os.getenv("TIMEOUT_MS", "15000"))

    # persistent profile directory (keeps cookies/session)
    user_data_dir: str = os.getenv("USER_DATA_DIR", "state/user-data")

    # output + debugging
    output_path: str = os.getenv("OUTPUT_PATH", "data/output.json")
    log_path: str = os.getenv("LOG_PATH", "logs/run.log")
    screenshot_dir: str = os.getenv("SCREENSHOT_DIR", "screenshots")


SETTINGS = Settings()


