from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.web_element import WebElement


class BasicAuthPage(BasePage):

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.success_message = WebElement(
            page.locator("div.example p"),
            description="Basic Auth success message",
        )

    def get_success_message(self) -> str:
        return self.success_message.get_inner_text()
