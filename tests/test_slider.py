
import random

from playwright.sync_api import Page

from pages.slider_page import HorizontalSliderPage


def test_horizontal_slider_random_value(page: Page) -> None:
    slider_page = HorizontalSliderPage(page)
    slider_page.open(slider_page.URL)

    target_steps = random.randint(1, 9)
    expected_value = target_steps * 0.5

    slider_page.set_slider_value(expected_value)

    actual_value = slider_page.get_slider_value()

    assert actual_value == expected_value, (
        f"Expected slider value: {expected_value}, "
        f"actual value: {actual_value}"
    )
