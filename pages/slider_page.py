
from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.web_element import WebElement


class HorizontalSliderPage(BasePage):
    URL = "https://the-internet.herokuapp.com/horizontal_slider"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.slider = WebElement(
            self.page.locator('input[type="range"]'),
            description="Horizontal Slider",
        )

        self.slider_value = WebElement(
            self.page.locator("#range"),
            description="Horizontal Slider Value",
        )

    def set_slider_value(self, target_value: float) -> None:
        self.slider.focus()
        self.slider.press("Home")

        steps = round(target_value / 0.5)

        for _ in range(steps):
            self.slider.press("ArrowRight")

    def get_slider_value(self) -> float:
        return float(self.slider_value.get_inner_text())
