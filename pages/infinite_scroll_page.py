
from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.multi_web_element import MultiWebElement


class InfiniteScrollPage(BasePage):
    URL = "https://the-internet.herokuapp.com/infinite_scroll"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.paragraphs = MultiWebElement(
            page=self.page,
            locator=self.page.locator(
                ".jscroll-inner .jscroll-added"
            ),
            description="Infinite scroll paragraphs",
        )

    def get_paragraphs_count(self) -> int:
        return self.paragraphs.count()

    def scroll_down(self) -> None:
        self.page.mouse.wheel(0, 1000)
