
from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.new_window_page import NewWindowPage
from ui.web_element import WebElement


class WindowsPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.click_here_link = WebElement(
            locator=self.page.get_by_role("link", name="Click Here"),
            description="Click Here link",
        )

    def open_new_window(self) -> NewWindowPage:
        with self.actions.expect_new_page() as new_page_info:
            self.click_here_link.click()

        new_page = new_page_info.value
        new_page.wait_for_load_state()

        return NewWindowPage(new_page)

    def return_to_original_tab(self) -> None:
        self.actions.bring_to_front()