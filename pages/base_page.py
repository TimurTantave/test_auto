from ui.page_actions import PageActions
from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.actions = PageActions(page)