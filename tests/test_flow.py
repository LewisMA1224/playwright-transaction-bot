from bot.browser import launch_context
from bot.auth import login
from bot.scraper import scrape

def test_flow_smoke():
    context, cleanup = launch_context()
    page = context.new_page()
    try:
        login(page)
        data = scrape(page)
        assert "items" in data
    finally:
        cleanup()
