from playwright.sync_api import sync_playwright, BrowserContext
from .config import SETTINGS


def launch_context(
    headless: bool | None = None,
    slow_mo_ms: int | None = None,
) -> tuple[BrowserContext, callable]:
    """
    Launch a persistent browser context.

    CLI / runtime overrides:
        - headless: if provided, overrides SETTINGS.headless
        - slow_mo_ms: if provided, overrides SETTINGS.slow_mo_ms
    """
    pw = sync_playwright().start()

    effective_headless = SETTINGS.headless if headless is None else headless
    effective_slow_mo = SETTINGS.slow_mo_ms if slow_mo_ms is None else slow_mo_ms

    context = pw.chromium.launch_persistent_context(
        user_data_dir=SETTINGS.user_data_dir,
        headless=effective_headless,
        slow_mo=effective_slow_mo,
        viewport={"width": 1280, "height": 800},
    )

    context.set_default_timeout(SETTINGS.timeout_ms)

    def cleanup():
        try:
            context.close()
        finally:
            pw.stop()

    return context, cleanup
