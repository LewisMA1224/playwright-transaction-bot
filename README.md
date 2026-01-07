# Playwright Transaction Bot (SauceDemo)

A production-style automation bot built with **Python + Playwright**, designed to demonstrate real-world testing practices, reusable actions, environment management, and clean automation architecture.

This project is structured exactly like a junior QA automation engineer or SDET would build it — with proper logging, config separation, CLI overrides, and a full automated scraping workflow.

---

## 🚀 Features

### **🔐 Login Automation**
- Navigates to SauceDemo  
- Enters credentials  
- Logs in and waits for inventory to load  

### **🔁 Reusable Actions (`bot/actions.py`)**
- `safe_click` — waits for an element to appear, then clicks  
- `type_like_human` — realistic typing with configurable delays  
- `wait_for_ready` — simple page-ready helper  
- `screenshot` — captures a screenshot to the configured directory  

These functions make the bot stable and production-grade.

### **⚙️ Environment-Driven Config (`bot/config.py`)**
Supports multiple environments using `.env` files:
- `.env` (default)
- `.env.demo`
- `.env.local`

Choose an environment at runtime:
```bash
python main.py --env demo

🧪 End-to-End Test (tests/test_flow.py)

A pytest test validates:

The scraper loads

Items are extracted

JSON output is created

No exceptions occur

Run tests:

pytest -q

📦 Structured Output (bot/scraper.py)

Scrapes product cards and outputs JSON like:

{
  "timestamp": "2026-01-08T06:38:53",
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

📝 Logging & Failure Debugging

Saves screenshots on failure

Writes logs to logs/run.log

Tracks run start, completion, and item count

⚙️ Installation
1. Clone the repository
git clone https://github.com/YOUR_USERNAME/playwright-transaction-bot.git
cd playwright-transaction-bot

2. Install dependencies
pip install -r requirements.txt
python -m playwright install

3. Set environment variables

The bot reads configuration from .env files.

Examples:

.env        → default
.env.demo   → demo environment
.env.local  → local overrides

▶️ Running the Bot

Default run

python main.py


Choose an environment

python main.py --env demo


Disable headless

python main.py --headless false


Slow motion for debugging

python main.py --slow 300

🧪 Running the Test Suite
pytest -q

📁 Project Structure
playwright-transaction-bot/
├── bot/
│   ├── actions.py      # reusable actions
│   ├── auth.py         # login flow
│   ├── browser.py      # browser launcher
│   ├── config.py       # loads .env files
│   ├── scraper.py      # scrapes product data
│   └── __init__.py
│
├── tests/
│   └── test_flow.py    # pytest e2e test
│
├── data/
│   └── output.json     # saved scrape results
│
├── logs/
│   └── run.log         # run history + errors
│
├── screenshots/        # failure screenshots
├── .env
├── .env.demo
├── .gitignore
├── main.py             # CLI entrypoint
└── requirements.txt
│── README.md

