
from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.web_element import WebElement


class ContextMenuPage(BasePage):

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.hot_spot = WebElement(
            page.locator("#hot-spot"),
            description="Context menu hot spot",
        )

    def right_click_hot_spot(self) -> None:
        self.hot_spot.right_click()
