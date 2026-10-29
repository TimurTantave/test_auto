import re

from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.multi_web_element import MultiWebElement


class HoversPage(BasePage):
    URL = "https://the-internet.herokuapp.com/hovers"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.user_images = MultiWebElement(
            page=self.page,
            locator=self.page.locator(".figure img"),
            description="User images",
        )

        self.user_names = MultiWebElement(
            page=self.page,
            locator=self.page.locator(".figure .figcaption h5"),
            description="User names",
        )

    def get_users_count(self) -> int:
        return self.user_images.count()

    def hover_user(self, index: int) -> None:
        self.user_images.nth(index).hover()

    def get_user_name(self, index: int) -> str:
        return self.user_names.nth(index).get_inner_text()

    def is_valid_user_name(self, name: str) -> bool:
        return re.fullmatch(r"name: user\d+", name) is not None