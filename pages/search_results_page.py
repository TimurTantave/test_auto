from playwright.sync_api import Page

from pages.base_page import BasePage

class SearchResultsPage(BasePage):
    def __init__(self, page:Page):
        super().__init__(page)

        self.sort_select = self.page.get_by_test_id("filter-sort")
        self.apply_filter_button = self.page.get_by_test_id(
            "apply-filters-button"
        )
        self.cards = self.page.locator(
            '[data-testid^="search-result-card-"]'
        )
        self.prices = self.page.locator(
            '[data-testid^="search-result-price-"]'
        )

    def sort_by_price(self, order: str):
        self.sort_select.select_option(order)

        self.page.locator(
            '[data-testid="results-region"].is-loading'
        ).wait_for(state="hidden")

    def get_cards_price(self,nums: int):
        prices = self.prices.all()[:nums]
        return [price.inner_text() for price in prices]