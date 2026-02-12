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



## 🧪 Automation Flow

1. Launches a Playwright browser context
2. Navigates to SauceDemo
3. Logs in using environment-based credentials
4. Waits for the inventory page to load
5. Scrapes product name, price, and description
6. Saves structured JSON output to `data/output.json`

---

## 🧰 Tech Stack

- **Python 3**
- **Playwright (sync API)**
- **pytest**
- **python-dotenv**

---

## 🛠 Setup

```bash
python -m venv .venv
# Windows (PowerShell)
.\.venv\Scripts\activate

pip install -r requirements.txt
playwright install




