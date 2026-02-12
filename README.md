# Playwright Transaction Bot – SauceDemo

**Production-grade UI automation example** built with **Python + Playwright** (sync API).  
Demonstrates clean architecture, reusable helpers, environment management, stable interaction patterns, logging, and realistic end-to-end scraping workflow.


<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue?style=flat-square&logo=python&logoColor=white" alt="Python version">
  <img src="https://img.shields.io/badge/Playwright-latest-success?style=flat-square&logo=playwright&logoColor=white" alt="Playwright">
  <img src="https://img.shields.io/badge/pytest-enabled-brightgreen?style=flat-square" alt="pytest">
</p>

## ✨ Features

- **Stable login automation** to SauceDemo
- **Human-like typing** simulation with configurable delays
- **Flakiness-resistant** interaction helpers (`safe_click`, explicit waits)
- **Environment-based configuration** via `.env` files
- **CLI overrides** for headless/slow-motion/debug modes
- **Structured JSON output** of scraped inventory data
- **Automatic screenshot** capture on demand
- **Smoke test** suite with pytest

## ⚡ Quick Start

```bash
# 1. Clone and prepare environment
git clone https://github.com/YOUR_USERNAME/playwright-saucedemo-bot.git
cd playwright-saucedemo-bot

# 2. Create virtual environment & install dependencies
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
playwright install --with-deps

# 3. Create a demo config (or use your own credentials)
cp .env.example .env.demo

# 4. Run the bot (headed + slow motion – great for demos)
python main.py --env demo --headless false --slow 250

# 5. Run in background (production-like)
python main.py --env demo
```
## 🛠️ Tech Stack

| Component            | Technology              | Purpose                                   |
|----------------------|--------------------------|-------------------------------------------|
| Browser Automation   | Playwright (Sync API)    | Reliable and consistent cross-browser automation |
| Test Framework       | pytest                   | Lightweight framework for smoke and validation tests |
| Configuration        | python-dotenv            | Secure, environment-based configuration management |
| Filesystem Handling  | pathlib                  | Modern, safe, and platform-independent path handling |

## 📂 Project Structure

```text
├── bot/
│   ├── actions.py        # Reusable UI helpers (safe_click, type_like_human, etc.)
│   ├── auth.py           # Login page object and authentication logic
│   ├── browser.py        # Browser and context factory
│   ├── config.py         # Environment variable and settings loader
│   └── scraper.py        # Inventory scraping and JSON export
│
├── tests/
│   └── test_flow.py      # End-to-end smoke test
│
├── data/
│   └── output.json       # Scraped results (gitignored)
│
├── .env.example          # Environment variable template
├── main.py               # CLI entry point
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## 🔐 Configuration

Multiple environments are supported via .env files:

1. .env          (default / local development) 
2. .env.demo     (standard demo credentials) 
3. .env.ci       (optional – for pipelines) 

Example .env.demo:

```
BASE_URL=https://www.saucedemo.com
USERNAME=standard_user
PASSWORD=secret_sauce
OUTPUT_DIR=data
SCREENSHOT_DIR=screenshots
```

## ▶️ Usage Examples

```
# Normal run (headless)
python main.py --env demo

# Debug: visible browser + 250 ms delay between actions
python main.py --env demo --headless false --slow 250

# Very slow – great for recording or presentations
python main.py --env demo --slow 800
```

## 🧪 Tests
```
# Run smoke test suite (validates full flow)
pytest -v

# Run with HTML report
pytest --html=report.html
```

## Why This Project Exists

This project demonstrates how to build **production-grade browser automation** in Python using Playwright.
It focuses on reliability, maintainability, and real-world interaction patterns rather than quick scripts.

Key goals:
- Avoid flaky UI automation
- Separate concerns (browser, auth, actions, scraping)
- Support multiple environments cleanly
- Provide a realistic end-to-end automation workflow


