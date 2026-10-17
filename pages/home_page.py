
from playwright.sync_api import Page

from config.config_reader import ConfigReader
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.config = ConfigReader()

        self.search_input = self.page.get_by_test_id("search-input")
        self.search_button = self.page.get_by_test_id("search-button")

    def open_home_page(self):
        self.open(self.config.get("base_url"))


    def search(self,search_text: str):
        self.search_input.fill(search_text)
        self.search_button.click()