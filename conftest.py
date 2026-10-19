
import pytest
from playwright.sync_api import sync_playwright

from config.config_reader import ConfigReader


@pytest.fixture(scope="session")
def config():
    return ConfigReader()


@pytest.fixture
def page(config):
    with sync_playwright() as playwright:
        browser_type = getattr(playwright, config.get("browser"))

        browser = browser_type.launch(
            headless=config.get("headless")
        )

        browser_context = browser.new_context()
        page = browser_context.new_page()
        page.set_default_timeout(config.get("timeout"))

        yield page

        browser_context.close()
        browser.close()
