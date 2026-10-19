from playwright.sync_api import Page
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.search_input = self.page.get_by_test_id("search-input")
        self.search_button = self.page.get_by_test_id("search-button")

    def search(self, search_text: str):
        self.search_input.fill(search_text)
        self.search_button.click()
