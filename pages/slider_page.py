
from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.web_element import WebElement


class HorizontalSliderPage(BasePage):

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

    def get_slider_parameters(self) -> tuple[float, float, float]:
        min_value = float(self.slider.get_attribute("min"))
        max_value = float(self.slider.get_attribute("max"))
        step = float(self.slider.get_attribute("step"))

        return min_value, max_value, step

    def set_slider_value(self, target_value: float) -> None:
        min_value, _, step = self.get_slider_parameters()

        self.slider.focus()
        self.slider.press("Home")

        steps = round((target_value - min_value) / step)

        for _ in range(steps):
            self.slider.press("ArrowRight")

    def get_slider_value(self) -> float:
        return float(self.slider_value.get_inner_text())