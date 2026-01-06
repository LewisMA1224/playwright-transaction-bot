import os
import logging
import argparse
from datetime import datetime


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Playwright transaction bot (SauceDemo demo automation)."
    )

    parser.add_argument(
        "--headless",
        choices=["true", "false"],
        help="Override headless mode (true/false). Default comes from env (HEADLESS).",
    )

    parser.add_argument(
        "--slow",
        type=int,
        help="Override Playwright slow motion delay in ms. Default comes from env (SLOW_MO_MS).",
    )

    parser.add_argument(
        "--env",
        choices=["default", "demo", "local"],
        help="Environment tag: chooses which .env file to load.",
    )

    return parser.parse_args()


def main(args: argparse.Namespace) -> None:
    # Import AFTER APP_ENV is set so config loads the right .env file
    from bot.config import SETTINGS
    from bot.browser import launch_context
    from bot.auth import login
    from bot.scraper import scrape, save_output
    from bot.actions import screenshot

    def setup_logging() -> None:
        os.makedirs(os.path.dirname(SETTINGS.log_path), exist_ok=True)
        logging.basicConfig(
            filename=SETTINGS.log_path,
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s",
        )

    setup_logging()

    # Resolve overrides from CLI
    headless_override: bool | None = None
    if args.headless is not None:
        headless_override = args.headless.lower() == "true"

    slow_override: int | None = args.slow

    print("=== Playwright Transaction Bot ===")
    print(f"ENV: {os.getenv('APP_ENV', 'default')}")
    print(f"HEADLESS (env): {SETTINGS.headless} | override: {headless_override}")
    print(f"SLOW_MO_MS (env): {SETTINGS.slow_mo_ms} | override: {slow_override}")
    print("----------------------------------")

    os.makedirs(SETTINGS.screenshot_dir, exist_ok=True)

    context, cleanup = launch_context(
        headless=headless_override,
        slow_mo_ms=slow_override,
    )
    page = context.new_page()

    try:
        logging.info("Run started")
        login(page)
        data = scrape(page)
        save_output(data)

        count = data.get("count", len(data.get("items", [])))
        logging.info(f"Run complete: {count} items scraped")
        print(f"✅ Saved {count} items to {SETTINGS.output_path}")

    except Exception as e:
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        shot_path = os.path.join(SETTINGS.screenshot_dir, f"error_{ts}.png")
        try:
            screenshot(page, shot_path)
        except Exception:
            pass
        logging.exception(f"Run failed: {e}")
        print(f"❌ Run failed. See log at {SETTINGS.log_path} and screenshot at {shot_path}")
        raise

    finally:
        cleanup()


if __name__ == "__main__":
    args = parse_args()

    # Set APP_ENV BEFORE config is imported so it knows which file to load
    if args.env:
        os.environ["APP_ENV"] = args.env
    else:
        os.environ.setdefault("APP_ENV", "default")

    main(args)
