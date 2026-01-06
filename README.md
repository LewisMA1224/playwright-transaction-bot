# Playwright Transaction Bot (SauceDemo)

A small, production-style web automation bot built with **Python + Playwright**.

The bot:

- Logs into [SauceDemo](https://www.saucedemo.com/)
- Scrapes all inventory items (name, price, description)
- Saves structured JSON to `data/output.json`
- Supports multiple environments via `.env` files
- Allows CLI overrides for headless mode and slow-motion
- Captures screenshots on failure and writes a run log
- Includes an end-to-end pytest to keep the flow stable

---

## Features

- **Login automation**  
  Uses Playwright to open SauceDemo, enter credentials, and log in.

- **Reusable actions** (`bot/actions.py`)  
  - `safe_click` – waits for element to be visible before clicking  
  - `type_like_human` – waits for input to be ready, types text  
  - `wait_for_ready` – small helper to wait for page state  
  - `screenshot` – captures a screenshot to the configured directory

- **Config-driven** (`bot/config.py`)  
  Configuration is loaded from `.env` files based on `APP_ENV`, so you can switch between environments without changing code.

- **Structured output** (`bot/scraper.py`)  
  Scrapes the product cards and outputs JSON in this shape:

  ```json
  {
    "timestamp": "2026-01-06T06:38:53",
    "source": "saucedemo",
    "count": 6,
    "items": [
      {
        "name": "Sauce Labs Backpack",
        "price": "$29.99",
        "description": "carry.allTheThings() with the sleek..."
      }
    ]
  }
