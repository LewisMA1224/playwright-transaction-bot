import json
from datetime import datetime
from playwright.sync_api import Page
from .actions import wait_for_ready
from .config import SETTINGS

def ensure_inventory(page: Page) -> None:
    # If already on inventory, don't force a fresh goto
    if "inventory.html" in page.url:
        return

    page.goto(SETTINGS.base_url)
    wait_for_ready(page)

    # If SauceDemo redirects you back to login, you are not authenticated
    if page.url.rstrip("/") == "https://www.saucedemo.com" or "saucedemo.com/" == page.url:
        raise RuntimeError("Redirected to login. Not authenticated when trying to access inventory.")

    page.wait_for_selector(".inventory_list", state="visible")

def scrape(page: Page) -> dict:
    ensure_inventory(page)

    items = page.locator(".inventory_item")
    results = []

    count = items.count()
    for i in range(count):
        item = items.nth(i)
        name = item.locator(".inventory_item_name").inner_text().strip()
        price = item.locator(".inventory_item_price").inner_text().strip()
        desc = item.locator(".inventory_item_desc").inner_text().strip()

        results.append({
            "name": name,
            "price": price,
            "description": desc,
        })

    payload = {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "source": "saucedemo",
        "count": len(results),
        "items": results,
    }
    return payload

from pathlib import Path
import json

def save_output(data):
    output_path = Path(SETTINGS.output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

