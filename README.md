# Playwright Transaction Bot (SauceDemo)

A production-style automation bot built with **Python + Playwright**, designed to demonstrate real-world testing practices, reusable actions, environment management, and clean automation architecture.

This project is structured exactly like a junior QA automation engineer or SDET would build it — with proper logging, config separation, CLI overrides, and a full automated scraping workflow.

---

## ✨ Features

---

## 🔐 Login Automation

- Navigates to SauceDemo  
- Enters credentials  
- Logs in and waits for inventory to load  

---

## 🧩 Reusable Actions (`bot/actions.py`)

- `safe_click` — waits for an element and clicks reliably  
- `type_like_human` — realistic typing with variable delays  
- `wait_for_ready` — simple page-ready helper  
- `screenshot` — captures screenshots into the configured directory  

These functions keep the bot stable and production-grade.

---

## ⚙️ Environment-Driven Config (`bot/config.py`)

Supports multiple environments using `.env` files:

- `.env` (default)  
- `.env.demo`  
- `.env.local`  

Choose an environment at runtime:

```bash
python main.py --env demo

Mark Lewis
Technical Systems Analyst • Python Automation • Playwright
(Feel free to connect or send opportunities.)

