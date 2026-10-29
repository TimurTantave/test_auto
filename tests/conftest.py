
import pytest
from playwright.sync_api import Browser, BrowserContext, Page, Playwright, sync_playwright

from logger import setup_logger


@pytest.fixture(scope="session", autouse=True)
def init_logger():
    setup_logger()


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="session")
def browser(playwright_instance: Playwright) -> Browser:
    browser = playwright_instance.chromium.launch(
        channel="chrome",
        headless=True,
    )
    yield browser
    browser.close()


@pytest.fixture
def context(browser: Browser) -> BrowserContext:
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture
def page(context: BrowserContext) -> Page:
    page = context.new_page()
    page.set_default_timeout(10_000)
    return page


@pytest.fixture
def auth_context(browser: Browser) -> BrowserContext:
    context = browser.new_context(
        http_credentials={
            "username": "admin",
            "password": "admin",
        }
    )
    yield context
    context.close()


@pytest.fixture
def auth_page(auth_context: BrowserContext) -> Page:
    page = auth_context.new_page()
    page.set_default_timeout(10_000)
    yield page
    page.close()

