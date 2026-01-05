from playwright.sync_api import sync_playwright, expect
import csv
import os
from datetime import datetime

URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"

EXPORT_DIR = "exports"
SCREENSHOT_DIR = "screenshots"
CSV_PATH = os.path.join(EXPORT_DIR, "transactions.csv")


def ensure_dirs():
    os.makedirs(EXPORT_DIR, exist_ok=True)
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)


def append_csv(row: dict):
    file_exists = os.path.exists(CSV_PATH)
    fieldnames = list(row.keys())

    with open(CSV_PATH, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)


def run():
    ensure_dirs()
    started_at = datetime.now().isoformat(timespec="seconds")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        try:
            # 1) Login
            page.goto(URL)
            page.fill("#user-name", USERNAME)
            page.fill("#password", PASSWORD)
            page.click("#login-button")

            expect(page.locator(".title")).to_have_text("Products")

            # 2) Add item + go to cart
            page.click('[data-test="add-to-cart-sauce-labs-backpack"]')
            page.click(".shopping_cart_link")

            expect(page.locator(".title")).to_have_text("Your Cart")

            # 3) Capture "transaction" details from cart
            item_name = page.locator(".inventory_item_name").first.inner_text().strip()
            item_price_text = page.locator(".inventory_item_price").first.inner_text().strip()

            # item_price_text like "$29.99"
            item_price = float(item_price_text.replace("$", "").strip())

            # 4) Checkout flow
            page.click('[data-test="checkout"]')
            expect(page.locator(".title")).to_have_text("Checkout: Your Information")

            page.fill('[data-test="firstName"]', "Mark")
            page.fill('[data-test="lastName"]', "Lewis")
            page.fill('[data-test="postalCode"]', "27601")
            page.click('[data-test="continue"]')

            expect(page.locator(".title")).to_have_text("Checkout: Overview")

            # Capture totals from overview
            item_total_text = page.locator(".summary_subtotal_label").inner_text().strip()
            tax_text = page.locator(".summary_tax_label").inner_text().strip()
            total_text = page.locator(".summary_total_label").inner_text().strip()

            # Parse like "Item total: $29.99"
            def parse_money(label: str) -> float:
                return float(label.split("$")[-1].strip())

            item_total = parse_money(item_total_text)
            tax = parse_money(tax_text)
            total = parse_money(total_text)

            page.click('[data-test="finish"]')
            expect(page.locator(".title")).to_have_text("Checkout: Complete!")

            expect(page.locator(".complete-header")).to_have_text("Thank you for your order!")

            screenshot_path = os.path.join(SCREENSHOT_DIR, "success.png")
            page.screenshot(path=screenshot_path, full_page=True)

            # 5) Write CSV record
            row = {
                "timestamp": started_at,
                "site": "saucedemo",
                "action": "checkout_demo",
                "item": item_name,
                "item_price": f"{item_price:.2f}",
                "item_total": f"{item_total:.2f}",
                "tax": f"{tax:.2f}",
                "total": f"{total:.2f}",
                "status": "SUCCESS",
                "screenshot": screenshot_path,
            }
            append_csv(row)

            print("✅ SUCCESS: transaction logged to", CSV_PATH)
            print("✅ Screenshot saved to", screenshot_path)

        except Exception as e:
            # If anything fails, capture proof + log failure
            fail_shot = os.path.join(SCREENSHOT_DIR, "failure.png")
            try:
                page.screenshot(path=fail_shot, full_page=True)
            except:
                pass

            row = {
                "timestamp": started_at,
                "site": "saucedemo",
                "action": "checkout_demo",
                "item": "",
                "item_price": "",
                "item_total": "",
                "tax": "",
                "total": "",
                "status": f"FAIL: {type(e).__name__}",
                "screenshot": fail_shot,
            }
            append_csv(row)

            print("❌ FAILED:", repr(e))
            print("📸 Failure screenshot (if captured):", fail_shot)
            raise
        finally:
            context.close()
            browser.close()


if __name__ == "__main__":
    run()
