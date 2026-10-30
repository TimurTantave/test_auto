from playwright.sync_api import Page, expect, TimeoutError as PlaywrightTimeoutError

from pages.base_page import BasePage
from ui.multi_web_element import MultiWebElement


class InfiniteScrollPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.paragraphs = MultiWebElement(
            page=self.page,
            locator=self.page.locator(".jscroll-inner .jscroll-added"),
            description="Infinite scroll paragraphs",
        )

    def get_paragraphs_count(self) -> int:
        return self.paragraphs.count()

    def scroll_until_paragraphs_count(self, expected_count: int) -> None:
        while self.get_paragraphs_count() < expected_count:
            self.paragraphs.last().scroll_into_view_if_needed()