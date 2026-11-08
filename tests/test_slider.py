
import random

from playwright.sync_api import Page

from pages.slider_page import HorizontalSliderPage


def test_horizontal_slider_random_value(page: Page) -> None:
    URL = "https://the-internet.herokuapp.com/horizontal_slider"
    page.goto(URL)

    slider_page = HorizontalSliderPage(page)

    min_value, max_value, step = slider_page.get_slider_parameters()

    possible_steps = round((max_value - min_value) / step)
    target_steps = random.randint(0, possible_steps)
    expected_value = min_value + target_steps * step

    slider_page.set_slider_value(expected_value)

    actual_value = slider_page.get_slider_value()

    assert actual_value == expected_value, (
        f"Slider value mismatch. "
        f"Expected: '{expected_value}', Actual: '{actual_value}'"
    )
