
from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.web_element import WebElement


class AlertsPage(BasePage):

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.js_alert_button = WebElement(
            page.locator("button[onclick='jsAlert()']"),
            description="JS Alert button",
        )
        self.js_confirm_button = WebElement(
            page.locator("button[onclick='jsConfirm()']"),
            description="JS Confirm button",
        )
        self.js_prompt_button = WebElement(
            page.locator("button[onclick='jsPrompt()']"),
            description="JS Prompt button",
        )
        self.result = WebElement(
            page.locator("#result"),
            description="JavaScript alert result",
        )

    def click_js_alert(self) -> None:
        self.actions.run_and_accept_alert(
            self.js_alert_button.click
        )

    def click_js_confirm(self) -> None:
        self.actions.run_and_accept_alert(
            self.js_confirm_button.click
        )

    def click_js_prompt(self, text: str) -> None:
        self.actions.run_and_accept_prompt(
            self.js_prompt_button.click,
            text,
        )

    def get_result(self) -> str:
        return self.result.get_inner_text()
