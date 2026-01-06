import random
import time
from playwright.sync_api import Page, Locator

def jitter(min_ms: int = 60, max_ms: int = 180) -> None:
    time.sleep(random.uniform(min_ms/1000, max_ms/1000))

def wait_for_ready(page: Page) -> None:
    # networkidle is useful, but some apps never go idle.
    # Start with domcontentloaded then a tiny jitter.
    page.wait_for_load_state("domcontentloaded")
    jitter(80, 160)

def safe_click(page: Page, selector: str) -> None:
    loc: Locator = page.locator(selector)
    loc.wait_for(state="visible")
    loc.click()
    jitter()

def type_like_human(page: Page, selector: str, text: str, clear_first: bool = True) -> None:
    loc = page.locator(selector)
    loc.wait_for(state="visible")
    if clear_first:
        loc.fill("")
        jitter(40, 80)
    for ch in text:
        loc.type(ch, delay=random.randint(15, 45))
    jitter()

def screenshot(page: Page, path: str) -> None:
    page.screenshot(path=path, full_page=True)
