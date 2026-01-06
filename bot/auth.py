from playwright.sync_api import Page
from .config import SETTINGS
from .actions import wait_for_ready, type_like_human, safe_click

def is_logged_in(page: Page) -> bool:
    # Best SauceDemo signal: inventory list exists
    return page.locator(".inventory_list").count() > 0 or "inventory.html" in page.url

def login(page: Page) -> None:
    # Go to login page first (clean start)
    page.goto(SETTINGS.login_url)
    wait_for_ready(page)

    # If already logged in, going to login will often redirect or show inventory if session is valid
    if is_logged_in(page):
        return

    # Fill creds and login
    type_like_human(page, "#user-name", SETTINGS.username)
    type_like_human(page, "#password", SETTINGS.password)
    safe_click(page, "#login-button")

    # Confirm we truly landed in inventory
    page.wait_for_url("**/inventory.html")
    page.wait_for_selector(".inventory_list", state="visible")
    wait_for_ready(page)

