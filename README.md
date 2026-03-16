# Playwright Transaction Bot – SauceDemo

**Production-grade UI automation example** built with **Python + Playwright** (sync API).  
Demonstrates clean architecture, reusable helpers, environment management, stable interaction patterns, logging, and realistic end-to-end scraping workflow.

This project is intended as a portfolio-quality example of maintainable UI automation,
not a full testing framework or scraping tool.


<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue?style=flat-square&logo=python&logoColor=white" alt="Python version">
  <img src="https://img.shields.io/badge/Playwright-latest-success?style=flat-square&logo=playwright&logoColor=white" alt="Playwright">
  <img src="https://img.shields.io/badge/pytest-enabled-brightgreen?style=flat-square" alt="pytest">
</p>


##  Features

- Stable login automation against SauceDemo
- Human-like typing with configurable delays
- Flakiness-resistant interaction helpers (`safe_click`, explicit waits)
- Environment-based configuration via `.env` files
- CLI flags for headless, slow-motion, and debug modes
- Structured JSON output for scraped inventory data
- Optional screenshot capture for debugging
- End-to-end smoke testing with pytest



## Why This Project Exists

This project demonstrates how to build **production-grade browser automation** in Python using Playwright.
It focuses on reliability, maintainability, and real-world interaction patterns rather than quick scripts.

Key goals:
- Avoid flaky UI automation
- Separate concerns (browser, auth, actions, scraping)
- Support multiple environments cleanly
- Provide a realistic end-to-end automation workflow




##  Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/playwright-saucedemo-bot.git
cd playwright-saucedemo-bot

# 2. Create & activate virtual environment
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
playwright install --with-deps

# 4. Prepare demo configuration (uses standard demo credentials)
cp .env.example .env.demo

# 5. Run – headed + slow motion (great for demos / debugging)
python main.py --env demo --headless false --slow 250

# 6. Run headless (production-like / CI)
python main.py --env demo
```



##  Tech Stack

| Component            | Technology              | Purpose                                   |
|----------------------|--------------------------|-------------------------------------------|
| Browser Automation   | Playwright (Sync API)    | Reliable and consistent cross-browser automation |
| Test Framework       | pytest                   | Lightweight framework for smoke and validation tests |
| Configuration        | python-dotenv            | Secure, environment-based configuration management |
| Filesystem Handling  | pathlib                  | Modern, safe, and platform-independent path handling |


##  Project Structure

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


## Architecture Overview

The project follows a modular design to keep responsibilities isolated:

- `browser.py` handles Playwright setup and lifecycle
- `auth.py` encapsulates login behavior
- `actions.py` provides safe, reusable UI interactions
- `scraper.py` focuses solely on data extraction and export
- `main.py` acts as a CLI orchestrator

This separation improves testability, readability, and long-term maintainability.


##  Configuration

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


##  Usage Examples

```
# Normal run (headless)
python main.py --env demo

# Debug: visible browser + 250 ms delay between actions
python main.py --env demo --headless false --slow 250

# Very slow – great for recording or presentations
python main.py --env demo --slow 800
```


##  Tests
```
# Run smoke test suite (validates full flow)
pytest -v

# Run with HTML report
pytest --html=report.html
```




